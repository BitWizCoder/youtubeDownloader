import subprocess

print("Enter Video URL or \"-a links.txt\"")
url = input()

print("Choose your option: d = default, h = highest, db = default best, v4 = 480p, a = audio, pl = playlist, pl-v4 = playlist_480p, 1080 = 1080p")
evaluator = input()

if evaluator == "d":
    subprocess.run(f"yt-dlp -F {url}", shell=True)
    print("Enter Video resolution")
    res = input()
    subprocess.run(f"yt-dlp -f {res} {url}", shell=True)

elif evaluator == "h":
    subprocess.run(f"yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {url}", shell=True)

elif evaluator == "db":
    subprocess.run(f"yt-dlp -f best {url}", shell=True)

elif evaluator == "pl":
    subprocess.run(f"yt-dlp -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {url}", shell=True)

elif evaluator == "a":
    subprocess.run(f"yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 {url}", shell=True)

elif evaluator == "v4":
    subprocess.run(f'yt-dlp -f "bestvideo[height<=480]+bestaudio/best[height<=480]" --merge-output mp4 {url}', shell=True)

elif evaluator == "pl-v4":
    subprocess.run(f'yt-dlp -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" -f "bestvideo[height<=480]+bestaudio/best[height<=480]" --merge-output-format mp4 {url}', shell=True)

elif evaluator == "1080":
    subprocess.run(f'yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=480]" --merge-output-format mp4 "{url}"', shell=True)

else:
    print("None of the conditions met")
