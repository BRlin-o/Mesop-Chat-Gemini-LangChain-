# Mesop Demo

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Using Google Generative AI

To run the chat interface using the Google Generative AI:

```bash
python gemini.py
```

### Using Langchain

To run the chat interface using Langchain:

```bash
python gemini_langchain.py
```

## Environment Variables

Make sure to set up your `.env` file with the following content:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Gemini API key.

## Project Structure

- `gemini.py`: Uses the Google Generative AI package.
- `gemini_langchain.py`: Uses the Langchain package.
- `requirements.txt`: Lists the dependencies required for the project.
- `.env`: Contains environment variables such as the API key.