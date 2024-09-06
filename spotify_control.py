import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-modify-playback-state user-read-playback-state user-read-currently-playing'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

gesture_detection_enabled = True

def volume_up():
    if gesture_detection_enabled:
        current_volume = sp.current_playback()['device']['volume_percent']
        sp.volume(min(100, current_volume + 10))

def volume_down():
    if gesture_detection_enabled:
        current_volume = sp.current_playback()['device']['volume_percent']
        sp.volume(max(0, current_volume - 10))

def next_track():
    if gesture_detection_enabled:
        sp.next_track()

def prev_track():
    if gesture_detection_enabled:
        sp.previous_track()

def shuffle():
    if gesture_detection_enabled:
        current_shuffle_state = sp.current_playback()['shuffle_state']
        sp.shuffle(not current_shuffle_state)

def toggle_pause_play():
    if gesture_detection_enabled:
        playback_info = sp.current_playback()
        if (playback_info is not None) and playback_info['is_playing']:
            sp.pause_playback()
        else:
            sp.start_playback()


def gesture_handler(get_hand_sign_id):
    global gesture_detection_enabled
    last_detected_gesture = None

    while True:
        current_gesture = get_hand_sign_id()
        print(f"Current_gesture: {current_gesture}, DetectionBool: {gesture_detection_enabled}")

        if current_gesture != last_detected_gesture:

            if current_gesture == 0:
                volume_down()
            elif current_gesture == 1:
                volume_up()
            elif current_gesture == 2:
                next_track()
            elif current_gesture == 3:
                prev_track()
            elif current_gesture == 4:
                shuffle()
            elif current_gesture == 5:
                toggle_pause_play()
            elif current_gesture == 6:
                gesture_detection_enabled = not gesture_detection_enabled
            else:
                print("Unknown Gesture")

            last_detected_gesture = current_gesture

        time.sleep(0.1)  # Adjust the sleep duration based on how frequently you want to check
