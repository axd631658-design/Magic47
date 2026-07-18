import streamlit as st
import os

from editor import get_video_duration, get_audio_duration
from utils import save_uploaded_file

st.set_page_config(page_title="Magic47 AI Reel Maker V2")

st.title("🎬 Magic47 AI Reel Maker V2")
st.write("Upload your videos, voice and music.")

videos = st.file_uploader(
    "Upload Video Clips",
    type=["mp4", "mov", "avi"],
    accept_multiple_files=True
)

voice = st.file_uploader(
    "Upload Voice",
    type=["mp3", "wav", "m4a"]
)

music = st.file_uploader(
    "Upload Background Music",
    type=["mp3", "wav"]
)

# Save uploaded files

video_paths = []

if videos:
    for video in videos:
        path = save_uploaded_file(video)
        video_paths.append(path)

voice_path = None
if voice:
    voice_path = save_uploaded_file(voice)

music_path = None
if music:
    music_path = save_uploaded_file(music)
