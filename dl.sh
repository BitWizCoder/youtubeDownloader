#!/bin/bash

echo "Enter Video URL"
read url
echo "Chose your option d = default - h = highest - db = default best- a = audio - pl = playlist"
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
	yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 --embed-thumbnail $url
else
	echo "None of the condition met"
fi
