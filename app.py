import os
import json
from flask import Flask, request, jsonify, render_template
import yt_dlp
from tqdm import tqdm
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def progress_hook(tq):
    def inner(d):
        if d['status'] == 'downloading':
            if tq.total == 0:
                tq.total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            tq.update(d['downloaded_bytes'] - tq.n)
        elif d['status'] == 'finished':
            tq.close()
    return inner

def list_formats(url, download_type):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            all_formats = info_dict.get('formats', [])
            
            if download_type == '1':
                formats = [f for f in all_formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']
            elif download_type == '2':
                formats = [f for f in all_formats if f.get('vcodec') != 'none' and f.get('acodec') == 'none']
            else:
                formats = [f for f in all_formats if f.get('acodec') != 'none' and f.get('vcodec') != 'none']
            
            return formats
    except Exception as e:
        print("Error in list_formats:", e)
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_formats', methods=['POST'])
def get_formats():
    data = request.json
    url = data.get('url')
    download_type = data.get('download_type')

    if not url:
        return jsonify({"error": "No URL provided"})

    formats = list_formats(url, download_type)
    
    if not formats:
        return jsonify({"error": "No formats available or an error occurred"})

    return jsonify({"formats": formats})

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    format_id = data.get('format_id')

    if not url or not format_id:
        return jsonify({"error": "Missing URL or format"})

    output_path = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(output_path, exist_ok=True)

    with tqdm(unit="B", unit_scale=True, unit_divisor=1024, miniters=1, desc="Downloading") as tq:
        ydl_opts = {
            'format': format_id,
            'progress_hooks': [progress_hook(tq)],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info_dict)
                return jsonify({"filename": os.path.basename(filename)})
        except Exception as e:
            print("Download error:", e)
            return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
