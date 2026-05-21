from groq import Groq

client = Groq(api_key="ENTER YOUR API KEY") #https://console.groq.com — completely free!

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("🤖 Chatbot Ready! Type 'bye' to exit.")
print("-" * 40)

while True:
    user_input = input("You\n> ").strip()

    if not user_input:
        continue

    if user_input.lower() == "bye":
        print("Bot: Alvida! 👋")
        break

    conversation_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  
            messages=conversation_history
        )

        bot_reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": bot_reply})
        print(f"Bot: {bot_reply}\n")

    except Exception as e:
        print(f"404 Error: {e}\n")