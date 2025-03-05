# davinci-transcribe
An easy to use script for creating transcripts using AI for free.

This script should be run from an external Python environment, not from within DaVinci Resolve. Here’s how you can run it:

## Steps to Run the Script

Ensure DaVinci Resolve is Open

Open DaVinci Resolve and load your project.
Install Dependencies (if needed)

Make sure you have the openai Python package installed:

```bash
pip install openai
```

## Set Up the Script

Update project_directory to point to your working directory.
Replace "your-api-key" with your actual OpenAI API key.
Run the Script in a Terminal

Open a terminal or command prompt and run:

```bash
python transcribe.py
```

## After running the script:

The video, extracted audio, and transcript will all be saved in the project directory.
You can import the transcript (SRT file) manually into DaVinci Resolve under Subtitle Tracks.


## Why Not Run It Inside Resolve?
DaVinci Resolve’s scripting console is limited in functionality and doesn't support external API calls (like OpenAI Whisper).

Running it externally allows better error handling and debugging.