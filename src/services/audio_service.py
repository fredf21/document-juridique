from gtts import gTTS
from io import BytesIO

def generate_audio_bytes(text: str) -> BytesIO:
    """
    Converts text to speech bytes using gTTS.
    
    Args:
        text (str): The text to convert to speech.
        
    Returns:
        BytesIO: A buffer containing the audio data.
    """
    if not text:
        return None
        
    try:
        tts = gTTS(text=text, lang='fr')
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None
