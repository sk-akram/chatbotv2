import streamlit as st
import google.generativeai as genai


api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

def get_response(prompt):
    res = model.generate_content(prompt)
    return res.text



# print(get_response("What is the capital of Maharastra?"))

st.set_page_config(page_title="🤖 Welcome to Bot Server!!", layout="centered")

if "messages" not in st.session_state:
    st.session_state.messages = []

# user_input = st.text_input(label="promt", key="input",placeholder="Ask Me Anything...",label_visibility="collapsed").strip()
# send = st.button("Send")


# def build_context(current_question):
#     context = "You are a helpful assistant.\n"
#     context += "Use the following previous user questions as context.\n"
#     context += "Do NOT answer them again.\n"
#     context += "Only answer the current question below.\n\n"
    
#     context += "Previous questions:\n"
#     for msg in st.session_state.messages:
#         if msg['role'] == 'user':
#             context += f"- {msg['text']}\n"

#     context += f"\nCurrent question:\n{current_question}\n"
#     context += "Only respond to the current question using the context above."
#     context += "No need to get too serious."
#     return context

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_area(
        label="prompt",
        key="input",
        placeholder="Ask Me Anything...",
        height=70,
        max_chars=None,
        label_visibility="collapsed"
    )
    submit = st.form_submit_button("Send")


if submit and user_input.strip():
    st.session_state.messages.append({'role':'user','text':user_input})
    # context_input = build_context(user_input)
    bot_res = get_response(user_input)
    st.session_state.messages.append({'role':'bot','text':bot_res})
    st.rerun()

with st.container(border=True, height=400):
    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.markdown(
                f"<div style='color:#000000; background-color:#ffffff; padding:5px;margin: 5px 0; display: inline-block; max-width: 80%;border-radius:10px'>👤{message['text']}</div>",
                unsafe_allow_html = True
            )
        
        else:
            st.markdown(
                f"<div style='color:#ffffff; background-color:#000000; padding:5px;margin: 5px 0; display: inline-block; max-width: 80%;border-radius:10px'>🤖{message['text']}</div>",
                unsafe_allow_html = True
            )
            st.divider()


