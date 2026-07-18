from moviepy import VideoFileClip, AudioFileClip

def get_video_duration(video_path):
    clip = VideoFileClip(video_path)
    duration = clip.duration
    clip.close()
    return duration

def get_audio_duration(audio_path):
    audio = AudioFileClip(audio_path)
    duration = audio.duration
    audio.close()
    return duration
