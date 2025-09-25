# Local Ollama Chat Interface

A privacy-focused chat application built with Chainlit that runs entirely on your local machine using Ollama's LLaMA 3.2 Vision model. This application provides a secure, private AI assistant experience with support for both text and image inputs.

## Features

- 🏠 **Completely Local**: Runs entirely on your machine - no data sent to external servers
- 🔒 **Privacy First**: All conversations stay on your device
- 🖼️ **Vision Support**: Upload and analyze images with the AI
- 💬 **Conversational Memory**: Maintains full context throughout your chat session
- ⚡ **Real-time Streaming**: Responses stream token-by-token for immediate feedback
- 🎨 **Friendly Interface**: Clean, modern chat interface powered by Chainlit

## Prerequisites

Before running this application, ensure you have:

1. **Python 3.8+** installed on your system
2. **Ollama** installed and running locally
3. **LLaMA 3.2 Vision model** pulled in Ollama

##  Offline GPT Screenshot

<p align="center">
  <img src="https://github.com/SushilkumarBarai/OfflineGPT/blob/main/Screenshot_1.png" alt="Screenshot_1" width="600"/>
</p>

<p align="center">
  <img src="https://github.com/SushilkumarBarai/OfflineGPT/blob/main/Screenshot_2.png" alt="Screenshot_1" width="600"/>
</p>

## Installation

### 1. Install Ollama

Visit [ollama.ai](https://ollama.ai) and follow the installation instructions for your operating system.

### 2. Pull the Required Model

```bash
ollama pull llama3.2-vision:latest
```

### 3. Install Python Dependencies

```bash
pip install chainlit ollama
```

## Usage

### Starting the Application

1. Make sure Ollama is running:
```bash
ollama serve
```

2. Run the chat application:
```bash
chainlit run app.py
```

3. Open your browser and navigate to the URL shown in the terminal (typically `http://localhost:8000`)

### Using the Chat Interface

- **Text Conversations**: Simply type your messages and press Enter
- **Image Analysis**: 
  - Click the attachment button to upload images
  - The AI can analyze, describe, and answer questions about your images
  - Supports common image formats (JPEG, PNG, etc.)
- **Conversation Memory**: The AI remembers the full context of your conversation

## Configuration

### Changing the Model

To use a different Ollama model, modify the `MODEL_NAME` variable at the top of the file:

```python
MODEL_NAME = "your-preferred-model:tag"
```

Make sure the model is pulled in Ollama first:
```bash
ollama pull your-preferred-model:tag
```

### Customizing Greetings

The application randomly selects from several greeting messages. You can modify or add new greetings by editing the `greetings` list in the code.

## How It Works

The application consists of three main components:

1. **Session Initialization** (`@cl.on_chat_start`): Sets up conversation memory and displays a random greeting
2. **Message Processing** (`@cl.on_message`): Handles incoming user messages and image uploads
3. **AI Integration** (`@cl.step`): Manages communication with the Ollama model while preserving conversation context

### Key Features:

- **Persistent Memory**: Each conversation maintains full context using Chainlit's session management
- **Async Processing**: Non-blocking operations ensure smooth user experience
- **Image Support**: Automatically detects and processes image uploads
- **Token Streaming**: Responses appear in real-time as they're generated

## Troubleshooting

### Common Issues

**"Model not found" error:**
- Ensure Ollama is running: `ollama serve`
- Verify the model is pulled: `ollama list`
- Pull the model if missing: `ollama pull llama3.2-vision:latest`

**Application won't start:**
- Check that all dependencies are installed: `pip list | grep -E "(chainlit|ollama)"`
- Ensure Python version is 3.8 or higher: `python --version`

**Slow responses:**
- The model runs locally, so performance depends on your hardware
- Consider using a smaller model if responses are too slow
- Ensure sufficient RAM and CPU resources are available

## Privacy & Security

This application is designed with privacy in mind:

- ✅ All processing happens locally on your machine
- ✅ No data is sent to external servers
- ✅ Conversations are not stored permanently (unless you explicitly save them)
- ✅ Full control over your data and AI interactions

## Requirements

- Python 3.8+
- Ollama with llama3.2-vision:latest model
- Chainlit
- At least 4GB RAM (8GB+ recommended for better performance)

## License

This project is open source. Please ensure you comply with the licensing terms of the underlying models and libraries used.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this application.

---

**Note**: This application requires a local installation of Ollama and the specified model. Performance will vary based on your hardware specifications.
