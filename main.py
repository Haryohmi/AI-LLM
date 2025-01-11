import logging
from tools import NoteGeneratorPipeline, VideoTranscriptError

# Configure Logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def main(
    video_url: str,
    video_id: str,
    prompt: str,
    lang: str
):
    video_url = input("Enter YouTube video URL: ").strip()
    
    try:
        logger.info("Starting the Note Generator Pipeline...")

        # Initialize pipeline
        pipeline = NoteGeneratorPipeline(
            doc_url=video_url, video_id=video_id, prompt=prompt, lang=lang
        )

        # Load and split transcript
        docs = pipeline.load_docs_youtube_url(video_url)
        if not docs:
            raise VideoTranscriptError("No transcript data available", video_url)

        # Generate summary
        summary = pipeline.generate_summary(docs)
        logger.info("summary generation completed successfully.")
        print("Generated summary:")
        print(summary)
        return {"status": "success", "summary": summary}

        # Allow follow-up questions - This feature is optional
        # while True:
        #     follow_up = input("\nEnter a follow-up question (or type 'exit' to quit): ").strip()
        #     if follow_up.lower() == "exit":
        #         print("Thank you for using the Note Generator. Goodbye!")
        #         break

        #     # Refine the query with the follow-up question
        #     refined_prompt = f"{summary}\nUser question: {follow_up}"
        #     response = pipeline.model.invoke([f"Answer the question based on the summary: {refined_prompt}"])
        #     # Extract the response content
        #     if isinstance(response, dict) and 'content' in response:
        #         print("\nResponse:")
        #         print(response['content'])
        #     else:
        #         print("\nResponse:")
        #         print(response)  # Fallback if response is plain text
        #         return {"status": "success", "summary": summary}

    except VideoTranscriptError as e:
        logger.error(f"Transcript error: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    video_url = ""
    video_id = ""
    prompt = ""
    lang = ""
    result = main(video_url, video_id, prompt, lang)
    if result["status"] == "success":
        print("summary:", result["summary"])
    else:
        print("Error:", result["message"])