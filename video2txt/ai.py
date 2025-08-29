import whisper
from moviepy import VideoFileClip
from pathlib import Path
from video2txt.convert import extract_audio_from_video

if __name__ == "__main__":
    # Load model (choose "base", "small", "medium", or "large")
    model = whisper.load_model("base")

    video_path = Path(f"video.avi")
    audio_path = Path(f"sound.wav")

    extract_audio_from_video(video_path, audio_path)
    # Transcribe audio
    result = model.transcribe("sound.wav", language="en")
    print("Transcription:", result["text"])
    with open(f"trans.txt", "w") as file:
        file.write(result["text"])