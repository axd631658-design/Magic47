import streamlit as st
import tempfile
from moviepy import VideoFileClip
st.set_page_config(page_title="Magic47 AI Reel Maker")

st.title("🎬 Magic47 AI Reel Maker")

st.write("Welcome to Magic47!")

video = st.file_uploader(
    "Upload Video Clips",
    accept_multiple_files=True,
    type=["mp4", "mov", "avi"]
)

voice = st.file_uploader(
    "Upload Voice",
    type=["mp3", "wav", "m4a"]
)

music = st.file_uploader(
    "Upload Background Music",
    type=["mp3", "wav"]
)

if st.button("Create Reel"):
    st.success("🚀 Reel generation feature will be added soon!")
if video:
    st.write("Uploaded Videos:")
    for v in video:
        st.write(f"📹 {v.name}")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp:
    temp.write(v.read())
    video_path = temp.name

    clip = VideoFileClip(video_path)
    st.write(f"⏱️ Duration: {clip.duration} seconds")
