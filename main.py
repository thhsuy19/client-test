import gradio as gr
import google.generativeai as genai
import os

# Set up the Gemini API
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "AIzaSyAiNz6qQiITWUTIUQbwBwzPZxQtfTj35os")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_response(prompt, history):
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text

# Create the Gradio interface
iface = gr.ChatInterface(
    fn=generate_response,
    title="Gemini 2.0 Flash Chatbot",
    description="A simple chatbot powered by Gemini 2.0 Flash."
)

if __name__ == "__main__":
    iface.launch()