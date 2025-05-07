# AI Sticky Notes

A simple AI-powered sticky notes application built with MCP (Model Context Protocol). This application allows you to create, read, and manage notes with AI assistance.

## Features

- Add new notes
- Read all notes
- Get the latest note
- AI-powered note summarization

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. Install the required dependencies:
```bash
pip install mcp
```

## Usage

1. Run the server:
```bash
python main.py
```

2. The server provides the following tools:
   - `add_note`: Add a new note
   - `read_notes`: Read all notes
   - `get_latest_notes`: Get the most recent note
   - `not_summary_prompt`: Generate a prompt for AI to summarize notes

## Notes Storage

Notes are stored in a local `notes.txt` file in the project directory.

## License

MIT License
