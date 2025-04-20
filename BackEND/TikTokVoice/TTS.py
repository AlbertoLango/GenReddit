#uses Github Repo for Tiktok Audio voices with the use of a funciton call we can use different populat tiktok voices
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent         
TTS_REPO  = BASE_DIR / "TikTok-Voice-TTS"           
if TTS_REPO.exists() and str(TTS_REPO) not in sys.path:
    sys.path.append(str(TTS_REPO))


from tiktok_voice import tts, Voice   

def generate_text (voice, inputText):
    tts(inputText, Voice.from_string(voice), "BackEND/TikTokVoice/TikTok-Voice-TTS/TTS_Script/output.mp3", play_sound=False)
    # arguments:
    #   - input text
    #   - voice which is used for the audio
    #   - output file name
    #   - play sound after generating the audio


selected_voice = 'US_MALE_3' # hardcoded for now 

with open('BackEND/TikTokVoice/TikTok-Voice-TTS/TTS_Script/Script.txt', "r") as file:
    content = file.readlines()
    generate_text( selected_voice, content[0])

