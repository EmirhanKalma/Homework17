from openai import OpenAI

system_prompt = """Ты ассистент
"""

class Debate:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com")
        self.messages=[
            {"role": "system", "content": system_prompt},
        ]

    def send_messages(self, messages):
        response = self.client.chat.completions.create(
            model="deepseek-v4-flash", #ПОМЕНЯЙТЕ МОДЕЛЬ НА ФЛЕШ, ЧТОБЫ НЕ ТРАТИТЬ МНОГО ДЕНЕГ
            messages=messages,
            reasoning_effort="low",
            extra_body={"thinking": {"type": "disabled"}}
        )

        return response.choices[0].message.content

    def start_chat(self):
        while True:
            print("Это программа дебатов. ИИ будет во всем вам перечить.")
            user_prompt = input("Введите сообщение:")
            self.messages.append({"role": "user", "content": user_prompt})
            ai_message = self.send_messages(self.messages)
            print(f"Aristotle: {ai_message}")
    

game = Debate(api_key="sk-16b9156d93c7477e999f68424752866a")
game.start_chat()