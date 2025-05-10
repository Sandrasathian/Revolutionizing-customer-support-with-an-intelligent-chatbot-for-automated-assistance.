import openai
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI API key
openai.api_key = "your-api-key-here"  # Replace with your actual key

# Function to get chatbot response
def get_chatbot_response(user_message):
    try:
        logger.info(f"User: {user_message}")
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are an intelligent customer support assistant. Be helpful, concise, and friendly."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.6,
            max_tokens=250
        )
        reply = response.choices[0].message['content'].strip()
        logger.info(f"Chatbot: {reply}")
        return reply
    except Exception as e:
        logger.error(f"Error getting response: {e}")
        return "Sorry, I'm having trouble understanding your request right now."

# Main chatbot loop
def main():
    print("🚀 Welcome to Customer Support Chatbot")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Thank you! Have a great day.")
            break
        response = get_chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
