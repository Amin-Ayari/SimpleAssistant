import yt_dlp
import webbrowser
from intentClassifier import classify
import keyboard
import pygetwindow as gw
import asyncio
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from pycaw.pycaw import AudioUtilities




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
    windows = gw.getWindowsWithTitle("YouTube")
    if windows:
        windows[0].activate()
        keyboard.send("play/pause media")

def skip_track():
    keyboard.send("next track")

def previous_track():
    keyboard.send("previous track")

def mute():
    keyboard.send("volume mute")

def is_muted():

    device = AudioUtilities.GetSpeakers()
    volume = device.EndpointVolume
    return volume.GetMute() == 1



def loop():
    # find the youtube window and focus it
    windows = gw.getWindowsWithTitle("YouTube")
    if windows:
        windows[0].activate()
        keyboard.send("l")

def handle(user_input: str, intent_group: dict):
    intent_name = classify(user_input, intent_group)
    user_input = user_input.lower()
    clean_input = user_input
    for prefix in ["play ", "put on ", "queue ", "stream ", "turn on "]:
        if clean_input.startswith(prefix):
            clean_input = clean_input[len(prefix):]
            break
    clean_input = clean_input.strip()   
    if intent_name == "play":
        if clean_input == "":
            if is_playing() == "paused":
                play_pause()
        else:           
            play(clean_input)
    elif intent_name == "stop":
        if is_playing() == "playing":
            play_pause()
    elif intent_name == "mute" or intent_name == "unmute":
        if intent_name == "mute" and not is_muted():
            mute()
        elif intent_name == "unmute" and is_muted():
            mute()
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

