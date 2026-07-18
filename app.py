import streamlit as st
import tempfile
from moviepy import VideoFileClip
from moviepy import AudioFileClip

st.set_page_config(page_title="Magic47 AI Reel Maker")

st.title("🎬 Magic47 AI Reel Maker")
st.write("Welcome to Magic47!")

# Upload Video Clips
video = st.file_uploader(
    "Upload Video Clips",
    accept_multiple_files=True,
    type=["mp4", "mov", "avi"]
)

# Upload Voice
voice = st.file_uploader(
    "Upload Voice",
    type=["mp3", "wav", "m4a"]
)

# Show Voice Duration
if voice:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
        temp.write(voice.read())
        audio_path = temp.name

    audio = AudioFileClip(audio_path)
    st.write(f"🎙️ Voice Duration: {audio.duration:.2f} seconds")

# Upload Background Music
music = st.file_uploader(
    "Upload Background Music",
    type=["mp3", "wav"]
)
if music:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
        temp.write(music.read())
        music_path = temp.name

    bg_music = AudioFileClip(music_path)
    st.write(f"🎵 Music Duration: {bg_music.duration:.2f} seconds")
# Create Reel Button
if st.button("Create Reel"):
    st.success("🚀 Reel generation feature will be added soon!")

# Show Uploaded Video Durations
if video:
    st.write("Uploaded Videos:")
    for v in video:
        st.write(f"📹 {v.name}")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp:
            temp.write(v.read())
            video_path = temp.name

        clip = VideoFileClip(video_path)
        st.write(f"⏱️ Duration: {clip.duration:.2f} seconds")
