import argparse
import os
import yt_dlp
import sys

def dl_video(url, format_c):
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    ydl_opts = {}

    if format_c == 'mp3':
        ydl_opts = {
            'nocheckcertificate': True,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        }
    elif format_c == 'mp4':
        ydl_opts = {
            'nocheckcertificate': True,
            'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4][vcodec^=avc1]/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Successfully downloaded to {downloads_path}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        if 'ffmpeg' in str(e).lower() and 'not found' in str(e).lower():
            print("Please ensure ffmpeg is installed and in your PATH.", file=sys.stderr)
            print("You can install it using Homebrew: brew install ffmpeg", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YouTube Downloader CLI')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--mp3', action='store_true', help='dl as MP3')
    group.add_argument('--mp4', action='store_true', help='dl as MP4')
    parser.add_argument('url', type=str, help='url of video')

    args = parser.parse_args()

    if args.mp3:
        dl_video(args.url, 'mp3')
    elif args.mp4:
        dl_video(args.url, 'mp4') 
