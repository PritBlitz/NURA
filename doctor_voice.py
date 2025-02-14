from dotenv import load_dotenv
load_dotenv()
import os
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

import subprocess
import platform


from pydub import AudioSegment
import subprocess
import platform
import os
from elevenlabs import ElevenLabs

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    # Generate audio
    audio = client.generate(
        text=input_text,
        voice="Daniel",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    
    elevenlabs.save(audio, output_filepath)

    # Convert MP3 to WAV for Windows
    wav_filepath = output_filepath.replace(".mp3", ".wav")
    sound = AudioSegment.from_mp3(output_filepath)
    sound.export(wav_filepath, format="wav")

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows (Use WAV format)
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
