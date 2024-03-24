import google.generativeai as genai

with open('Google_API_Key.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_summary(transcript):
    prompt = """Summarize and Take Notes on the following Transcript from a Lecture""" + transcript
    response = model.generate_content(prompt)
    return response.text

print()
#print(get_summary("""Hey everyone, life's like a box of chocolates, right? Full of surprises. So, let's roll with the punches. Take each day as it comes and make the most of every moment. Cheers to randomness, thanks!""").replace('**', ''), "\n")