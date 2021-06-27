import sys
import time
import webbrowser
import youtube_dl

url = input("Enter a Youtube link: ").strip()

ydl_opts = {
    "outtmpl": "%(id)s.%(ext)s",
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    try:
        video = ydl.extract_info(url, download=False)
    except:
        print(
            "ERROR FOUND:"
            "\n*****************************************\n"
            "Invalid URL. Cannot retrieve Youtube video!\n"
            "*******************************************\n"
        )
        sys.exit()

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

print("\nANALYSIS COMPLETED:")
if rickroll:
    print(
        "**********************************\n"
        "RICKROLL DETECTED! DO NOT PROCEED!\n"
        "**********************************"
    )
else:
    print("No rickroll detected. Proceed with caution!")
    res = input("Continue opening the video? (y/n): ")
    if res.lower()=="y":
        for i in range(3, 0, -1):
            print(f"Opening your video in {i}...")
            time.sleep(1)
        webbrowser.open(url)
