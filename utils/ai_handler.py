import os
import openai
import streamlit as st
from .prompt_templates import DAVID_PROMPT_TEMPLATE

class AIHandler:
    def __init__(self):
        try:
            # ננסה לטעון מ-secrets
            self.api_key = st.secrets["OPENAI_API_KEY"]
        except:
            # אם לא מצליח, נשתמש במשתני סביבה רגילים
            self.api_key = os.environ.get("OPENAI_API_KEY")
        
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
            print(f"Error generating AI response: {str(e)}")
            return "מצטער, נתקלתי בבעיה בעת יצירת התשובה. אנא נסה שוב." 