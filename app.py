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

# Theme Selection
theme = st.sidebar.selectbox(
    "🌍 Choose Your World!",
    ["🦄 Magic", "🚀 Space", "🦖 Dino"]
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
st.markdown(f"""
<div class="title-banner">
    <h1>{app_title}</h1>
    <p>{app_subtitle}</p>
</div>
""", unsafe_allow_html=True)

# ===============================
# SCORE DISPLAY
# ===============================
m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(
        f"""
        <div class="score-board">
        🌟 Stars Earned<br>
        <span style="font-size: 24px;">{"⭐"*min(st.session_state.correct_count, 7) if st.session_state.correct_count > 0 else "✨"}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

with m2:
    st.metric("📝 Tries ✨", st.session_state.total_count)

with m3:
    if st.session_state.total_count > 0:
        learning_score = (st.session_state.correct_count / st.session_state.total_count) * 100
    else:
        learning_score = 0
    st.metric("🏆 Power Level 🌟", f"{learning_score:.0f}%")

st.markdown("<br>", unsafe_allow_html=True)

# ===============================
# PLAYSPACE COLUMNS
# ===============================
left_col, right_col = st.columns([1, 1], gap="large")

target = st.session_state.target_digit
emoji, object_name = number_objects[target]

with left_col:
    st.markdown('<div class="kids-card">', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 22px; font-weight: bold; margin:0;">Your Challenge Sparkle:</p>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="target-box">
        <div class="target-num">{target}</div>
    </div>
    """, unsafe_allow_html=True)
    
    object_display = emoji if target == 0 else emoji * target
    
    st.markdown(f"""
    <div class="object-display">{object_display}</div>
    <div class="object-label">{target} {object_name}</div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="kids-card">', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; font-weight: bold; margin-bottom: 15px;">✏️ Draw the number {target} on the magic board below:</p>', unsafe_allow_html=True)
    
    c_left, c_mid, c_right = st.columns([1, 5, 1])
    with c_mid:
        canvas = st_canvas(
            fill_color="black",
            stroke_width=14,  # Smooth canvas stroke width
            stroke_color="white",
            background_color="black",
            height=280,
            width=280,
            drawing_mode="freedraw",
            key=f"canvas_{st.session_state.canvas_key}"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button(action_button_text, use_container_width=True, type="primary"):
        if canvas.image_data is None:
            st.warning("Please draw a number first 😊")
        else:
            st.session_state.show_result = True
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# CNN PROCESSING & RENDERING (Logic Safe)
# ===============================
if st.session_state.show_result:
    st.markdown("---")
    
    img = Image.fromarray(canvas.image_data.astype("uint8"))
    img = img.convert("L")
    img_array = np.array(img)

    if np.max(img_array) == 0:
        st.warning("Please draw something beautiful on the board first!")
        st.session_state.show_result = False
    else:
        # Pipeline calculations
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

        final_array = np.array(final_img)
        final_array = final_array.astype("float32") / 255.0
        cnn_input = final_array.reshape(1, 28, 28, 1)

        prediction_prob = model.predict(cnn_input, verbose=0)
        prediction = np.argmax(prediction_prob)
        model_score = np.max(prediction_prob) * 100

        st.session_state.total_count += 1

        # SUCCESS
        if prediction == target:
            st.session_state.correct_count += 1
            if theme == "🚀 Space":
                st.snow()
            else:
                st.balloons()
            message = random.choice(encouragements)
            
            st.markdown(f"""
            <div class="success-card">
                <h2 style="margin:0; font-size:38px;">{message}</h2>
                <p style="font-size:24px; margin: 15px 0;">You beautifully wrote the number <b style="font-size:32px;">{prediction}</b>!</p>
                <span style="background: rgba(26, 188, 156, 0.15); padding: 6px 16px; border-radius: 12px; font-size:14px; font-weight:bold;">
                    ✨ Match Meter: {model_score:.0f}%
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.button("🚀 Journey to a New Number", use_container_width=True, on_click=next_number_action)

        # TRY AGAIN
        else:
            st.markdown(f"""
            <div class="fail-card">
                <h2 style="margin:0; font-size:34px;">😊 Splendid Effort!</h2>
                <p style="font-size:22px; margin: 15px 0;">Oops! My magic lens saw a <b>{prediction}</b>, let's try drawing a <b>{target}</b> again!</p>
                <span style="background: rgba(231, 76, 60, 0.15); padding: 6px 16px; border-radius: 12px; font-size:14px; font-weight:bold;">
                    ✨ Match Meter: {model_score:.0f}%
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            action_col1, action_col2 = st.columns(2)
            
            with action_col1:
                st.button("🔄 Give it Another Go!", use_container_width=True, on_click=try_again_action)
                    
            with action_col2:
                st.button("⏭ Try a Different Number", use_container_width=True, on_click=next_number_action)

# ===============================
# FOOTER
# ===============================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; padding: 20px;'>
    <h3 style='font-weight:bold;'>🌈 Every single trace makes you sharper! Keep going, Little Genius! 🌈</h3>
</div>
""", unsafe_allow_html=True)