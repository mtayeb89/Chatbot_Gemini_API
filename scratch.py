import google.generativeai as genai

# Set up your Google API key (replace with your actual key)
GOOGLE_API_KEY = "Put your API KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the GenerativeAI model
model = genai.GenerativeModel("gemini-pro")

print("Chatbot: Hi! Type your message (or enter an empty string to exit).")
while True:
    user_input = input("You: ")
    if not user_input:
        print("Chatbot: Goodbye!")
        break

    # Generate a response from the Gemini model
    response = model.generate_content(user_input)
    print("Chatbot:", response.text)
