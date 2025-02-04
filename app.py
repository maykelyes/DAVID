import streamlit as st
from dotenv import load_dotenv
import asyncio
from utils.ai_handler import AIHandler
from utils.tts_handler import TTSHandler
import logging
import openai

# הגדרת הלוגר
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# טעינת משתני הסביבה
openai.api_key = st.secrets["OPENAI_API_KEY"]

# הוספת CSS ליישור כל הטקסטים לימין (RTL)
st.markdown(
    """
    <style>
        /* משנה את כיוון הטקסט לכל גוף הדף */
        body {
            direction: rtl;
        }
        /* מיישר את כל הטקסטים (כותרות, פסקאות וכו') לימין */
        .stMarkdown, .stText, .stTitle, .stHeader, h1, h2, h3, h4, h5, h6 {
            text-align: right;
        }
        /* יישור תוכן בסיידבר */
        .css-1d391kg { 
            direction: rtl;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# הגדרת הכותרת והתיאור
st.title("השראות מדוד גלפרין🎯")
st.markdown("""
מערכת המאפשרת לקבל תשובות מעוררות השראה מדוד גלפרין, יו"ר ובעלים של קבוצת גיל גרופ.
שאל כל שאלה וקבל תשובה מעוררת השראה בקולו של דוד!
""")

# יצירת מופעים של המחלקות
ai_handler = AIHandler()
tts_handler = TTSHandler()

# שדה קלט לשאלת המשתמש
user_question = st.text_input("מה תרצה לשאול את דוד?", key="user_question")

if st.button("שאל את דוד"):
    if user_question:
        with st.spinner('מעבד את השאלה...'):
            ai_response = ai_handler.generate_response(user_question)
            st.markdown(f"**תשובה:**\n\n{ai_response}")
            
            with st.spinner('ממיר את התשובה לאודיו... (עשוי לקחת מספר שניות)'):
                # כעת הפונקציה מחזירה את האודיו כ-bytes
                audio_bytes = asyncio.run(tts_handler.generate_speech(ai_response))
                logger.info(f"Received audio data of size: {len(audio_bytes) if audio_bytes else 0} bytes")
                
                if audio_bytes:
                    try:
                        st.audio(audio_bytes, format='audio/mp3', start_time=0)
                        logger.info("Audio playback widget created")
                    except Exception as e:
                        logger.error(f"Error during audio playback: {str(e)}", exc_info=True)
                        st.error(f"שגיאה בהצגת האודיו: {str(e)}")
                else:
                    logger.error("Audio data is invalid or empty")
                    st.error("מצטער, נתקלתי בבעיה בהמרת הטקסט לדיבור.")
    else:
        st.warning("אנא הכנס שאלה כדי להמשיך.") 