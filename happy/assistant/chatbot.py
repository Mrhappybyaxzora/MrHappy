from happy.env import Keys
from happy.logging import Logger
from happy.assistant.llm import OpenAILLM
from prompts.chatbot import prompt, prompt_required
from datetime import datetime

l = Logger(__file__)

class ChatModel:
    required = prompt_required
    def __init__(self, details: dict) -> None:
        try:
            self.system_prompt = prompt.format(**details)
        except Exception as e:
            l.error(e)

        self.llm = OpenAILLM(
            model = "gpt-3.5-turbo",
            temperature = 0.7,
            system_prompt = self.system_prompt,
            max_tokens = 4096,
            api_key="ssk-proj-yfGuiEPqlc6AYZhdEP25s8mUaM29MqEtoS9EHv0ZRFd7kIDPYptBNz82grjfvnHHJ3TF9mZg_0T3BlbkFJd9MuQfim_uuF3mOCNXCPDVilM6ig3zAbzqqsDADN_TAhY8pTCCHVyN4p1j4Nj9JJ_NV0oCgZ8A"
        )
    
    def dateTime(self) -> str:
        date_time_=f"Please use this realtime information if needed,\nCurrent date and time: {datetime.now()}"
        return date_time_

    def run(self, prompt: str, messages: list) -> str:
        self.llm.messages = [{"role": "system", "content": self.system_prompt}]+messages
        self.llm.add_message(self.llm.SYSTEM, self.dateTime())

        response = self.llm.run(prompt)
        
        return response
    
    
        
