Audio Summarizer AI
-------------------

Overview
--------
This project includes three components that work together to transcribe audio files into text and then summarize the transcribed text. It leverages Google Generative AI and OpenAI's Whisper model to achieve high-quality results.

Features
--------
- Text Summarization: Uses Google's Generative AI to summarize text transcripts.
- Audio Transcription: Utilizes OpenAI's Whisper model to transcribe audio files into text.
- Integrated Workflow: Combines transcription and summarization to provide concise summaries of audio content.

Requirements
------------
- Python 3.x
- google.generativeai library
- whisper library
- Google API Key for accessing Generative AI services
- Pre-trained models for Whisper and Generative AI

How To Use
----------
- Install Required Libraries:
  - Ensure you have the required Python libraries installed. You can install them using pip:

    pip install google-generativeai whisper

- Setup API Key:
  - Save your Google API Key in a file named Google_API_Key.txt.

- Text Summarizer:
  - Save the text summarizer code into a Python file, e.g., text_summarizer.py.
  - Run the file to test the summarizer function.
  - You can uncomment the test line to see a sample summary.

- Audio Transcriber:
  - Save the transcriber code into a Python file, e.g., audio_transcriber.py.
  - Run the file to transcribe Sample_Audio_1.mp3.

- Audio Summarizer:
  - Save the audio summarizer code into a Python file, e.g., audio_summarizer.py.
  - Run the file and input the name of your audio file when prompted.
  - The program will transcribe and then summarize the audio content.

How It Works
------------
- Text Summarizer:
  - Loads the Google API key and configures the Generative AI model.
  - Defines a function to summarize a given text transcript.

- Audio Transcriber:
  - Loads the Whisper model.
  - Transcribes the provided audio file into text.

- Audio Summarizer:
  - Loads the Whisper model.
  - Prompts the user to input an audio file.
  - Transcribes the audio file into text.
  - Summarizes the transcribed text using the text summarizer function.

Notes
-----
- Ensure that your audio files are accessible and in a supported format (e.g., MP3).
- The summarizer function relies on the google.generativeai library and requires a valid API key for access.
- The transcription and summarization process may take some time depending on the length of the audio file and the complexity of the transcript.
