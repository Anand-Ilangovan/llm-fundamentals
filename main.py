from groq import Groq
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Send a message to the LLM
def chat(user_message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    return response.choices[0].message.content

# Test it
if __name__ == "__main__":
    print("AI Assistant Ready! Type 'quit' to exit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = chat(user_input)
        print(f"\nAI: {response}\n")