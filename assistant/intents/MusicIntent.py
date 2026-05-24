import yt_dlp
import webbrowser
from intentClassifier import classify
import keyboard
import pygetwindow as gw
import asyncio
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

async def _get_status():
    sessions = await MediaManager.request_async()
    current = sessions.get_current_session()
    if current:
        status = current.get_playback_info().playback_status
        return status
    return None

def is_playing() -> bool:
    status = asyncio.run(_get_status())
    
    return "playing" if status == 4 else "paused" if status == 5 else "none"

def play(query: str):
    options = {"quiet": True, "extract_flat": True}
    with yt_dlp.YoutubeDL(options) as ydl:
        results = ydl.extract_info(f"ytsearch1:{query}", download=False)
        video = results["entries"][0]
        url = f"https://www.youtube.com/watch?v={video['id']}"
        webbrowser.open(url)


def play_pause():
    keyboard.send("play/pause media")

def skip_track():
    keyboard.send("next track")

def previous_track():
    keyboard.send("previous track")

def mute():
    keyboard.send("volume mute")
def unmute():
    keyboard.send("volume unmute")


def loop():
    # find the youtube window and focus it
    windows = gw.getWindowsWithTitle("YouTube")
    if windows:
        windows[0].activate()
        keyboard.send("l")

def handle(user_input: str, intent_group: dict):
    intent_name = classify(user_input, intent_group)

    if intent_name == "play":
        if is_playing() == "paused":
            play_pause()
        else:           
            play(user_input)
    elif intent_name == "stop":
        if is_playing() == "playing":
            play_pause()
    elif intent_name == "mute":
        mute()
    elif intent_name == "unmute":
        unmute()
    elif intent_name == "resume":
        if is_playing() == "paused":
            play_pause()
    elif intent_name == "skip":
        skip_track()
    elif intent_name == "previous":
        previous_track()
    elif intent_name == "loop":
        loop()
    else:
        print("Sorry, I didn't understand the command.")

