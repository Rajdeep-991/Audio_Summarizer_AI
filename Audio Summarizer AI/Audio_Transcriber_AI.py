# Import the Whisper library for audio transcription
import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe("Sample_Audio_1.mp3")

# Print the transcript
print("\nTranscript\n----------")
print(result["text"].strip(), "\n")
