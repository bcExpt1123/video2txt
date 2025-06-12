# 🎬 Video Speech Transcriber

A Python project that extracts speech from a video file and converts it to text using [MoviePy](https://zulko.github.io/moviepy/) and [SpeechRecognition](https://pypi.org/project/SpeechRecognition/).

## 🚀 Features

- Extracts audio from `.mp4` video files
- Transcribes speech using Google's Speech Recognition API
- Modular and clean codebase
- Uses Poetry for dependency management
- Automatically deletes temporary audio files after transcription

## 📦 Requirements

- Python 3.8+
- `ffmpeg` installed and available in your system PATH

## 🛠️ Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/bcExpt1123/video2txt.git
   cd video2txt
   ```

2. **Install dependencies using Poetry**

   ```bash
   poetry install
   ```

3. **Activate the virtual environment**

   ```bash
   poetry shell
   ```

4. **Run the script**

   Place your video file (e.g., `video.mp4`) in the project root and run:

   ```bash
   python video2txt/convert.py
   ```

## 📂 File Structure

```
video-speech-transcriber/
│
├── video2txt
│   └──convert.py          # Main script
├── pyproject.toml         # Poetry project configuration
├── README.md              # Project documentation
└── video.mp4              # (Example) video file for transcription
```

## 🧪 Example Output

```
Transcribing video...

The resultant text from video is:

Hello, and welcome to the video!
```

## 🧼 Notes

* Temporary audio files are automatically deleted after transcription.
* Accuracy depends on the video audio quality and background noise.
* You must be connected to the internet to use Google's free recognizer API.

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
