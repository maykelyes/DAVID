import os
import openai
import streamlit as st
import logging
from .prompt_templates import DAVID_PROMPT_TEMPLATE

# הגדרת הלוגר
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class AIHandler:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_API_KEY")
        # ודא שמפתח ה־API מוגדר
        if not self.api_key:
            logger.error("OPENAI_API_KEY is not set in the environment!")
        openai.api_key = self.api_key
        
    def generate_response(self, user_question: str) -> str:
        try:
            prompt = DAVID_PROMPT_TEMPLATE.format(user_question=user_question)
            
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=150
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            # שימוש ב-logger.error להדפסת השגיאה עם כל הפרטים
            logger.error(f"Error generating AI response: {e}", exc_info=True)
            return "מצטער, נתקלתי בבעיה בעת יצירת התשובה. אנא נסה שוב." 