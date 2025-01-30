from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from youtube_video_summary_generator.services.pipeline import NoteGeneratorPipeline, VideoTranscriptError

# Initialize FastAPI Router
router = APIRouter()

# Initialize pipeline
pipeline = NoteGeneratorPipeline(doc_url="", video_id="", prompt="", lang="en")

class VideoInput(BaseModel):
    video_url: str

class FollowUpInput(BaseModel):
    summary: str
    follow_up: str

@router.get("/")
async def root():
    """
    API Root: Health check
    """
    return {"message": "YouTube Video Summary Generator API is running!"}

@router.post("/generate_summary")
async def generate_summary(request: VideoInput):
    """
    Generate a summary for a YouTube video given its URL.
    """
    try:
        docs = pipeline.load_docs_youtube_url(request.video_url)
        summary = pipeline.generate_summary(docs)
        return {"summary": summary}
    except VideoTranscriptError as e:
        raise HTTPException(status_code=400, detail=f"Transcript error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating summary: {str(e)}")


@router.post("/follow_up")
async def follow_up(request: FollowUpInput):
    """
    Generate a response to a follow-up question based on the summary.
    """
    try:
        response = pipeline.follow_up_query(request.summary, request.follow_up)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating follow-up response: {str(e)}")

@router.get("/suggest_questions")
async def suggest_questions():
    """
    Returns suggested follow-up questions.
    """
    questions = [
        "What are the key takeaways?",
        "Can you explain the main ideas?",
        "What insights can I derive from this?",
    ]
    return {"suggested_questions": questions}
