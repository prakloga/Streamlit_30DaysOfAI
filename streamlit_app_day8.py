#Day 8: Meet the Chat Elements
import streamlit as st

st.title(":material/chat: Meet the Chat Elements")

# 2.Chat Input
prompt = st.chat_input("Type a message here...")

# 3. Reacting to Input
if prompt:
    # Display the User's new message
    with st.chat_message("user"):
        st.write(prompt)

    # Display a mock assistant response
    with st.chat_message("assistant"):
        st.write(f"You just said:\n\n '{prompt}' \n\n(I don't have memory yet)")