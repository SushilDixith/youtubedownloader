# YouTube Video Downloader Web App

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Setup Instructions

1. Clone the repository or create a new directory for the project

2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install flask yt-dlp tqdm
```

4. Project Structure:
```
youtube_downloader/
│
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Web interface HTML
└── downloads/          # Directory for downloaded files
```

5. Save the HTML file as `templates/index.html`
6. Save the Python Flask script as `app.py`

7. Run the application:
```bash
python app.py
```

8. Open a web browser and navigate to `http://localhost:5000`

## Usage
1. Enter a YouTube video URL
2. Select download type (Audio Only, Video Only, or Audio and Video)
3. Click "Get Formats" to see available formats
4. Select a format and click "Download"

## Notes
- Downloads will be saved in the `downloads` directory
- Ensure you have the necessary rights and permissions when downloading videos

## Dependencies
- Flask
- yt-dlp
- tqdm
