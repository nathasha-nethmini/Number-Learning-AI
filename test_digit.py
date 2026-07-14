import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import joblib
import os
import random


# Page configuration
st.set_page_config(page_title="Number Learning Game", layout="wide")

# Load trained model
if not os.path.exists("digit_classifier.pkl"):
    st.error("Error: digit_classifier.pkl not found. Please train the model first.")
    st.stop()

try:
    model = joblib.load("digit_classifier.pkl")
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

# Initialize session state
if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0
if "total_count" not in st.session_state:
    st.session_state.total_count = 0
if "target_digit" not in st.session_state:
    st.session_state.target_digit = random.randint(0, 9)
if "predicted_digit" not in st.session_state:
    st.session_state.predicted_digit = None
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "canvas_key" not in st.session_state:
    st.session_state.canvas_key = 0

# Custom CSS for child-friendly styling
st.markdown("""
    <style>
        * {
            font-family: 'Comic Sans MS', 'Arial Rounded MT Bold', cursive;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .main-title {
            text-align: center;
            background: linear-gradient(90deg, #FF6B9D, #FFE66D, #95E1D3);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 70px;
            font-weight: 900;
            margin-bottom: 5px;
            text-shadow: 3px 3px 0px rgba(0,0,0,0.1);
            letter-spacing: 2px;
        }
        
        .subtitle {
            text-align: center;
            color: #FFE66D;
            font-size: 32px;
            margin-bottom: 30px;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .stats-box {
            text-align: center;
            font-size: 28px;
            padding: 25px;
            border-radius: 20px;
            margin: 15px 0;
            font-weight: bold;
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
            transform: scale(1);
            transition: transform 0.3s;
            border: 3px solid white;
        }
        
        .stats-box:hover {
            transform: scale(1.05);
        }
        
        .stats-correct {
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
            color: #2C3E50;
        }
        
        .stats-total {
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            color: #2C3E50;
        }
        
        .stats-score {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            color: #2C3E50;
        }
        
        .good-job {
            background: linear-gradient(135deg, #FFD93D 0%, #FFE66D 100%);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #2C3E50;
            box-shadow: 0 10px 30px rgba(255, 217, 61, 0.4);
            border: 5px solid #FFB700;
            margin: 20px 0;
        }
        
        .needs-practice {
            background: linear-gradient(135deg, #FF9999 0%, #FFB3B3 100%);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: white;
            box-shadow: 0 10px 30px rgba(255, 153, 153, 0.4);
            border: 5px solid #FF7777;
            margin: 20px 0;
        }
        
        .target-number {
            background: linear-gradient(135deg, #95E1D3 0%, #4ECDC4 100%);
            padding: 40px;
            border-radius: 25px;
            text-align: center;
            font-size: 120px;
            font-weight: 900;
            color: white;
            margin: 30px 0;
            box-shadow: 0 15px 40px rgba(78, 205, 196, 0.4);
            border: 5px dashed #2C3E50;
            text-shadow: 4px 4px 0px rgba(0,0,0,0.2);
        }
        
        .instructions {
            background: linear-gradient(135deg, #FFE66D 0%, #FFF9C4 100%);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            font-size: 28px;
            color: #2C3E50;
            font-weight: bold;
            margin: 25px 0;
            box-shadow: 0 10px 25px rgba(255, 230, 109, 0.3);
            border: 4px solid #FFB700;
        }
        
        .stButton>button {
            font-size: 24px;
            padding: 20px 40px;
            border-radius: 15px;
            border: none;
            font-weight: bold;
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
            transition: all 0.3s;
            letter-spacing: 1px;
        }
        
        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.3);
        }
        
        .stButton>button:active {
            transform: translateY(-1px);
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Comic Sans MS', cursive;
            font-weight: bold;
            color: #2C3E50;
        }
        
        .comparison-box {
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            font-weight: bold;
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
            margin: 15px 0;
        }
        
        .wrong-answer {
            background: linear-gradient(135deg, #FF9999 0%, #FFB3B3 100%);
            border: 4px solid #FF6B6B;
        }
        
        .correct-answer {
            background: linear-gradient(135deg, #95E1D3 0%, #4ECDC4 100%);
            border: 4px solid #2C3E50;
        }
    </style>
    
    <script>
        // Add some fun animations
        window.addEventListener('load', function() {
            document.querySelectorAll('.main-title').forEach(el => {
                el.style.animation = 'bounce 2s infinite';
            });
        });
    </script>
""", unsafe_allow_html=True)

# Title and welcome
st.markdown('<div class="main-title">🎨 Learn to Write Numbers! 🎮</div>',
            unsafe_allow_html=True)
st.markdown('<div class="subtitle">Draw what you see and let me check!</div>',
            unsafe_allow_html=True)

# Show stats
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        f'<div class="stats-box stats-correct">✅ Correct: <br>{st.session_state.correct_count}</div>', unsafe_allow_html=True)
with col2:
    st.markdown(
        f'<div class="stats-box stats-total">📊 Total: <br>{st.session_state.total_count}</div>', unsafe_allow_html=True)
with col3:
    if st.session_state.total_count > 0:
        accuracy = (st.session_state.correct_count /
                    st.session_state.total_count) * 100
        st.markdown(
            f'<div class="stats-box stats-score">⭐ Score: <br>{accuracy:.0f}%</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            f'<div class="stats-box stats-score">⭐ Score: <br>0%</div>', unsafe_allow_html=True)

# Show target number
st.markdown(
    f'<div class="target-number">{st.session_state.target_digit}</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="instructions">📝 Draw the number <b>{st.session_state.target_digit}</b> in the box below</div>', unsafe_allow_html=True)

st.markdown("---")

# Canvas with better styling
st.markdown('<div style="text-align: center; font-size: 24px; color: #FFE66D; font-weight: bold; margin: 20px 0;">✏️ Draw Here ✏️</div>', unsafe_allow_html=True)

canvas_result = st_canvas(
    fill_color="black",
    stroke_width=7,
    stroke_color="white",
    background_color="black",
    height=300,
    width=300,
    drawing_mode="freedraw",
    key=f"canvas_{st.session_state.canvas_key}"
)

st.markdown("")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_clicked = st.button(
        "✅ CHECK MY DRAWING! ✅", use_container_width=True, key="predict_btn")

if predict_clicked:
    st.session_state.show_result = True

if st.session_state.show_result:
    if canvas_result.image_data is not None:

        # Convert canvas to image
        img = Image.fromarray(
            canvas_result.image_data.astype("uint8")
        )

        img = img.convert("L")

        img_array = np.array(img)

        if np.max(img_array) == 0:
            st.warning("⚠️ Please draw a digit first!")

        else:

            # Find digit area
            coords = np.column_stack(
                np.where(img_array > 0)
            )

            y_min, x_min = coords.min(axis=0)
            y_max, x_max = coords.max(axis=0)

            digit = img_array[
                y_min:y_max+1,
                x_min:x_max+1
            ]

            # Resize keeping shape
            digit_img = Image.fromarray(digit)

            digit_img.thumbnail(
                (20, 20)
            )

            # Create 28x28 image
            final_img = Image.new(
                "L",
                (28, 28),
                0
            )

            x_offset = (28-digit_img.size[0])//2
            y_offset = (28-digit_img.size[1])//2

            final_img.paste(
                digit_img,
                (x_offset, y_offset)
            )

            final_array = np.array(final_img)

            # Normalize like training
            final_array = final_array.astype("float32") / 255.0

            # Predict
            try:
                prediction = model.predict(
                    final_array.reshape(1, 784)
                )

                # Get confidence scores
                if hasattr(model, 'predict_proba'):
                    probabilities = model.predict_proba(
                        final_array.reshape(1, 784))
                    confidence = np.max(probabilities) * 100
                else:
                    confidence = 75  # Default confidence if not available

                if prediction is None or len(prediction) == 0:
                    st.error("❌ Model returned invalid prediction")
                else:
                    predicted_digit = int(prediction[0])
                    st.session_state.predicted_digit = predicted_digit

                    st.markdown("---")

                    # Check confidence threshold
                    CONFIDENCE_THRESHOLD = 55  # Model must be at least 55% confident

                    if confidence < CONFIDENCE_THRESHOLD:
                        # Low confidence - ask to redraw
                        st.session_state.total_count += 1

                        st.markdown(f"""
                            <div style="background: linear-gradient(135deg, #FFB366 0%, #FFD699 100%); padding: 30px; border-radius: 20px; text-align: center; font-size: 28px; font-weight: bold; color: #2C3E50; border: 4px solid #FFA500;">
                                Hmm! 🤔 I'm only {confidence:.0f}% sure!<br><br>
                                Your drawing is a bit unclear.<br>
                                Let's try again with cleaner lines! 📝
                            </div>
                        """, unsafe_allow_html=True)

                        st.markdown("---")
                        st.markdown(
                            '<div style="text-align: center; font-size: 26px; color: #FFE66D; font-weight: bold;">Draw more carefully! You can do it! 💪</div>', unsafe_allow_html=True)

                        col_btn1, col_btn2 = st.columns(2)

                        with col_btn1:
                            if st.button("🔄 TRY AGAIN! 🔄", use_container_width=True, key="try_again_btn"):
                                st.session_state.show_result = False
                                st.session_state.predicted_digit = None
                                st.session_state.canvas_key += 1
                                st.rerun()

                        with col_btn2:
                            if st.button("⏭️ NEXT NUMBER! ⏭️", use_container_width=True, key="skip_btn"):
                                st.session_state.target_digit = random.randint(
                                    0, 9)
                                st.session_state.show_result = False
                                st.session_state.predicted_digit = None
                                st.session_state.canvas_key += 1
                                st.rerun()

                    # Check if prediction matches target
                    elif predicted_digit == st.session_state.target_digit:
                        # SUCCESS!
                        st.session_state.correct_count += 1
                        st.session_state.total_count += 1

                        st.markdown("""
                            <div class="good-job">
                                🎉 PERFECT! AMAZING JOB! 🎉<br><br>
                                You wrote the <b>{}</b> correctly! ⭐<br>
                                Confidence: {:.0f}%<br>
                                You're a SUPERSTAR! 🌟
                            </div>
                        """.format(st.session_state.target_digit, confidence), unsafe_allow_html=True)
                        st.balloons()

                        # Show next button
                        if st.button("🚀 LET'S LEARN A NEW NUMBER! 🚀", use_container_width=True, key="next_btn_correct"):
                            st.session_state.target_digit = random.randint(
                                0, 9)
                            st.session_state.show_result = False
                            st.session_state.predicted_digit = None
                            st.session_state.canvas_key += 1
                            st.rerun()

                    else:
                        # INCORRECT - Show only target, not prediction
                        st.session_state.total_count += 1

                        st.markdown("""
                            <div class="needs-practice">
                                Oops! That's not quite right! 😅<br><br>
                                I thought it was a {} ({:.0f}% sure)<br>
                                Let me show you the correct one! 👇
                            </div>
                        """.format(predicted_digit, confidence), unsafe_allow_html=True)

                        st.markdown(
                            '<div style="text-align: center; font-size: 26px; color: #95E1D3; font-weight: bold; margin: 30px 0;">✅ It should be:</div>', unsafe_allow_html=True)
                        st.markdown(
                            '<div style="text-align: center; font-size: 100px; font-weight: bold; color: #4ECDC4; margin: 20px 0;">{}</div>'.format(st.session_state.target_digit), unsafe_allow_html=True)

                        st.markdown("---")
                        st.markdown(
                            '<div style="text-align: center; font-size: 26px; color: #FFE66D; font-weight: bold;">Try drawing again! You can do it! 💪</div>', unsafe_allow_html=True)

                        col_btn1, col_btn2 = st.columns(2)

                        with col_btn1:
                            if st.button("🔄 TRY AGAIN! 🔄", use_container_width=True, key="try_again_btn"):
                                st.session_state.show_result = False
                                st.session_state.predicted_digit = None
                                st.session_state.canvas_key += 1
                                st.rerun()

                        with col_btn2:
                            if st.button("⏭️ NEXT NUMBER! ⏭️", use_container_width=True, key="skip_btn"):
                                st.session_state.target_digit = random.randint(
                                    0, 9)
                                st.session_state.show_result = False
                                st.session_state.predicted_digit = None
                                st.session_state.canvas_key += 1
                                st.rerun()

            except Exception as e:
                st.error(f"❌ Error during prediction: {str(e)}")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div style="text-align: center; font-size: 22px; color: #FFE66D; font-weight: bold;">🌟 Keep practicing! You\'re doing AWESOME! 🌟</div>', unsafe_allow_html=True)
