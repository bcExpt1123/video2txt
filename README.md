# video2txt

Convert video to text using Python.

## Overview

**video2txt** is a Python-based tool that enables you to extract text from video files. This project automates the process of transcribing spoken content in videos, making it easier to generate subtitles, build searchable archives, or analyze video data.

## Features

- Extracts speech from video files and converts it to text
- Supports a variety of video formats (e.g., mp4, avi, mov)
- Batch processing of multiple videos
- Simple command-line interface
- Easy integration with other Python scripts

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/bcExpt1123/video2txt.git
   cd video2txt
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line

```bash
python video2txt.py --input <path_to_video> --output <path_to_text>
```

- `--input`: Path to the video file.
- `--output`: Path where the resulting text file will be saved.

#### Example

```bash
python video2txt.py --input sample.mp4 --output transcript.txt
```

### As a Python Module

```python
from video2txt import video_to_text

transcript = video_to_text("sample.mp4")
print(transcript)
```

## Requirements

- Python 3.7+
- ffmpeg (for audio extraction)
- Speech-to-text libraries such as SpeechRecognition or OpenAI Whisper (depending on implementation)

## How it Works

1. Extracts audio from the video using ffmpeg.
2. Processes the audio to recognize and transcribe speech.
3. Outputs the recognized text to a file or console.

## Contributing

Contributions are welcome! Please open issues and submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [ffmpeg](https://ffmpeg.org/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [OpenAI Whisper](https://github.com/openai/whisper) (optional)
