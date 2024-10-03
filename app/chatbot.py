from openai import OpenAI
import logging
from datetime import datetime
from constant import OPENAI_API_KEY, SUMMARIZATION_PROMPT

# Configure logging
logging.basicConfig(level=logging.ERROR)


class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_summerization(self, user_query: str, list_of_reviews: list[str]) -> str:
        try:
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            model = "gpt-4o-mini"
            response = self.client.chat.completions.create(
                model= model,
                messages=[
                    {"role": "system", "content": SUMMARIZATION_PROMPT.format(query=user_query, reviews=list_of_reviews, timestamp=date_time)}
                ]
            )
            generated_summary = response.choices[0].message.content
            return generated_summary
        except Exception as e:
            logging.error({
                "function": "generate_summerization",
                "data": str(e)
            })
            raise e