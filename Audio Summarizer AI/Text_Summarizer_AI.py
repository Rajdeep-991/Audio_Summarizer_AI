# Import the Google Generative AI library and alias it as genai
import google.generativeai as genai

# Load Google API key from a file
with open('Google_API_Key.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

# Configure the Generative AI API with the loaded API key
genai.configure(api_key = GOOGLE_API_KEY)

# Select the generative model
model = genai.GenerativeModel('gemini-pro')

# Function to get summary from the transcript
def get_summary(transcript):
    prompt = """Summarize and Take Notes on the following Transcript from a Lecture""" + transcript
    response = model.generate_content(prompt)
    return response.text

print()

# Uncomment the following line to test the summarizer with a sample transcript
#print(get_summary("""Hey everyone, life's like a box of chocolates, right? Full of surprises. So, let's roll with the punches. Take each day as it comes and make the most of every moment. Cheers to randomness, thanks!""").replace('**', ''), "\n")
