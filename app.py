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

# %% Side bar and settings
download_type = st.sidebar.selectbox(
    label="File Type", options=["720p", "480p", "360p", "144p", "mp3"]
)

# %% Main Body
# Title
st.title("Download Internet Media")

# Get Video URL
# video_url = "https://www.youtube.com/watch?v=lx68okMe2fo"
video_url = st.text_input("Paste your URL")


if video_url:
    # Get File
    if download_type == "mp3":
        file_path = (
            YouTube(video_url)
            .streams.filter(only_audio=True, abr="128kbps")
            .first()
            .download("local_data")
        )
    else:
        file_path = (
            YouTube(video_url)
            .streams.filter(res=download_type)
            .first()
            .download("local_data")
        )
    with open(file_path, "rb") as file:
        file_bytes = file.read()

    # Video Title
    video_title = YouTube(video_url).vid_info["videoDetails"]["title"]

    # file type
    if download_type == "mp3":
        file_type = download_type
    else:
        file_type = file_path.split(".")[-1]

    st.download_button(
        label="Download",
        data=file_bytes,
        file_name=f"{video_title}.{file_type}",
    )
