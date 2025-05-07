from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("Ai sticky notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__),"notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file

    Args:
    message (str): The note content to be added.

    Returns:
        str: Confirmation message indicating the note was saved.

    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "NOTE saved"
@mcp.tool()
def read_notes()->str:
    """
    Read and return all notes from the sticky note file.

    Returns:
        str: All notes as a single string seperated by line breaks.
            if no notes exists, a default message is returned.

    """
    ensure_file()
    with open(NOTES_FILE,"r") as f:
        content = f.read().strip()
    return content or "no notes yet"

@mcp.resource("notes://latest")
def get_latest_notes()->str:
    """
     Get the most recently added note from the sticky note file.

    Returns:
        str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE,"r") as f:
        lines = f.read().strip()
    return lines[-1].strip() if lines else "no notes yet"

@mcp.prompt()
def not_summary_prompt()->str:
    """
    Generate a prompt asking the AI to summarize all current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
             If no notes exist, a message will be shown indicating that.
    """
    ensure_file()
    with open(NOTES_FILE,"r") as f:
        content = f.read().strip()
    if not content:
        return "there are no notes yet"
    return f"summarise the current notes: {content}" 