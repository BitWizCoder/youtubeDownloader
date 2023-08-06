import yt_dlp

def download_playlist(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_with_resolution(url, resolution):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_playlist_with_resolution(url, resolution):
    ydl_opts = {
        'outtmpl': '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    print("Enter Video URL or \"-a links.txt\"")
    url = input()

    print("Choose your option: d = default, h = highest, db = default best, v4 = 480p, a = audio, pl = playlist, pl-v4 = playlist_480p, 1080 = 1080p")
    evaluator = input()

    if evaluator == "d":
        download_playlist(url)
    elif evaluator == "h":
        download_with_resolution(url, 1080)
    elif evaluator == "db":
        download_with_resolution(url, 720)
    elif evaluator == "pl":
        download_playlist_with_resolution(url, 1080)
    elif evaluator == "a":
        download_audio(url)
    elif evaluator == "v4":
        download_with_resolution(url, 480)
    elif evaluator == "pl-v4":
        download_playlist_with_resolution(url, 480)
    elif evaluator == "1080":
        download_with_resolution(url, 1080)
    else:
        print("None of the conditions met")
