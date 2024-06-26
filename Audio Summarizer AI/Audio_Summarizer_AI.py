# Import the Whisper library for audio transcription
import whisper

# Import the custom module Text_Summarizer_AI, which contains the text summarization function
import Text_Summarizer_AI

# Load the Whisper model
model = whisper.load_model("base")

# Prompt the user to input the audio file name
audio_file = input("Enter Audio File Name with Extension : ")

# Transcribe the audio file
result = model.transcribe(audio_file)
transcription = result["text"]

# Print the summary of the transcription
print("\n"+Text_Summarizer_AI.get_summary(transcription).replace('**', '')+"\n")
