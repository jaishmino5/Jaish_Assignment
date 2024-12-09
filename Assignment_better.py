import streamlit as st
from huggingface_hub import InferenceClient


CODE_OPTIMIZATION_PROMPT = """
You are a code optimization expert. When presented with code, your task is to:
1. Determine if the code can be optimized
2. If optimization is possible:
   - Respond with "Yes"
   - Provide a detailed explanation of optimization techniques
   - Share the fully optimized code
3. If no significant optimization is possible, respond with "No"
"""


st.set_page_config(page_title="Code Optimizer", page_icon="💻", layout="centered")


if "messages" not in st.session_state:
    st.session_state.messages = []


st.sidebar.title("🤖 Code Optimization Settings")
api_key = st.sidebar.text_input("Hugging Face API Key", type="password")
model_name = st.sidebar.text_input("Model Name", value="Qwen/Qwen2.5-Coder-32B-Instruct")
max_tokens = st.sidebar.number_input("Max Response Length", min_value=50, max_value=2048, value=500)


st.title("💻 Code Optimization Chat")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Paste your code for optimization"):
   
    if not api_key:
        st.warning("Please enter your Hugging Face API key in the sidebar.")
    else:
       
        full_prompt = f"{CODE_OPTIMIZATION_PROMPT}\n\nCode to optimize:\n{prompt}"
        
       
        st.session_state.messages.append({"role": "user", "content": prompt})
        
       
        with st.chat_message("user"):
            st.markdown(prompt)
        
      
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Analyzing and optimizing code...")
            
            try:
                
                client = InferenceClient(api_key=api_key)
                
               
                messages = [
                    {"role": "system", "content": CODE_OPTIMIZATION_PROMPT},
                    {"role": "user", "content": prompt}
                ]
                
             
                completion = client.chat.completions.create(
                    model=model_name, 
                    messages=messages, 
                    max_tokens=max_tokens
                )
                
             
                response = completion.choices[0].message.content
                
       
                message_placeholder.markdown(response)
                
               
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response
                })
                
            except Exception as e:
                message_placeholder.markdown(f"Error: {str(e)}")


st.sidebar.markdown("---")
st.sidebar.info("""
    🚀 Code Optimization Interface
    - Specializes in code improvement suggestions
    - Requires Hugging Face API key
    - Customizable model and response length
""")
