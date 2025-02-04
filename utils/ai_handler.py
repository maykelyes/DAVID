import os
import openai
from .prompt_templates import DAVID_PROMPT_TEMPLATE

class AIHandler:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        
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