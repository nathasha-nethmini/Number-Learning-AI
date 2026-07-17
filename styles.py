import streamlit as st

def load_custom_css(theme="🦄 Magic"):
    if theme == "🚀 Space":
        bg_anim = "linear-gradient(-45deg, #090a0f, #1b1b3a, #4a1c40, #0a192f)" # Deep Dark Space & Nebula
        primary = "#00D4FF" # Glowing Neon Cyan
        secondary = "#0088AA" # Deep Cyan Shadow
        card_bg = "rgba(15, 15, 35, 0.85)" # Dark Glassy Panel
        text_color = "#E0F7FA" # Ice White/Cyan text
        border_color = "#00D4FF" # Neon Cyan borders
    elif theme == "🦖 Dino":
        bg_anim = "linear-gradient(-45deg, #FDFBF7, #F4F1DE, #E07A5F, #81B29A)"
        primary = "#81B29A"
        secondary = "#E07A5F"
        card_bg = "rgba(253, 251, 247, 0.9)"
        text_color = "#3D405B"
        border_color = "#E07A5F"
    elif theme == "🌊 Ocean":
        bg_anim = "linear-gradient(-45deg, #4facfe, #00f2fe, #43e97b, #38f9d7)" # Vibrant underwater
        primary = "#00B4DB"
        secondary = "#0083B0"
        card_bg = "rgba(255, 255, 255, 0.85)"
        text_color = "#003A4D"
        border_color = "#00B4DB"
    else: # Magic
        bg_anim = "linear-gradient(-45deg, #FF9A9E, #FECFEF, #F6D365, #FDA085)" # Sunrise Magical Pastel
        primary = "#FF6384" # Vibrant Coral Pink
        secondary = "#D83A56" # Deep Red/Pink Shadow
        card_bg = "rgba(255, 255, 255, 0.9)" # Clear glassy card
        text_color = "#4A154B" # Deep Magical Purple for contrast
        border_color = "#FF6384" # Pink borders

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
        div[data-testid="stRadio"] {{
            background: {card_bg} !important;
            backdrop-filter: blur(15px);
            border-radius: 30px;
            padding: 10px 20px;
            margin-top: 10px;
            margin-bottom: 20px;
            border: 2px solid {border_color};
            box-shadow: 0 5px 15px rgba(0,0,0,0.15);
            display: flex;
            justify-content: center;
        }}
        div.row-widget.stRadio > div {{
            background: transparent !important;
            display: flex !important;
            gap: 15px !important;
            justify-content: center !important;
        }}
        div[data-testid="stRadio"] p, 
        div[data-testid="stRadio"] label, 
        div[data-testid="stRadio"] span {{
            font-size: 18px !important;
            font-weight: 800 !important;
            color: {text_color} !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
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
            padding: 5px;
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
        
        /* Mobile Responsiveness for HUD */
        @media (max-width: 600px) {{
            .hud-container {{
                flex-direction: column !important;
                gap: 10px !important;
                text-align: center !important;
                padding: 15px !important;
                border-radius: 25px !important;
            }}
            .hud-container h3 {{
                font-size: 20px !important;
                margin-right: 0 !important;
                text-align: center !important;
            }}
            .hud-score {{
                font-size: 16px !important;
                justify-content: center !important;
                flex-wrap: wrap !important;
            }}
            .mission-screen {{
                flex-direction: column !important;
                gap: 15px !important;
                text-align: center !important;
            }}
            div[data-testid="stRadio"] {{
                padding: 8px 10px !important;
            }}
            div[data-testid="stRadio"] p,
            div[data-testid="stRadio"] label,
            div[data-testid="stRadio"] span {{
                font-size: 12px !important;
            }}
            div.row-widget.stRadio > div {{
                gap: 5px !important;
            }}
        }}

    </style>
    """, unsafe_allow_html=True)