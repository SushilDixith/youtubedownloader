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

## License
[Your Preferred License]
```

To run this application:

1. Create a new directory for your project
2. Create a `templates` subdirectory
3. Save the HTML file as `templates/index.html`
4. Save the Python Flask script as `app.py`
5. Save the README as `README.md`
6. Install the required dependencies with `pip install flask yt-dlp tqdm`
7. Run the application with `python app.py`
8. Open a web browser and go to `http://localhost:5000`

A few important notes:
- The app creates a `downloads` directory in the current working directory to save downloaded files
- The interface allows you to select download type and specific formats
- Error handling is included for various scenarios
- The app uses Tailwind CSS for styling via CDN
- The backend uses Flask to handle format listing and downloading

Would you like me to explain any part of the implementation or help you set up the application?