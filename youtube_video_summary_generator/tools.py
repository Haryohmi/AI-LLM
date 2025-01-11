import logging
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.summarize.chain import load_summarize_chain

# Configure Logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


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
        #self.prompt = input("Please write your question: ").strip() #update to suggest some questions
        self.lang = lang
        self.model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")  # Initialize LLM
        self.embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # Initialize embeddings
        self.vectorstore = None
        self.retriever = None

    def load_docs_youtube_url(self, youtube_url: str, verbose=True) -> List[Document]:
        """
        Load and split YouTube video transcripts into manageable chunks.
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

        # Split documents into manageable parts
        splitter = RecursiveCharacterTextSplitter()
        split_docs = splitter.split_documents(docs)
        return split_docs

    def generate_summary(self, docs: List[Document]) -> str:
        """
        Generate a summary using the video transcript and a prompt.
        """
        if not docs and not self.prompt:
            return "No documents or text content provided."

        doc_summary = ""
        if docs:
            # Build a vector store and perform summarization
            try:
                self.vectorstore = Chroma.from_documents(docs, self.embedding_model)
                self.retriever = self.vectorstore.as_retriever()

                summarize_chain = load_summarize_chain(self.model, chain_type="map_reduce")
                prompt_template = f"Summarize the content focusing on '{self.prompt}'. Language: {self.lang}"
                doc_summary = summarize_chain.run({"input_documents": docs, "question": prompt_template})
            except Exception as e:
                logger.error(f"Error during document summarization: {e}")
                doc_summary = "Failed to summarize the documents."

        text_summary = ""
        if self.prompt and not docs:
            try:
                logger.info(f"No Video link provided. Summarizing text directly using the prompt: {self.prompt}")
                text_summary = self.model.invoke(
                    [f"Summarize this text focusing on '{self.prompt}'. Language: {self.lang}"]
                )
            except Exception as e:
                logger.error(f"Error during LLM invocation: {e}")
                text_summary = "Failed to generate a summary using the prompt."

        # Combine summaries
        return doc_summary or text_summary or "No content to summarize."
        

