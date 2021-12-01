# Youtube Downloader using yt-dlp combined with bash for easier use.

### Requerments
- [Gitbash](https://git-scm.com/downloads)
  
  Download and install gitbash and if you want you can use it with Cmdr or just use it as its own.
- [Python](https://www.python.org/downloads/)
  
  Download and install python for your os.

- [yt-dlp](https://github.com/yt-dlp/yt-dlp#installation)
  
  for installing yt-dlp run ```python -m pip install -U yt-dlp``` on your terminal.

- [ffmpeg](https://ffmpeg.org/download.html)
  
  Download and install a full version of FFmpeg and move the extracted folder into your c drive and put the bin folder to your systems path.


### Installation
- Clone the repo and put the ```dl.sh``` file into ```C:\Program Files\Git\usr\bin```


### Usage
- Now open your terminal and run ```dl.sh``` it will ask you for the link. you can provide a channel, playlist, and single video link.
- Then you will be asked to choose the resolution for the video, choose one, and hit enter. the video will be downloaded immediately.
- 
### Options for dowloading videos (Resulations)
- d = default -> Defult options from youtube-dl
- h = highest -> This will find and dowload the best resulation format available.
- db = default best -> 720p for most cases.
- v4 = 480p -> for 480p video and best available audio.
- a = audio -> as the options says for getting audio
- pl = playlist -> will add numeric naming also will get best available video.
