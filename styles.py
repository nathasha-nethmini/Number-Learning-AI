import streamlit as st

def load_custom_css(theme="🦄 Magic"):
    if theme == "🚀 Space":
        bg_anim = "linear-gradient(-45deg, #A9C9FF, #FFBBEC, #C3A6FF, #FFC4E1)" # Cosmic Pastel Nebula
        primary = "#9B5DE5" # Bright Cosmic Purple
        secondary = "#7B3FE4" # 3D Shadow Purple
        card_bg = "rgba(255, 255, 255, 0.85)" # Clear light card
        text_color = "#2C3E50" # Dark highly-visible text
        border_color = "#9B5DE5" # Purple borders
    elif theme == "🦖 Dino":
        bg_anim = "linear-gradient(-45deg, #FDFBF7, #F4F1DE, #E07A5F, #81B29A)"
        primary = "#81B29A"
        secondary = "#E07A5F"
        card_bg = "rgba(253, 251, 247, 0.9)"
        text_color = "#3D405B"
        border_color = "#E07A5F"
    else: # Magic
        bg_anim = "linear-gradient(-45deg, #FF9A9E, #FECFEF, #A18CD1, #FBC2EB)"
        primary = "#FF6B9D"
        secondary = "#9B5DE5"
        card_bg = "rgba(255, 255, 255, 0.85)"
        text_color = "#2C3E50"
        border_color = "#FF6B9D"

    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700;800&display=swap');

        /* FULLSCREEN IMMERSION: Hide Streamlit Padding & Margins */
        .block-container {{
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 1200px !important;
        }}
        
        header[data-testid="stHeader"], footer {{ display: none !important; }}
        
        .stApp {{
            background: {bg_anim} !important;
            background-size: 400% 400% !important;
            animation: gradientBG 15s ease infinite !important;
            font-family: 'Fredoka', 'Comic Sans MS', sans-serif !important;
            color: {text_color} !important;
        }}

        @keyframes gradientBG {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        /* HUD - HEADS UP DISPLAY */
        .hud-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: {card_bg};
            backdrop-filter: blur(15px);
            border: 4px solid {border_color};
            border-radius: 40px;
            padding: 10px 25px;
            margin-bottom: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            width: 100%;
        }}
        
        /* THEME SELECTOR IN HUD */
        div.row-widget.stRadio > div {{
            background: transparent !important;
            display: flex !important;
            gap: 15px !important;
        }}
        div.row-widget.stRadio p {{
            font-size: 18px !important;
            font-weight: 800 !important;
            color: {text_color} !important;
        }}
        
        /* SCORE IN HUD */
        .hud-score {{
            display: flex;
            gap: 20px;
            font-size: 20px;
            font-weight: 800;
            color: {text_color};
        }}
        .hud-score span {{
            background: rgba(0,0,0,0.05);
            padding: 5px 15px;
            border-radius: 20px;
            border: 2px solid {primary};
        }}

        /* THE GAME CONSOLE (Main Device) - Applied to Streamlit border container */
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background: {card_bg} !important;
            backdrop-filter: blur(20px) !important;
            border: 12px solid {border_color} !important;
            border-radius: 50px !important;
            padding: 30px !important;
            box-shadow: 
                inset 0 0 20px rgba(0,0,0,0.1),
                0 20px 50px rgba(0,0,0,0.3),
                0 0 0 8px rgba(255,255,255,0.4) !important;
            margin: 0 auto !important;
            max-width: 950px !important;
            text-align: center !important;
            position: relative !important;
        }}
        
        /* Console Speaker/Camera detail at the top */
        .game-console::before {{
            content: '';
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%);
            width: 120px;
            height: 12px;
            background: {border_color};
            border-bottom-left-radius: 15px;
            border-bottom-right-radius: 15px;
        }}

        /* THE MISSION SCREEN (Top part of console) */
        .mission-screen {{
            background: rgba(255,255,255,0.5);
            border: 4px dashed {primary};
            border-radius: 30px;
            padding: 15px;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 30px;
            box-shadow: inset 0 5px 15px rgba(0,0,0,0.05);
        }}
        .mission-title {{
            font-size: 24px;
            font-weight: 800;
            color: {text_color};
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}
        .mission-target {{
            font-size: 80px;
            font-weight: 900;
            color: {primary};
            line-height: 1;
            text-shadow: 3px 3px 0px rgba(0,0,0,0.1);
        }}
        .mission-emoji {{
            font-size: 40px;
            letter-spacing: -5px;
        }}

        /* PERFECT CANVAS BORDER & CENTERING */
        iframe[title="streamlit_drawable_canvas.st_canvas"] {{
            border: 8px solid {border_color};
            border-radius: 10px !important;
            max-width: 290px !important; 
            min-height: 325px;
            margin: auto !important;
            display: block !important;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.5) !important;
        }}

        /* RESULT CARDS (CONGRATS/FAIL BOXES) */
        .success-card {{
            background: {card_bg};
            backdrop-filter: blur(20px);
            border: 8px solid {primary};
            border-radius: 40px;
            padding: 40px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            text-align: center;
        }}

        .fail-card {{
            background: {card_bg};
            backdrop-filter: blur(20px);
            border: 8px solid #E74C3C;
            border-radius: 40px;
            padding: 40px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            text-align: center;
        }}

        /* CHUNKY 3D ARCADE BUTTONS */
        div.stButton > button, button[data-testid="baseButton-secondary"], button[data-testid="baseButton-primary"] {{
            border-radius: 20px !important;
            font-weight: 900 !important;
            font-size: 24px !important;
            padding: 15px 40px !important;
            text-transform: uppercase;
            letter-spacing: 2px;
            background: {primary} !important;
            color: white !important;
            border: none !important;
            /* 3D Drop Shadow Effect */
            box-shadow: 0 10px 0 {secondary}, 0 15px 20px rgba(0,0,0,0.2) !important;
            transition: all 0.1s ease !important;
            position: relative;
            top: 0;
            width: 100%;
        }}
        
        div.stButton > button:active, button[data-testid="baseButton-secondary"]:active, button[data-testid="baseButton-primary"]:active {{
            /* Press down effect */
            top: 10px;
            box-shadow: 0 0px 0 {secondary}, 0 5px 10px rgba(0,0,0,0.2) !important;
            background: {primary} !important;
        }}
        
        /* Cleaned up old border hiding rule */

    </style>
    """, unsafe_allow_html=True)