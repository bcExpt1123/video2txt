from moviepy import VideoFileClip
import speech_recognition as sr
from pathlib import Path


def extract_audio_from_video(video_path: str, output_audio_path: str) -> None:
    """Extracts audio from video and saves it to a file."""
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path, logger=None)


def transcribe_audio(audio_path: str) -> str:
    """Transcribes audio file to text using Google's speech recognition API."""
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return "[Could not understand audio]"
    except sr.RequestError as e:
        return f"[Could not request results; {e}]"

def transcribe_video(video_path: str) -> str:
    """Extracts audio from a video and returns the transcribed text."""
    audio_path = Path("temp_audio.wav")
    extract_audio_from_video(video_path, str(audio_path))
    transcription = transcribe_audio(str(audio_path))
    audio_path.unlink(missing_ok=True)  # Cleanup temp file
    return transcription

def main():
    video_path = Path("video.mp4")
    audio_path = Path("sound.wav")

    if not video_path.exists():
        print(f"Video file not found: {video_path}")
        return

    print("Transcribing video...")
    transcription = transcribe_video(str(video_path))

    print("\nThe resultant text from video is:\n")
    print(transcription)


if __name__ == "__main__":
    main()
