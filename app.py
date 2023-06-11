# %% imports
import base64
import streamlit as st
from pytube import YouTube


# %% App Config
st.set_page_config(
    page_title="Download Internet Media",
    page_icon="cloud-arrow-down",
    layout="wide",
    initial_sidebar_state="expanded",
)


# %% Functions
pass


# %% Main Body
# Title
st.title("Download Internet Media")

# Get Video URL
# video_url = "https://www.youtube.com/watch?v=lx68okMe2fo"
video_url = st.text_input("Paste your URL")


if video_url:
    # Get File
    video_path = (
        YouTube(video_url)
        .streams.filter(res="720p")
        .first()
        .download("local_data")
    )
    with open(video_path, "rb") as file:
        video_bytes = file.read()

    # Video Title and type (mp4, ...)
    video_title = YouTube(video_url).vid_info["videoDetails"]["title"]
    video_type = video_path.split(".")[-1]

    st.download_button(
        label="Download",
        data=video_bytes,
        file_name=f"{video_title}.{video_type}",
    )
