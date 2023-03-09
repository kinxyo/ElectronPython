from pytube import YouTube
from pytube.cli import on_progress
import eel

eel.init('web')

@eel.expose
def showtitle(link):
    data = YouTube(link)
    return data.title

@eel.expose
def thumb(link):
    data = YouTube(link)
    return data.thumbnail_url

@eel.expose
def ytH(link):
    data = YouTube(link, on_progress_callback=on_progress)
    try:
        data.streams.filter(file_extension='mp4').get_highest_resolution().download()
        print("download successfully")
        return "File downloaded."
    except: 
        print("process went haywire.")
        return "Download Failed Successfully--"

@eel.expose
def ytP(link):
    data = YouTube(link, on_progress_callback=on_progress)
    try:
        data.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        print("download successfully")
        return "File downloaded."
    except: 
        print("process went haywire.")
        return "Download Failed Successfully--"

print("Initiated...\n")
eel.start('index.html', size=(856, 554))

# eel.start('index.html', size=(440, 340))
# Inner Width: 856
# Inner Height: 554
# Outer Width: 871
# Outer Height: 591