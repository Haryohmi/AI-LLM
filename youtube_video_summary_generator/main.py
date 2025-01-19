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
        print(f"status: success, Generated summary: {summary}")
    
        # Interactive follow-up loop
        while True:
            print("\nSuggested Questions:")
            print("1. What are the key takeaways?")
            print("2. Can you explain the main ideas?")
            print("3. What insights can I derive from this?")
            print("Type 'exit' to quit.")
            
            follow_up = input("\nEnter your follow-up question: ").strip()
            if follow_up.lower() == "exit":
                print("Thank you for using the Note Generator. Goodbye!")
                break

            # Generate follow-up response
            follow_up_response = pipeline.follow_up_query(summary, follow_up)
            print(f"\nResponse: {follow_up_response}")
            #print(f"\nResponse: {follow_up_response['content']}")

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
        if result["follow_up_response"]:
            print("follow_up_response:", result["follow_up_response"])
    else:
        print("Error:", result["message"])