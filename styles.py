import streamlit as st

def load_custom_css(theme="🦄 Magic"):
    if theme == "🚀 Space":
        bg_anim = "linear-gradient(-45deg, #0B0C10, #1F2833, #111B24, #1B263B)"
        primary = "#66FCF1"
        secondary = "#45A29E"
        card_bg = "rgba(11, 12, 16, 0.65)"
        text_color = "#FFFFFF"
        border_color = "rgba(102, 252, 241, 0.3)"
    elif theme == "🦖 Dino":
        bg_anim = "linear-gradient(-45deg, #FDFBF7, #F4F1DE, #E07A5F, #81B29A)"
        primary = "#81B29A"
        secondary = "#F2CC8F"
        card_bg = "rgba(253, 251, 247, 0.65)"
        text_color = "#3D405B"
        border_color = "rgba(129, 178, 154, 0.4)"
    else: # Magic
        bg_anim = "linear-gradient(-45deg, #FF9A9E, #FECFEF, #A18CD1, #FBC2EB)"
        primary = "#FF6B9D"
        secondary = "#4ECDC4"
        card_bg = "rgba(255, 255, 255, 0.5)"
        text_color = "#2C3E50"
        border_color = "rgba(255, 255, 255, 0.5)"

    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap');

        /* ANIMATED BACKGROUND */
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

        /* HIDE STREAMLIT HEADER AND FOOTER */
        header[data-testid="stHeader"] {{ display: none !important; }}
        footer {{ display: none !important; }}

        /* GLASSMORPHISM CARDS */
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background: {card_bg} !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 2px solid {border_color} !important;
            border-radius: 30px !important;
            padding: 24px !important;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15) !important;
            text-align: center !important;
            color: {text_color} !important;
        }}

        /* Ensure text in cards inherits color */
        div[data-testid="stVerticalBlockBorderWrapper"] p, 
        div[data-testid="stVerticalBlockBorderWrapper"] h1, 
        div[data-testid="stVerticalBlockBorderWrapper"] h2 {{
            color: {text_color} !important;
        }}

        /* MAGICAL BANNER */
        .title-banner-compact {{
            background: {card_bg};
            backdrop-filter: blur(10px);
            border: 2px solid {border_color};
            padding: 20px;
            border-radius: 30px;
            text-align: center;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            margin-bottom: 20px;
        }}
        
        .title-banner-compact h2 {{
            font-size: 38px !important;
            font-weight: 700 !important;
            color: {text_color} !important;
            margin: 0 !important;
            text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
            font-family: 'Fredoka', sans-serif !important;
        }}

        /* COMPACT SCOREBOARD - GLASS */
        .score-board-compact {{
            background: {card_bg};
            backdrop-filter: blur(8px);
            border: 2px solid {border_color};
            border-radius: 20px;
            padding: 12px 15px;
            font-size: 20px;
            font-weight: 700;
            color: {text_color};
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 12px;
            font-family: 'Fredoka', sans-serif !important;
        }}

        /* TARGET BOX - GLASS CIRCLE */
        .target-box-compact {{
            background: {card_bg};
            backdrop-filter: blur(8px);
            border: 4px dashed {primary};
            border-radius: 50%;
            width: 120px;
            height: 120px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 10px auto;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        }}
        
        .target-num-compact {{
            font-size: 72px !important;
            font-weight: 700;
            color: {primary};
            line-height: 1;
            margin: 0;
            font-family: 'Fredoka', sans-serif !important;
        }}

        .object-label-compact {{
            font-size: 26px !important;
            color: {text_color};
            font-weight: 700;
            text-align: center;
            font-family: 'Fredoka', sans-serif !important;
        }}

        .object-display-compact {{
            font-size: 38px;
            letter-spacing: 5px;
            margin: 15px 0;
            text-align: center;
            white-space: normal;
            word-wrap: break-word;
        }}

        /* THEME SELECTOR GLASS PILL */
        .theme-selector-wrapper {{
            background: {card_bg};
            backdrop-filter: blur(10px);
            border: 2px solid {border_color};
            border-radius: 40px;
            padding: 8px 15px;
            margin: 0 auto 20px auto;
            max-width: 450px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
            display: flex;
            justify-content: center;
        }}
        
        div.row-widget.stRadio p {{
            font-size: 18px !important;
            font-weight: 700 !important;
            color: {text_color} !important;
            padding-right: 15px !important;
        }}
        
        /* PREMIUM BUTTONS */
        div.stButton > button, button[data-testid="baseButton-secondary"], button[data-testid="baseButton-primary"] {{
            border-radius: 30px !important;
            font-weight: 700 !important;
            font-size: 20px !important;
            padding: 12px 30px !important;
            transition: all 0.3s ease !important;
            background: linear-gradient(135deg, {primary}, {secondary}) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15) !important;
        }}
        
        div.stButton > button:hover, button[data-testid="baseButton-secondary"]:hover, button[data-testid="baseButton-primary"]:hover {{
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 12px 25px rgba(0, 0, 0, 0.25) !important;
            filter: brightness(1.1);
        }}

        /* SUCCESS & FAIL CARDS - GLASS */
        .success-card, .fail-card {{
            background: {card_bg};
            backdrop-filter: blur(12px);
            border: 2px solid {border_color};
            padding: 30px;
            border-radius: 30px;
            text-align: center;
            color: {text_color};
            box-shadow: 0 10px 30px rgba(31, 38, 135, 0.2);
            margin-bottom: 20px;
        }}

    </style>
    """, unsafe_allow_html=True)