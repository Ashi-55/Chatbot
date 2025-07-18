# AI Support Chatbot 🤖

This is a simple AI-powered chatbot using OpenAI's GPT model and Gradio for the interface.

## 🚀 Features

- Chat with GPT-3.5 Turbo
- Helpful for Q&A, assistant-like use cases
- Simple Gradio UI

## 📦 Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Add Your OpenAI Key

In `app.py`, replace:

```python
openai.api_key = "your-api-key"
```

with your actual OpenAI key.

## 🧠 Run the Chatbot

```bash
python app.py
```

## 📸 UI Preview

Gradio will launch in your browser at `http://localhost:7860`

## 📁 Folder Structure

```
chatbot-support-assistant/
├── app.py
├── requirements.txt
└── README.md
```

---

> 🔐 **Note**: Never commit your API key to public repositories!
