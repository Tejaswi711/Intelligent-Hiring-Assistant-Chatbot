import os
 from dotenv import load_dotenv
 # Load environment variables from .env file
 load_dotenv()
 # OpenAI API Key
 OPENAI_API_KEY = os.getenv("HIRING_ASSISTANT_API_KEY")
 if OPENAI_API_KEY is None:
    raise ValueError("OpenAI API key not found. Please check your .env file.")
 # Chatbot Configuration
 CHATBOT_SETTINGS = {
    "temperature": 0.7,  # Controls the creativity of responses
    "memory_type": "ConversationBufferMemory",  # Defines memory storage type
 }
 # Streamlit UI Config
 UI_CONFIG = {
    "title": "Intelligent Hiring Assistant Chatbot",
    "input_placeholder": "Type your message here...",
 }