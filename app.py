import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import os
import random
from tensorflow.keras.models import load_model

# Import custom styling system
from styles import load_custom_css

# ===============================
# PAGE CONFIG & STYLE LOADING
# ===============================
st.set_page_config(
    page_title="Magic Number Academy",
    page_icon="🎨",
    layout="wide"
)

# Theme Selection Layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    theme = st.radio(
        "🌍 Choose Your World!",
        ["🦄 Magic", "🚀 Space", "🦖 Dino", "🌊 Ocean"],
        index=0,
        horizontal=True,
        label_visibility="collapsed"
    )

load_custom_css(theme)

# ===============================
# LOAD CNN MODEL (Untouched)
# ===============================
MODEL_PATH = "digit_cnn.keras"

if not os.path.exists(MODEL_PATH):
    st.error("❌ CNN model not found!")
    st.stop()

try:
    model = load_model(MODEL_PATH)
except Exception as e:
    st.error(f"Model loading error: {e}")
    st.stop()

# ===============================
# CHILD LEARNING DATA (Dynamic by Theme)
# ===============================
if theme == "🚀 Space":
    number_objects = {
        0: ("🌑", "Moons"),
        1: ("🌍", "Earth"),
        2: ("🚀", "Rockets"),
        3: ("👽", "Aliens"),
        4: ("⭐", "Stars"),
        5: ("🪐", "Planets"),
        6: ("🛸", "UFOs"),
        7: ("☄️", "Comets"),
        8: ("👨‍🚀", "Astronauts"),
        9: ("🛰️", "Satellites")
    }
    app_title = "🚀 Space Number Academy 🌟"
    app_subtitle = "Draw the numbers and explore the galaxy!"
    action_button_text = "✨ LAUNCH MY DRAWING! ✨"
elif theme == "🦖 Dino":
    number_objects = {
        0: ("🥚", "Dino Eggs"),
        1: ("🦖", "T-Rex"),
        2: ("🦕", "Brontosaurus"),
        3: ("🌿", "Leaves"),
        4: ("🌋", "Volcanoes"),
        5: ("🦴", "Bones"),
        6: ("🌴", "Palm Trees"),
        7: ("🐾", "Footprints"),
        8: ("🥩", "Meat"),
        9: ("🏕️", "Tents")
    }
    app_title = "🦖 Dino Number Academy 🌿"
    app_subtitle = "Draw the numbers and discover dinosaurs!"
    action_button_text = "✨ ROAR! CHECK MY DRAWING! ✨"
elif theme == "🌊 Ocean":
    number_objects = {
        0: ("🫧", "Bubbles"),
        1: ("🐋", "Whale"),
        2: ("🐬", "Dolphins"),
        3: ("🐢", "Turtles"),
        4: ("🦀", "Crabs"),
        5: ("🦑", "Squids"),
        6: ("🐠", "Fish"),
        7: ("🐚", "Shells"),
        8: ("🐙", "Octopuses"),
        9: ("🦈", "Sharks")
    }
    app_title = "🌊 Ocean Number Academy 🐠"
    app_subtitle = "Draw the numbers and dive into the deep!"
    action_button_text = "✨ SPLASH! CHECK MY DRAWING! ✨"
else:
    number_objects = {
        0: ("🍩", "Donuts"),
        1: ("🍎", "Apple"),
        2: ("⚽", "Balls"),
        3: ("🦋", "Butterflies"),
        4: ("⭐", "Stars"),
        5: ("🍌", "Bananas"),
        6: ("🐟", "Fish"),
        7: ("🌈", "Rainbows"),
        8: ("🎈", "Balloons"),
        9: ("🚗", "Cars")
    }
    app_title = "🎨 Magic Number Academy 🦄"
    app_subtitle = "Draw the magical numbers and level up your skills!"
    action_button_text = "✨ SHOW MY MAGIC! ✨"

encouragements = [
    "🌟 Amazing!", "🎉 Fantastic work!", "👏 Great writing!",
    "🚀 You are improving!", "⭐ Super job!", "😊 Keep practicing!"
]

# ===============================
# SESSION ENGINE INITIALIZATION
# ===============================
if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0

if "total_count" not in st.session_state:
    st.session_state.total_count = 0

if "target_digit" not in st.session_state:
    st.session_state.target_digit = random.randint(0, 9)

if "show_result" not in st.session_state:
    st.session_state.show_result = False

if "canvas_key" not in st.session_state:
    st.session_state.canvas_key = 0

if "last_status" not in st.session_state:
    st.session_state.last_status = None
if "prediction" not in st.session_state:
    st.session_state.prediction = None
if "model_score" not in st.session_state:
    st.session_state.model_score = 0

# ===============================
# CALLBACKS TO PREVENT BALLOON BUG
# ===============================
def next_number_action():
    st.session_state.target_digit = random.randint(0, 9)
    st.session_state.show_result = False
    st.session_state.canvas_key += 1

def try_again_action():
    st.session_state.show_result = False
    st.session_state.canvas_key += 1

# ===============================
# HEADER BANNER
# ===============================
# ===============================
# GAME HUD (Heads Up Display)
# ===============================
learning_score = (st.session_state.correct_count / st.session_state.total_count * 100) if st.session_state.total_count > 0 else 0
hud_html = f'''
<div class="hud-container">
    <div style="display:flex; align-items:center;">
        <h3 style="margin:0; margin-right:15px; font-weight:900;">{app_title}</h3>
    </div>
    <div class="hud-score">
        <span>⭐ {st.session_state.correct_count}</span>
        <span>📝 {st.session_state.total_count}</span>
        <span>🏆 {learning_score:.0f}%</span>
    </div>
</div>
'''
st.markdown(hud_html, unsafe_allow_html=True)

# ===============================
# SCENE SWAPPING LOGIC
# ===============================

target = st.session_state.target_digit
emoji, object_name = number_objects[target]
object_display = emoji if target == 0 else emoji * target

if not st.session_state.show_result:
    # ===============================
    # SCENE 1: THE GAME CONSOLE
    # ===============================
    with st.container(border=True):
        # Mission Screen
        st.markdown(f'''
        <div class="mission-screen">
            <div>
                <p class="mission-title">MISSION: Draw this number!</p>
                <p style="font-size:20px; font-weight:bold; margin:0; color:#555;">{target} {object_name}</p>
            </div>
            <div class="mission-target">{target}</div>
            <div class="mission-emoji">{object_display}</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Interactive Screen
        canvas = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=20,
            stroke_color="#000000",
            background_color="#FFFFFF",
            height=280, 
            width=280,
            drawing_mode="freedraw",
            key=f"canvas_{st.session_state.canvas_key}"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 3D Arcade Button
        if st.button(action_button_text, use_container_width=True, type="primary"):
            if canvas.image_data is None:
                st.toast("Please draw a number first! 😊", icon="🎨")
            else:
                img = Image.fromarray(canvas.image_data.astype("uint8")).convert("L")
                img_array = 255 - np.array(img)
        
                if np.max(img_array) < 50:
                    st.toast("The board is empty! Draw something first! ⚠️", icon="⚠️")
                else:
                    coords = np.column_stack(np.where(img_array > 0))
                    y_min, x_min = coords.min(axis=0)
                    y_max, x_max = coords.max(axis=0)
        
                    digit = img_array[y_min:y_max+1, x_min:x_max+1]
                    digit_img = Image.fromarray(digit)
                    digit_img.thumbnail((20, 20))
        
                    final_img = Image.new("L", (28, 28), 0)
                    x_offset = (28 - digit_img.size[0]) // 2
                    y_offset = (28 - digit_img.size[1]) // 2
                    final_img.paste(digit_img, (x_offset, y_offset))
        
                    final_array = np.array(final_img).astype("float32") / 255.0
                    cnn_input = final_array.reshape(1, 28, 28, 1)
        
                    prediction_prob = model.predict(cnn_input, verbose=0)
                    prediction = np.argmax(prediction_prob)
                    model_score = np.max(prediction_prob) * 100
                    
                    st.session_state.total_count += 1
                    st.session_state.prediction = prediction
                    st.session_state.model_score = model_score
                    
                    if prediction == target:
                        st.session_state.correct_count += 1
                        st.session_state.last_status = "success"
                    else:
                        st.session_state.last_status = "fail"
                    
                    st.session_state.show_result = True
                    st.rerun()

else:
    # ===============================
    # SCENE 2: THE CELEBRATION BOX
    # ===============================
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True) # Spacer
    
    if st.session_state.last_status == "success":
        if theme == "🚀 Space" or theme == "🌊 Ocean": st.snow()
        else: st.balloons()
        
        message = random.choice(encouragements)
        st.markdown(f'''
        <div class="success-card" style="max-width: 600px; margin: 0 auto; transform: scale(1.1);">
            <h1 style="font-size:50px; margin-bottom:10px;">{message}</h1>
            <p style="font-size:24px;">You beautifully wrote the number <b style="font-size:40px;">{st.session_state.prediction}</b>!</p>
            <div style="margin: 20px 0; font-size:60px;">{object_display}</div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.button("🌟 NEXT LEVEL! 🌟", use_container_width=True, on_click=next_number_action, type="primary")

    else:
        st.markdown(f'''
        <div class="fail-card" style="max-width: 600px; margin: 0 auto; transform: scale(1.1);">
            <h1 style="font-size:45px; margin-bottom:10px;">😊 Splendid Effort!</h1>
            <p style="font-size:24px;">The computer saw a <b style="font-size:30px;">{st.session_state.prediction}</b>.</p>
            <p style="font-size:24px;">Let's try drawing a <b style="font-size:30px;">{target}</b> again!</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        action_col1, action_col2 = st.columns(2)
        with action_col1:
            st.button("🔄 RETRY LEVEL", use_container_width=True, on_click=try_again_action)
        with action_col2:
            st.button("⏭ SKIP LEVEL", use_container_width=True, on_click=next_number_action)