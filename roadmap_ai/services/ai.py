import os

import openai

from roadmap_ai.settings import get_settings


class OpenAIService:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = get_settings().openai_api_key
        self.client = openai.OpenAI()

    def get_roadmap(self, skill: str):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                { "role": "user", "content": f"Identify the main points necessary for learning {skill} in less than 200 characters" },
                # { "role": "user", "content": "Well, now separate it into chronologically organized descriptions"},
                # { "role": "user", "content": """Now for each topic, create the following parts:
                #     - Title
                #     - Description of the topic and objectives
                #     - Online material
                #     - Book"""
                # }
            ]
        )

        return completion.choices[0].message.content
