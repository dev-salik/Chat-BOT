from groq import Groq
import re
import time
import textwrap


client = Groq(api_key="ENTER YOUR API_KEY") #https://console.groq.com — completely free!


conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful, friendly assistant. Reply naturally without showing internal reasoning. /no_think"
    }
]

#TYPING ANIMATION
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
def typing(text, delay=0.01):

    paragraphs = text.split("\n")
    print(GREEN, end="", )
    for para in paragraphs:
        wrapped = textwrap.fill(para, width=70)
        for char in wrapped:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()  

    print(RESET, end="")

    print()  


print("=" * 50)
print("      ✨ GROQ TERMINAL CHATBOT ✨")
print("      Type 'exit' to quit")
print("    Type 'clear' to reset chat")
print("=" * 50)


while True:
    user_input = input("\n👤 You\n> ").strip()

    if not user_input:
        continue

    if user_input.lower() == "exit":
        print("\n🤖 Bot: Goodbye! 👋")
        break

    if user_input.lower() == "clear":
        conversation_history = [conversation_history[0]]
        print("\n🧹 Chat history cleared!")
        continue

    conversation_history.append({
        "role": "user",
        "content": f"/no_think\n{user_input}"
    })

    try:
        response = client.chat.completions.create(
            model="qwen/qwen3.6-27b",
            messages=conversation_history,
            temperature=0.7,
            max_completion_tokens=1024
        )

        bot_reply = response.choices[0].message.content or ""

        # Remove <think> block if it appears
        bot_reply = re.sub(
            r"<think>.*?</think>\s*",
            "",
            bot_reply,
            flags=re.DOTALL | re.IGNORECASE
        ).strip()

        conversation_history.append({
            "role": "assistant",
            "content": bot_reply
        })

        print("\n🤖 Bot")
        typing(bot_reply)

    except Exception as e:
        print(f"\n❌ Error: {e}")
