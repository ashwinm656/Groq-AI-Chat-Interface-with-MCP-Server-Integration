
# Groq-AI-Chat-Interface-with-MCP-Server-Integration

Welcome! This project integrates **MCP agents** powered by **Groq AI** into an interactive **Streamlit** web app. It enables seamless multi-agent workflows, with each agent hosted and managed via configurable MCP hosts.

## 📁 What’s Inside?

- **MCP Hosts Config** — Define agent servers in `servers.json` (e.g., "playwright", "airbnb") with commands to launch each MCP server.  
- **Groq AI Integration** — Uses the `langchain-groq` library for advanced AI chat capabilities.  
- **Streamlit UI** — Simple and intuitive interface to chat and interact with MCP agents in real time.  
- **Async Support** — Efficient asynchronous calls to handle multiple agents smoothly.  

## 🚀 Getting Started

### 1. How to Run

1. Clone the repository:  
   ```bash
   git clone https://github.com/ashwinm656/Groq-AI-Chat-Interface-with-MCP-Server-Integration.git
   cd Groq-AI-Chat-Interface-with-MCP-Server-Integration


### 2. Set Up Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt  # or use pyproject.toml if preferred
```

> If you're using `pyproject.toml`, install with:
```bash
pip install uv
uv pip install -r pyproject.toml
```

### 3. Configure Servers

Edit `servers.json` to define the MCP agent servers. Example:
```json
{
  "playwright": {
    "host": "http://localhost:8001",
    "command": "python playwright_server.py"
  },
  "airbnb": {
    "host": "http://localhost:8002",
    "command": "python airbnb_server.py"
  }
}
```

### 4. Run the App

```bash
streamlit run app.py
```

## 🔐 Environment Variables

Create a `.env` file in the root directory with the necessary variables. Example:

```env
GROQ_API_KEY=your_api_key_here
```

## 🧠 Features

- Multi-agent support via custom MCP backends
- Groq AI-driven chat with `langchain`
- Real-time Streamlit UI
- Asynchronous backend for speed and scalability

## 📄 License

MIT License – free to use and modify.




## 🖼️ Interface Overview

Below is a preview of the chat interface with integrated MCP servers:

![MCP Server UI](Images/mcp%20server.png)


## 🧠 Built Using

- **Cursor AI** – Developed and managed with the help of Cursor AI IDE for seamless AI-assisted coding.
- **Streamlit**, **Langchain**, **Groq AI**, and custom **MCP agent servers**.

