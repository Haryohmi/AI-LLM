import logging
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.summarize.chain import load_summarize_chain
from langchain.schema import StrOutputParser, AIMessage

# Configure Logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class VideoTranscriptError(Exception):
    """Custom exception for video transcript loading errors."""

    def __init__(self, message, youtube_url):
        self.message = message
        self.youtube_url = youtube_url
        super().__init__(self.message)


class NoteGeneratorPipeline:
    def __init__(self, doc_url: str, video_id: str, prompt: str, lang: str):
        self.doc_url = doc_url
        self.video_id = video_id
        self.prompt = prompt
        self.lang = lang
        self.model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
        self.embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.vectorstore = None
        self.retriever = None
        self.cache = {}

        # Output parser ensures only string responses
        self.output_parser = StrOutputParser()

    def parse_response(self, raw_response):
        """Extracts only the meaningful string content from the LLM response."""
        return self.output_parser.parse(raw_response)

    def load_docs_youtube_url(self, youtube_url: str, verbose=True) -> List[Document]:
        """
        Load and split YouTube video transcripts into chunks.
        """
        try:
            loader = YoutubeLoader.from_youtube_url(youtube_url, add_video_info=False)
            docs = loader.load()
        except Exception as e:
            logger.error(f"Failed to load video transcript from {youtube_url}: {e}")
            raise VideoTranscriptError("Failed to load video transcript", youtube_url) from e

        if verbose:
            logger.info("Video transcript loaded successfully.")
            logger.info("Splitting transcript into chunks.")

        splitter = RecursiveCharacterTextSplitter()
        split_docs = splitter.split_documents(docs)
        return split_docs

    def generate_summary(self, docs: List[Document]) -> str:
        """
        Generate a summary using the video transcript.
        """
        if not docs:
            return "No transcript data available."

        try:
            # Summarization logic
            summarize_chain = load_summarize_chain(self.model, chain_type="map_reduce")
            prompt_template = f"Summarize the content focusing on '{self.prompt}'. Language: {self.lang}"
            summary = summarize_chain.run({"input_documents": docs, "question": prompt_template})
            return summary
        except Exception as e:
            logger.error(f"Error during summarization: {e}")
            return "Failed to generate summary."

    def follow_up_query(self, summary: str, follow_up: str) -> str:
        """
        Generate a response to a follow-up question.
        """
        if not summary.strip():
            return "No summary available. Please generate a summary first."
        if not follow_up.strip():
            return "No follow-up question provided."

        # Generate cache key
        cache_key = f"{summary}-{follow_up}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        try:
            refined_prompt = f"Summary:\n{summary}\n\nFollow-Up Question: {follow_up}"
            raw_response = self.model.invoke([f"Answer the question based on the summary: {refined_prompt}"])

            # Handle response as AIMessage
            if isinstance(raw_response, AIMessage):
                content = raw_response.content.strip()
            elif isinstance(raw_response, str):
                content = raw_response.strip()
            else:
                return "Unexpected response format."

            if not content:
                return "The question was unclear. Try being more specific."

            # Cache the response
            self.cache[cache_key] = content
            return content
        except Exception as e:
            logger.error(f"Error generating follow-up response: {e}")
            return "Failed to generate a response."
