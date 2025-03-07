from elevenlabs.client import ElevenLabs
from happy.logging import Logger
from happy.env import Keys
import re
import asyncio

l = Logger(__file__)
client = ElevenLabs(
  api_key=Keys["ELEVENLABS_API_KEY"], # Defaults to ELEVEN_API_KEY or ELEVENLABS_API_KEY
)

def remove_emojis(data: str) -> str:
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

def fetch_audio(text, AssistantVoice = "en-US-JennyNeural") -> bytes:
    text = remove_emojis(text)
    try:
        audio = client.generate(text=text, voice="pqHfZKP75CvOlQylNhV4")
        audio_bytes = b""
        for element in audio:
            audio_bytes += element
        return audio_bytes
    except Exception as e:
        l.error(e)
        return b""

async def TextToSpeechBytes(Text, AssistantVoice = "en-US-JennyNeural") -> bytes:
    return await asyncio.to_thread(fetch_audio, Text, AssistantVoice)




if __name__ == "__main__":
    from rich import print
    # response = client.voices.get_all()
    # audio = client.generate(text="Hello there!", voice="pqHfZKP75CvOlQylNhV4")
    # print([i for i in audio])
    # print(response.voices)
    print(fetch_audio("Hello there!", "pqHfZKP75CvOlQylNhV4"))
    

