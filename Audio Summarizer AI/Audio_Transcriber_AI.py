import whisper

model = whisper.load_model("base")
result = model.transcribe("Sample_Audio_1.mp3")

print("\nTranscript\n----------")
print(result["text"].strip(), "\n")