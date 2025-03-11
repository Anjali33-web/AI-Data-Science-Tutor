import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from config import GOOGLE_API_KEY  # Import API Key

# Streamlit UI
st.title("📚 Conversational AI Data Science Tutor")
st.write("Ask me anything about Data Science!")

# Memory for conversation awareness
memory = ConversationBufferMemory()

# Load Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY)

# Create a conversational chain with memory
conversation = ConversationChain(llm=llm, memory=memory)

# User Input
user_query = st.text_input("Enter your Data Science question:")

if user_query:
    response = conversation.run(user_query)
    st.write("🤖 Tutor:", response)

# Show conversation history
with st.expander("🔍 Conversation History"):
    st.write(memory.buffer)
