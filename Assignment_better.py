import streamlit as st
from huggingface_hub import InferenceClient

# Pre-prompt for code optimization
CODE_OPTIMIZATION_PROMPT = """
You are a code optimization expert. When presented with code, your task is to:
1. Determine if the code can be optimized
2. If optimization is possible:
   - Respond with "Yes"
   - Provide a detailed explanation of optimization techniques
   - Share the fully optimized code
3. If no significant optimization is possible, respond with "No"
"""

# Page configuration
st.set_page_config(page_title="Code Optimizer", page_icon="💻", layout="centered")

# Initialize session state for chat history if not exists
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for API configuration
st.sidebar.title("🤖 Code Optimization Settings")
api_key = st.sidebar.text_input("Hugging Face API Key", type="password")
model_name = st.sidebar.text_input("Model Name", value="Qwen/Qwen2.5-Coder-32B-Instruct")
max_tokens = st.sidebar.number_input("Max Response Length", min_value=50, max_value=2048, value=500)

# Main chat interface
st.title("💻 Code Optimization Chat")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Paste your code for optimization"):
    # Check if API key is provided
    if not api_key:
        st.warning("Please enter your Hugging Face API key in the sidebar.")
    else:
        # Combine pre-prompt with user's code
        full_prompt = f"{CODE_OPTIMIZATION_PROMPT}\n\nCode to optimize:\n{prompt}"
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Show loading indicator
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Analyzing and optimizing code...")
            
            try:
                # Create Inference Client
                client = InferenceClient(api_key=api_key)
                
                # Prepare messages for API call
                messages = [
                    {"role": "system", "content": CODE_OPTIMIZATION_PROMPT},
                    {"role": "user", "content": prompt}
                ]
                
                # Generate response
                completion = client.chat.completions.create(
                    model=model_name, 
                    messages=messages, 
                    max_tokens=max_tokens
                )
                
                # Get the response
                response = completion.choices[0].message.content
                
                # Display response
                message_placeholder.markdown(response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response
                })
                
            except Exception as e:
                message_placeholder.markdown(f"Error: {str(e)}")

# Sidebar additional information
st.sidebar.markdown("---")
st.sidebar.info("""
    🚀 Code Optimization Interface
    - Specializes in code improvement suggestions
    - Requires Hugging Face API key
    - Customizable model and response length
""")