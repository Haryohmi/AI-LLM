# YouTube Video Note Generator
This project provides a pipeline to extract transcripts from YouTube videos, summarize them, and generate structured a summary. It allows users to focus on specific topics within the transcript and supports follow-up questions for deeper insights.

# Features
- YouTube Transcript Extraction: Fetches transcripts from public YouTube videos.
- Summarization: Generates concise summaries tailored to user-provided prompts.
- Follow-Up Questions: Enables interactive querying of the summary for additional insights.
- Multilingual Support: Summaries can be generated in the language specified by the user. (To be implemented)
- Persistence with ChromaDB: Stores transcript data for efficient retrieval and summarization.

# Installation

1. Clone the Repository:
```bash
git clone https://github.com/Haryohmi/AI-LLM.git
cd AI-LLM/youtube_video_summary_generator
```
2. Set Up a Virtual Environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Set Up Google Credentials (for AI-powered summarization):
- Create a Google Cloud project and enable the necessary APIs.
- Download the service account key (JSON) and set the environment variable:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-key.json"
```
# Usage
1. Run the Script:
```bash
python main.py
```
2. Provide the Required Inputs:
- YouTube Video URL: URL of the video to analyze.
- Prompt: (Optional) Specify a topic to focus the summary on.
- Language: (Optional) Specify the output language for the notes.
Interactive Mode:

# Project Structure
- **`main.py`**:
  Entry point for the program.
- **`tools.py`**:
  Contains the pipeline and utility functions for transcript extraction and summarization.
- **`requirements.txt`**:
  Lists the dependencies required for the project.
- **`metadata.json`**:
  Describes the project inputs and functionality.

# Contributing
1. Fork the repository.
2. Create a feature branch:
```bash
git checkout -b feature-name
```
3. Commit and push your changes.
4. Create a pull request.


