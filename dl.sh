#!/bin/bash


echo 'Enter Video URL or "-a links.txt"'
read url
echo "Chose your option d = default - h = highest - db = default best - v4 = 480p - a = audio - pl = playlist - pl-v4 = playlist_480p 1080 = 1080p"
read evaluator


if [ $evaluator == "d" ]
then
	yt-dlp -F $url
	echo "Enter Video resulation"
	read res
	yt-dlp -f $res $url

elif [ $evaluator == "h" ]
then
	yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 $url

elif [ $evaluator == "db" ]
then
	yt-dlp -f best $url
elif [ $evaluator == "pl" ]
then
	yt-dlp -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 $url
elif [ $evaluator == "a" ]
then
	yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 $url
elif [ $evaluator == "v4" ]
then
	# yt-dlp -f 'bestvideo[height<=480]+bestaudio/best[height<=480]' --merge-output-format mp4 $url
	yt-dlp -f 'bestvideo[height<=480]+bestaudio/best[height<=480]' --merge-output mp4 $url
elif [ $evaluator == "pl-v4" ]
then
	# yt-dlp -f 'bestvideo[height<=480]+bestaudio/best[height<=480]' --merge-output-format mp4 $url
	yt-dlp -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' -f 'bestvideo[height<=480]+bestaudio/best[height<=480]' --merge-output-format mp4 $url
elif [ $evaluator == "1080" ]
then
	yt-dlp -f 'bestvideo[height<=1080]+bestaudio/best[height<=480]' --merge-output-format mp4 $url
else
	echo "None of the condition met"
fi