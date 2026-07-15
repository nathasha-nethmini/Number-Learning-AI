import streamlit as st

def load_custom_css(theme="🦄 Magic"):
    if theme == "🚀 Space":
        css_vars = """
            --bg-app: #0B0C10;            
            --bg-card: #1F2833;           
            --primary-accent: #66FCF1;      
            --secondary-accent: #45A29E;    
            --highlight: #C5C6C7;         
            --soft-bg: #111B24;      
            --score-bg: #FFC300;         
            --text-color: #FFFFFF;
            --text-dark: #C5C6C7;
            --card-border: #45A29E;
            --success-bg1: #112A2A;
            --success-bg2: #163832;
            --success-border: #45A29E;
            --success-text: #66FCF1;
            --fail-bg1: #3A1C1C;
            --fail-bg2: #4A2020;
            --fail-border: #E74C3C;
            --fail-text: #FF6B6B;
            --score-text: #1F2833;
            --score-border: #FFC300;
        """
    elif theme == "🦖 Dino":
        css_vars = """
            --bg-app: #F4F1DE;            
            --bg-card: #FFFFFF;           
            --primary-accent: #81B29A;      
            --secondary-accent: #A8D5BA;    
            --highlight: #E07A5F;         
            --soft-bg: #F2E8CF;      
            --score-bg: #F2CC8F;         
            --text-color: #3D405B;
            --text-dark: #3D405B;
            --card-border: #81B29A;
            --success-bg1: #E8F8F5;
            --success-bg2: #A2E8DD;
            --success-border: #1ABC9C;
            --success-text: #117864;
            --fail-bg1: #FFECEC;
            --fail-bg2: #FFC4C4;
            --fail-border: #E74C3C;
            --fail-text: #922B21;
            --score-text: #3D405B;
            --score-border: #E07A5F;
        """
    else: # Magic
        css_vars = """
            --bg-app: #FFFDF4;            
            --bg-card: #FFFFFF;           
            --primary-accent: #FF6B9D;      
            --secondary-accent: #FF8EAF;    
            --highlight: #4ECDC4;         
            --soft-bg: #EDF9F8;      
            --score-bg: #FFE66D;         
            --text-color: #2C3E50;
            --text-dark: #2C3E50;
            --card-border: #FFEBEF;
            --success-bg1: #E8F8F5;
            --success-bg2: #A2E8DD;
            --success-border: #1ABC9C;
            --success-text: #117864;
            --fail-bg1: #FFECEC;
            --fail-bg2: #FFC4C4;
            --fail-border: #E74C3C;
            --fail-text: #922B21;
            --score-text: #7D6B00;
            --score-border: #F4D03F;
        """

    st.markdown(f"""
    <style>
        :root {{
            {css_vars}
            --font-family: 'Comic Sans MS', 'Chalkboard SE', 'Open Sans', sans-serif;
        }}

        .stApp {{
            background-color: var(--bg-app);
            font-family: var(--font-family);
            color: var(--text-color);
        }}
        
        /* Modern Rounded Kids Card Containers */
        .kids-card {{
            background-color: var(--bg-card);
            padding: 26px;
            border-radius: 28px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.06);
            border: 3px solid var(--card-border);
            text-align: center;
            margin-bottom: 20px;
            color: var(--text-color);
        }}
        
        /* Playful Header Banner Gradient */
        .title-banner {{
            background: linear-gradient(135deg, var(--primary-accent), var(--secondary-accent));
            padding: 32px 20px;
            border-radius: 32px;
            color: white;
            text-align: center;
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
            margin-bottom: 32px;
        }}
        
        .title-banner h1 {{
            font-size: 46px !important;
            font-weight: 900 !important;
            color: white !important;
            margin: 0 !important;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.12);
        }}
        
        .title-banner p {{
            font-size: 20px;
            margin: 12px 0 0 0;
            opacity: 0.95;
            font-weight: bold;
        }}
        
        /* Large Target Box Display */
        .target-box {{
            background-color: var(--soft-bg);
            border: 4px dashed var(--highlight);
            border-radius: 24px;
            padding: 15px;
            margin: 15px 0;
        }}
        
        .target-num {{
            font-size: 140px !important;
            font-weight: 900;
            color: var(--highlight);
            line-height: 1;
            margin: 0;
        }}
        
        .object-display {{
            font-size: 58px;
            letter-spacing: 6px;
            margin: 18px 0;
        }}
        
        .object-label {{
            font-size: 30px !important;
            color: var(--text-dark);
            font-weight: 800;
            margin-bottom: 5px;
        }}
        
        /* Bright Yellow Kids Scoreboard */
        .score-board {{
            background-color: var(--score-bg);
            border: 3px solid var(--score-border);
            border-radius: 22px;
            padding: 16px;
            font-size: 20px;
            font-weight: 900;
            color: var(--score-text);
            text-align: center;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        }}
        
        /* High-contrast Success/Fail Cards */
        .success-card {{
            background: linear-gradient(135deg, var(--success-bg1), var(--success-bg2));
            border: 3px solid var(--success-border);
            padding: 30px;
            border-radius: 26px;
            text-align: center;
            color: var(--success-text);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        }}
        
        .fail-card {{
            background: linear-gradient(135deg, var(--fail-bg1), var(--fail-bg2));
            border: 3px solid var(--fail-border);
            padding: 30px;
            border-radius: 26px;
            text-align: center;
            color: var(--fail-text);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        }}
        
        /* Rounded buttons adjustments & animations */
        div.stButton > button, button[data-testid="baseButton-secondary"], button[data-testid="baseButton-primary"] {{
            border-radius: 24px !important;
            font-weight: 900 !important;
            font-size: 18px !important;
            padding: 12px 28px !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            background-color: var(--primary-accent) !important;
            color: white !important;
            border: none !important;
        }}
        
        div.stButton > button:hover, button[data-testid="baseButton-secondary"]:hover, button[data-testid="baseButton-primary"]:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            background-color: var(--secondary-accent) !important;
            color: white !important;
        }}
        
        /* Ensure metrics have high-contrast text */
        div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"], [data-testid="stMetricValue"] > div {{
            color: var(--text-color) !important;
        }}
        
        /* Specific animation for primary button */
        button[data-testid="baseButton-primary"] {{
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0% {{
                transform: scale(1);
            }}
            50% {{
                transform: scale(1.03);
            }}
            100% {{
                transform: scale(1);
            }}
        }}
        
    </style>
    """, unsafe_allow_html=True)