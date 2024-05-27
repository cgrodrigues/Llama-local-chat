import requests
import streamlit as st

# Local model server address
ollama_url = "http://localhost:11434/api/chat"



# Function to add the Llama3 indication
def llama3_text():
    # Criar um container para o texto
    st.header("Power by Llama 3 model and Ollama running Locally")



def main():
    st.title("Ollama Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
                st.markdown(prompt)

        # Prepare the data to send to your local model
        data = {
            "model": "llama3",
            "messages": [
                {
                    "role": m["role"],
                    "content": m["content"]
                } for m in st.session_state.messages
            ],
            "stream": False
        }
        

        # Send a post request to your model server
        response = requests.post(ollama_url, json=data)
    

        if response.status_code == 200:
            # Assuming the response includes the generated text directly
            generated_text = response.json()['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": generated_text})
            with st.chat_message("assistant"):
                st.markdown(generated_text)
        else:
            st.error("Failed to generate response from the model.")
     

# Put the LLama 3 name in the page
llama3_text()

main()