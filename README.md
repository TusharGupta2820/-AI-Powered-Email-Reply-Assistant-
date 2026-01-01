# Email Reply Assistant Agent

An AI-powered assistant that helps generate professional email replies using advanced language models.

## Features

- **Context-aware replies**: Understands the intent of incoming emails
- **Tone selection**: Choose between Formal, Casual, or Friendly tones
- **Auto-tone detection**: Automatically detects appropriate tone if not specified
- **Streamlit UI**: User-friendly interface for easy interaction
- **Copy functionality**: One-click copy to clipboard for generated replies

## Requirements

- Python 3.8 or higher
- Internet connection for API access

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:

```bash
streamlit run app.py
```

2. The application will open in your default browser at `http://localhost:8501`

3. In the left panel:
   - Paste or type the incoming email text in the text area
   - Select your preferred response tone (Formal, Casual, Friendly) or leave as "Auto" for AI detection
   - Click "Generate Reply"

4. The generated reply will appear in the right panel
5. Use the "📋 Copy to Clipboard" button to copy the reply to your clipboard

## Project Structure

```
EmailReplyAssistant/
│
├── app.py              # Streamlit UI implementation
├── ai_agent.py         # AI logic and LLM integration
├── config.py           # API key and configuration settings
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## How It Works

1. **Intent Analysis**: The AI analyzes the incoming email to understand its purpose
2. **Tone Detection**: Automatically detects appropriate response tone or uses your selection
3. **Reply Generation**: Creates a context-aware, professional reply using the DeepSeek model
4. **Output**: Provides a grammatically correct, polite, and professional reply

## API Configuration

The application uses OpenRouter API with the DeepSeek model. The API key is configured in `config.py`.

## Example Use Cases

- Professional email correspondence
- Customer service responses
- Business communication
- Follow-up emails
- Meeting scheduling

## License

This project is created for educational and personal use.