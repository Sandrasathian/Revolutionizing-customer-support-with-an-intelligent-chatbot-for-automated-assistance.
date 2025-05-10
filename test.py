import openai

# Replace with your actual API key if you're using OpenAI
openai.api_key = "your-api-key-here"

def chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful customer support assistant."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return response.choices[0].message['content'].strip()

def main():
    print("Welcome to the Customer Support Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Thank you for contacting support. Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
