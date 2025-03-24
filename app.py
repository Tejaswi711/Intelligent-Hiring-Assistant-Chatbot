# Import necessary libraries
import streamlit as st
from langchain_community.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Debug: Print the API key
print("HIRING_ASSISTANT_API_KEY:", os.getenv("HIRING_ASSISTANT_API_KEY"))

# Retrieve the OpenAI API key from the environment
openai_api_key = os.getenv("HIRING_ASSISTANT_API_KEY")
if openai_api_key is None:
    st.error("OpenAI API key not found in environment variables. Please check your `.env` file.")
    st.stop()  # Stop the app if the API key is missing

# Set the OpenAI API key in the environment
os.environ["OPENAI_API_KEY"] = openai_api_key

# Set up the Streamlit app
st.title("Intelligent Hiring Assistant Chatbot")

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state['history'] = []


# Function to generate response using OpenAI
def generate_response(prompt):
    llm = OpenAI(temperature=0.7)  # You can adjust the temperature for creativity
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory)
    response = conversation.predict(input=prompt)
    return response


# Streamlit UI components
user_input = st.text_input("You: ", "")

if user_input:
    # Generate a response from the chatbot
    response = generate_response(user_input)

    # Update conversation history
    st.session_state['history'].append(f"You: {user_input}")
    st.session_state['history'].append(f"Bot: {response}")

# Display conversation history
st.subheader("Conversation History")
for message in st.session_state['history']:
    st.write(message)