from flask import Flask, render_template, request, jsonify, send_file, url_for
import yt_dlp
import os
from pathlib import Path

app = Flask(__name__)

# Create a directory to store downloaded files
DOWNLOADS_DIR = "downloads"
Path(DOWNLOADS_DIR).mkdir(parents=True, exist_ok=True)

# Format options for different downloads
FORMAT_OPTIONS = {
    "mp3": "bestaudio",
    "3gp": "18",   # 3GP format (low quality)
    "360p": "18",  # 360p
    "480p": "135", # 480p
    "720p": "22"   # 720p
}

@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    video_url = data.get('url')
    format_choice = data.get('format')
    
    if not video_url or not format_choice:
        return jsonify({'success': False, 'message': 'Invalid input'}), 400
    
    format_code = FORMAT_OPTIONS.get(format_choice)
    
    try:
        # Define options for yt-dlp
        ydl_opts = {
            'format': format_code,
            'outtmpl': os.path.join(DOWNLOADS_DIR, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }
        
        # If user selects mp3, use ffmpeg to convert the audio
        if format_choice == "mp3":
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
            ydl_opts['outtmpl'] = os.path.join(DOWNLOADS_DIR, '%(title)s.%(ext)s')

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            file_path = ydl.prepare_filename(info)
            
            # If the format is mp3, the file extension will be .mp3 after postprocessing
            if format_choice == "mp3":
                file_path = file_path.rsplit('.', 1)[0] + ".mp3"

        return jsonify({'success': True, 'fileUrl': url_for('download_file', filename=os.path.basename(file_path))})
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/downloaded/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(os.path.join(DOWNLOADS_DIR, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
