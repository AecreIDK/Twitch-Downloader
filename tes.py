import yt_dlp

def download_twitch_video(url):
    ydl_opts = {
        'format': 'best',  # Downloads the best available quality
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("Done")  # Print message after download completes

# Example Twitch video URL
twitch_url = 'https://www.twitch.tv/videos/YOUR_VIDEO_ID'
download_twitch_video(twitch_url)
