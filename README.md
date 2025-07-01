# cli-yt-downloader
Lightweight YouTube downloader for macOS. (Works on any OS, just different steps for the venv/ffmpeg)

**Requirements**
1. Homebrew
2. Python 

**How to set up**
1. Run `git clone https://github.com/echo1097/cli-yt-downloader`
2. Make a Python Virtual Environment `python3 -m venv venv` then `source venv/bin/activate` (Not required but highly recommended)
3. Run `pip install -r requirements.txt`
4. Run `brew install ffmpeg` (Required)

**Usage**
Run `python3 main.py --mp4/--mp3 video_url` 
Example: `python3 main.py --mp4 https://www.youtube.com/watch?v=dQw4w9WgXcQ`

This will output the MP4/MP3 into your downloads folder. The script automatically cleans up temporary files. 

# To-Do

Gui
