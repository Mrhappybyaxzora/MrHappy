import os, sys

sys.path.append(os.getcwd())

from pyht import Client
from pyht.client import TTSOptions, Format
from happy.env import Keys
import asyncio
import re



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



client = Client(
    user_id=Keys["PLAY_HT_USER_ID"],
    api_key=Keys["PLAY_HT_API_KEY"],
)
def fetch_audio(text, voice="s3://voice-cloning-zero-shot/7c339a9d-370f-4643-adf5-4134e3ec9886/mlae02/manifest.json"):
    options = TTSOptions(voice="s3://voice-cloning-zero-shot/7c339a9d-370f-4643-adf5-4134e3ec9886/mlae02/manifest.json", format=Format.FORMAT_MP3)
    b_ = b""
    for chunk in client.tts(text, options):
        b_+=chunk
    return b_

async def TextToSpeechBytes(Text, AssistantVoice = "en-US-JennyNeural") -> bytes:
    Text = str(Text)
    return await asyncio.to_thread(fetch_audio, Text, AssistantVoice)