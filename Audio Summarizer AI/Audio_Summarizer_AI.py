import whisper
import Text_Summarizer_AI

model = whisper.load_model("base")
audio_file = input("Enter Audio File Name with Extension : ")
result = model.transcribe(audio_file)

transcription = result["text"]

print()
print(Text_Summarizer_AI.get_summary(transcription).replace('**', ''), "\n")