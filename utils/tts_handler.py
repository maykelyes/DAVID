import os
import time
import logging
import asyncio
import streamlit as st

# הגדרת הלוגר
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyht import AsyncClient
from pyht.client import TTSOptions, Language

class TTSHandler:
    def __init__(self):
        self.api_key = os.environ.get("PLAYHT_API_KEY")
        self.user_id = os.environ.get("PLAYHT_USER_ID")
        self.voice_id = os.environ.get("PLAYHT_VOICE_ID")
        
        logger.info(f"Initializing TTSHandler with voice_id: {self.voice_id}")
        
    async def generate_speech(self, text: str) -> bytes:
        try:
            if not text:
                logger.error("Empty text received")
                raise ValueError("Text cannot be empty")
            
            logger.info(f"Generating speech for text of length: {len(text)}")
            
            # אתחול הלקוח ללא הפרמטר base_url (גרסה 0.1.4 אינה תומכת בו)
            client = AsyncClient(user_id=self.user_id, api_key=self.api_key)
            # עדכון ידני של כתובת הבסיס לפי התיעוד
            client._base_url = "https://api.play.ht"
            
            # יש לוודא שהערך של voice מתחיל בכיתוב "s3://"
            voice = self.voice_id if self.voice_id.startswith("s3://") else f"s3://{self.voice_id}"

            # הגדרת האפשרויות להמרת טקסט לדיבור - חשוב לציין את השפה לעברית ואיכות גבוהה
            options = TTSOptions(
                voice=voice,
                sample_rate=48000,  # הגדרת איכות גבוהה
                speed=1.0,
                language=Language.HEBREW,
                quality="high",
                temperature=0.4,
                top_p=0.9,
                text_guidance=0.80,
                voice_guidance=1.40,   
                style_guidance=8.0,
                repetition_penalty=1.00
            )

            # בהתאם לתיעוד, לשימוש במודול 3.0-mini יש להגדיר את ה-voice_engine כ-"Play3.0-mini-http"
            voice_engine = "Play3.0-mini-http"
            
            logger.info("Starting audio generation via PlayHT AsyncClient (streaming)...")
            
            # הצטברות התוכן בזיכרון במקום כתיבה לקובץ זמני
            audio_data = bytearray()
            first_chunk = True
            # שימוש ב-async for לקבלת חלקי האודיו בצורה אסינכרונית
            async for chunk in client.tts(text, options, voice_engine=voice_engine):
                if first_chunk:
                    try:
                        # ננסה לדלות את תוכן החבילה כמחרוזת כדי לבדוק אם מדובר בהודעת שגיאה
                        chunk_str = chunk.decode("utf-8", errors="replace").strip()
                        if chunk_str.startswith("{") and '"detail"' in chunk_str:
                            logger.error("התקבלה הודעת שגיאה מה-API במקום נתוני אודיו: " + chunk_str)
                    except Exception as e:
                        logger.error("שגיאה בעת בדיקת תוכן החבילה הראשונה", exc_info=True)
                    first_chunk = False
                logger.info(f"Received chunk of size: {len(chunk)} bytes")
                audio_data.extend(chunk)
                
            logger.info(f"Audio data received, total size: {len(audio_data)} bytes")
            return bytes(audio_data)
            
        except Exception as e:
            logger.error(f"Error in TTS process: {str(e)}", exc_info=True)
            return None