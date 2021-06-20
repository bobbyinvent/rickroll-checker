import youtube_dl

url = input("Enter a Youtube link: ")

ydl_opts = {
    "outtmpl": "%(id)s.%(ext)s",
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    video = ydl.extract_info(
        url, download=False
    )

video_title = video["title"]
video_description = video["description"]
video_content = video_title + video_description

phrases = [
    "rickroll",
    "rick roll",
    "rick astley",
    "never gonna give you up",
]

rickroll = False
for phrase in phrases:
    if phrase in video_content.lower():
        rickroll = True

if rickroll:
    print("RICKROLL DETECTED!")
else:
    print("No rickroll detected. Proceed with caution!")
    
