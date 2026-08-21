# 🚀 AI Chatbot Using Groq API

A simple and fast AI chatbot built with **Python** and the **Groq API**. It features conversation memory, a clean terminal interface, typing animation, and colorful output for a better chat experience.

## ✨ Features

* Real AI responses
* Remembers conversation history
* Superfast responses
* Typing animation
* Colored terminal output
* `clear` command to reset chat
* `exit` command to close the chatbot




## 🔑 How to Get a Groq API Key

1. Go to **https://console.groq.com**
2. Create a free account.
3. Open the **API Keys** section.
4. Generate your free API key.

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dev-salik/my-chatbot.git
cd my-chatbot
```

### 2. Install Dependencies

```bash
pip install groq
```

### 3. Add Your API Key

Open `main.py` and replace the placeholder with your generated Groq API key.

```python
client = Groq(api_key="YOUR_API_KEY")
```

### 4. Run the Chatbot

```bash
python main.py
```

## 💻 Commands

| Command | Action                     |
| ------- | -------------------------- |
| `clear` | Reset conversation history |
| `exit`  | Close the chatbot          |

## 🛠️ Tech Used

* Python 3
* Groq API
* Qwen 3.6 27B *(If this model becomes outdated or not Working, you can use another model available on the Groq website.)*

## 📄 License

This project is open-source and available under the **MIT License**.
