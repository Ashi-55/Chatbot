import openai
import gradio as gr

openai.api_key = "your-api-key"

def chat_with_gpt(message, history):
    history_openai_format = [{"role": "user", "content": message}]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history_openai_format
        )
        reply = response.choices[0].message["content"]
    except Exception as e:
        reply = f"Error: {str(e)}"
    return reply

iface = gr.ChatInterface(fn=chat_with_gpt, title="AI Support Chatbot")
iface.launch()
