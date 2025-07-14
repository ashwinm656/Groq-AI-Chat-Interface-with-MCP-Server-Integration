import streamlit as st
import asyncio
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

# Load environment variables
load_dotenv()

CONFIG_FILE = "servers.json"

# Load MCP servers from config
with open(CONFIG_FILE) as f:
    config_data = json.load(f)
    mcp_servers = config_data.get("mcpServers", {})

# Initialize session state
if "client" not in st.session_state:
    st.session_state.client = MCPClient.from_config_file(CONFIG_FILE)
if "llm" not in st.session_state:
    st.session_state.llm = ChatGroq(model="llama-3.3-70b-versatile")
if "agent" not in st.session_state:
    st.session_state.agent = MCPAgent(
        llm=st.session_state.llm,
        client=st.session_state.client,
        max_steps=15,
        memory_enabled=True,
    )
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Async wrapper
async def get_response(agent, user_input):
    try:
        response = await agent.run(user_input)
        return response
    except Exception as e:
        return f"Error: {e}"

# Custom CSS styles with glowing bold title
def local_css():
    st.markdown(
        """
        <style>
        .title {
            color: #FFFFFF;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: bold;
            font-size: 38px;
            margin-bottom: 0px;
            text-shadow: 0 0 8px #00FFC6, 0 0 12px #00FFC6;
        }
        .subtitle {
            color: #AAAAAA;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin-top: 0px;
            margin-bottom: 25px;
            font-style: italic;
        }
        .user-msg {
            background-color: #3498DB;
            color: white;
            padding: 12px 18px;
            border-radius: 15px 15px 0 15px;
            max-width: 80%;
            margin-bottom: 10px;
            font-size: 16px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .assistant-msg {
            background-color: #2ECC71;
            color: white;
            padding: 12px 18px;
            border-radius: 15px 15px 15px 0;
            max-width: 80%;
            margin-bottom: 10px;
            font-size: 16px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .footer {
            font-size: 14px;
            color: #95A5A6;
            text-align: center;
            margin-top: 40px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Main UI
def main():
    local_css()

    st.markdown('<div class="title">MCP Interactive Chat</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Groq AI Chat Interface with MCP Server Integration</div>', unsafe_allow_html=True)

    # Sidebar with MCP server list
    with st.sidebar:
        st.header("MCP Servers Included")
        for server_name, server_info in mcp_servers.items():
            cmd = server_info.get("command", "")
            args = " ".join(server_info.get("args", []))
            st.markdown(f"**{server_name}**  \n_Command:_ `{cmd} {args}`")

        st.markdown("---")
        st.markdown("Developed by Ashwin Muralidharan")

    # Show chat history
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f'<div class="user-msg">You: {chat["message"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-msg">Assistant: {chat["message"]}</div>', unsafe_allow_html=True)

    # Text input
    user_input = st.text_input("Type your message:", key="input")

    # Send button
    if st.button("Send") and user_input.strip():
        st.session_state.chat_history.append({"role": "user", "message": user_input})
        response = asyncio.run(get_response(st.session_state.agent, user_input))
        st.session_state.chat_history.append({"role": "assistant", "message": response})
        st.rerun()  # Rerun after updating session state

    # Clear conversation button
    if st.button("Clear Conversation"):
        st.session_state.chat_history = []
        st.session_state.agent.clear_conversation_history()
        st.rerun()

    # Footer
    st.markdown('<div class="footer">Developed by Ashwin Muralidharan</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
