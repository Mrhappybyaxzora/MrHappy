from happy.env import Keys
from groq import Groq
from happy.logging import Logger

l = Logger(__file__)

def Content(Topic) -> str:
    client = Groq(api_key=Keys["Groq"])
    def ContentWriterAI(prompt):
        SystemChatBot = [{"role": "system","content": f"Hello, You're a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems etc."}]
        messages = []
        messages.append({"role": "user", "content": f"{prompt}"})
        completion = client.chat.completions.create(
        model = "mixtral-8x7b-32768",
        messages = SystemChatBot + messages,
        max_tokens=2048,
        temperature=0.7,
        top_p=1,
        stream=True,
        stop=None)

        Answer =""
        for chunk in completion:
                if chunk.choices[0].delta.content:
                    Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")
        return Answer
    try:
        ContentByAI = ContentWriterAI(Topic)
    except Exception as e:
        l.error(e)
        return "Something went wrong. Please try again later."
    return ContentByAI