# Simple AI Agent

A lightweight AI agent implementation built with LangChain and LangGraph that provides an interactive conversational interface with tool capabilities.

## Features

- Interactive chat interface with OpenAI GPT-4o
- Built-in calculator tool for mathematical operations
- Extensible tool system for adding custom functionality
- Streaming responses for real-time interaction
- Environment-based configuration

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Simple-AI-Agent.git
cd Simple-AI-Agent

# Install dependencies using uv (recommended)
uv sync

# Or install with pip
pip install -r requirements.txt
```

## Prerequisites

- Python 3.13 or higher
- OpenAI API key

## Setup

1. Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

2. Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Usage

Run the agent:

```bash
python main.py
```

The agent will start an interactive session where you can:

- Have conversations with the AI
- Use the built-in calculator by asking math questions
- Type 'exit' to quit

### Example interactions:

```
You: What is 25 + 37?
Agent: I'll help you calculate that. Let me use the calculator tool.

Calculating the sum of 25 and 37
The sum of 25 and 37 is 62

You: Tell me about Python programming
Agent: Python is a high-level, interpreted programming language...
```

## Configuration

The agent can be customized by modifying the following in `main.py`:

- **Model**: Change the OpenAI model (currently set to `gpt-4o`)
- **Temperature**: Adjust response creativity (currently set to `0` for deterministic responses)
- **Tools**: Add custom tools to extend functionality

### Adding Custom Tools

To add new tools, define them using the `@tool` decorator:

```python
@tool
def your_custom_tool(parameter: str) -> str:
    """Description of what your tool does."""
    # Your tool logic here
    return "result"

# Add to tools list
tools = [calculator, your_custom_tool]
```

## Dependencies

This project uses the following main dependencies:

- **LangChain** (>=0.3.27): Framework for building applications with LLMs
- **LangChain OpenAI** (>=0.3.33): OpenAI integration for LangChain
- **LangGraph** (>=0.6.7): Tool for building stateful, multi-actor applications
- **python-dotenv** (>=1.1.1): Environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -am 'Add some feature'`)
6. Push to the branch (`git push origin feature/your-feature`)
7. Submit a pull request

## License

[Your license information]
