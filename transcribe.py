import sys
import os

# Detect the operating system
if sys.platform == "darwin":  # macOS
    dvr_path = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules/"
elif sys.platform == "win32":  # Windows
    dvr_path = r"C:\Program Files\Blackmagic Design\DaVinci Resolve\Developer\Scripting\Modules"
elif sys.platform == "linux" or sys.platform == "linux2":  # Linux
    dvr_path = "/opt/resolve/Developer/Scripting/Modules/"
else:
    raise EnvironmentError("Unsupported OS")

# Add the correct path to sys.path
sys.path.append(dvr_path)

# Import DaVinci Resolve Script module
import DaVinciResolveScript as dvr
import openai
import sys
import os

# OpenAI Whisper API Key
OPENAI_API_KEY = "your-api-key"  # Replace with your actual API key

# Define project directory
project_directory = "/path/to/project/"  # Change to your project location
input_video = os.path.join(project_directory, "video.mp4")
output_audio = os.path.join(project_directory, "audio.wav")
srt_file = os.path.join(project_directory, "transcript.srt")

# Connect to DaVinci Resolve
resolve = dvr.scriptapp("Resolve")
if not resolve:
    print("Could not connect to DaVinci Resolve.")
    sys.exit(1)

project_manager = resolve.GetProjectManager()
project = project_manager.GetCurrentProject()
if not project:
    print("No active project found.")
    sys.exit(1)

media_pool = project.GetMediaPool()

# Import media
media_pool.ImportMedia([input_video])

# Get timeline
timeline = project.GetCurrentTimeline()
if not timeline:
    timeline = media_pool.CreateEmptyTimeline("AudioExtraction")
    media_pool.AppendToTimeline(input_video)

# Export audio
render_settings = {
    "TargetDir": project_directory,  # Output directory
    "CustomName": "audio",
    "Format": "wav",
    "AudioCodec": "pcm",
    "Video": False,  # Exclude video
    "Audio": True   # Include audio
}
project.SetRenderSettings(render_settings)
project.StartRendering()


# Transcribe audio using Whisper API
def transcribe_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file, api_key=OPENAI_API_KEY)
    return response["text"]


transcript = transcribe_audio(output_audio)

# Save transcript as SRT file
with open(srt_file, "w") as f:
    f.write("1\n00:00:00,000 --> 00:00:10,000\n" + transcript + "\n")

print(f"Transcript saved to: {srt_file}")
