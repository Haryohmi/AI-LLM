# YouTube Video Note Generator
This project provides a pipeline to extract transcripts from YouTube videos, summarize them, and generate structured a summary. It allows users to focus on specific topics within the transcript and supports follow-up questions for deeper insights.

# Features
YouTube Transcript Extraction: Fetches transcripts from public YouTube videos.
Summarization: Generates concise summaries tailored to user-provided prompts.
Follow-Up Questions: Enables interactive querying of the summary for additional insights.
Multilingual Support: Summaries can be generated in the language specified by the user. (To be implemented)
Persistence with ChromaDB: Stores transcript data for efficient retrieval and summarization.
# Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/your-repo.git
cd your-repo
Set Up a Virtual Environment:

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Google Credentials (for AI-powered summarization):

Create a Google Cloud project and enable the necessary APIs.
Download the service account key (JSON) and set the environment variable:
bash
Copy code
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-key.json"
Usage
Run the Script:

bash
Copy code
python main.py
Provide the Required Inputs:

YouTube Video URL: URL of the video to analyze.
Prompt: (Optional) Specify a topic to focus the summary on.
Language: (Optional) Specify the output language for the notes.
Interactive Mode:

After the summary is generated, you can ask follow-up questions for more details.
Type "exit" to end the session.
Example Interaction
User Input:

text
Copy code
Enter YouTube video URL: https://www.youtube.com/watch?v=example
Enter a follow-up question (or type 'exit' to quit): What is the main takeaway?
Output:

text
Copy code
Generated Summary:
The video discusses recognizing God-ordained marriages through spiritual signs and emotional connections.

Response:
The main takeaway is the speaker's emphasis on aligning spiritual and earthly marriage to maintain divine favor.

# Project Structure
main.py: Entry point for the program.
tools.py: Contains the pipeline and utility functions for transcript extraction and summarization.
requirements.txt: Lists the dependencies required for the project.
metadata.json: Describes the project inputs and functionality.
# Known Issues
Videos without transcripts or private videos are not supported.
Follow-up questions may generate verbose responses if the input is vague.
# Contributing
Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature-name
Commit and push your changes.
Create a pull request.

Let me know if you'd like to customize this further! 😊
