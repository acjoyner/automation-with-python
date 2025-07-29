from pytube import YouTube
import os

print("🚀 Starting download script...")

# IMPORTANT: Replace this with a REAL YouTube video link.
# The previous link "https://www.youtube.com/watch?v=nzIq9RSZoA8" is not valid.
# Example of a valid YouTube video link (a public domain video):
link = "https://www.youtube.com/watch?v=LXb3EKWsInQ" # Example: "Big Buck Bunny"

try:
    yt = YouTube(link)
    print("✅ Title:", yt.title)
    print("👀 Views:", yt.views)

    # Get the highest quality stream available for download
    yd = yt.streams.get_highest_resolution()

    # Define the download path on the Desktop
    # os.path.expanduser("~") gets the user's home directory
    download_path = os.path.expanduser("~/Desktop/downloaded_videos")

    # Create the directory if it doesn't exist
    os.makedirs(download_path, exist_ok=True)

    print(f"⬇️ Downloading '{yt.title}' to: {download_path}")
    yd.download(output_path=download_path)

    print("✅ Download completed successfully!")

except Exception as e:
    print(f"❌ An error occurred: {e}")
    print("Please ensure the YouTube link is valid and accessible. If the issue persists,")
    print("try updating or reinstalling pytube, or use a different video link.")

