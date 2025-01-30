# 🚀 YouTube Video Summary Generator

## 📌 Project Overview
The **YouTube Video Summary Generator** is an AI-powered application that extracts transcripts from YouTube videos, generates structured summaries, and allows users to ask follow-up questions for deeper insights.

### 🌟 Features:
✅ **Extracts YouTube video transcripts**  
✅ **Generates AI-powered summaries**  
✅ **Handles dynamic follow-up questions**  
✅ **Provides suggested follow-up questions for engagement**  
✅ **FastAPI-powered backend with real-time API responses**  

---

## 🛠 Technologies Used
| **Technology**       | **Purpose** |
|----------------------|------------|
| **FastAPI**         | High-performance backend for API development |
| **Uvicorn**         | ASGI server for running the FastAPI app |
| **LangChain**       | AI-driven text processing and summarization |
| **YouTubeTranscriptAPI** | Extracts transcripts from YouTube videos |
| **Google Generative AI** | AI language model for summary generation |
| **ChromaDB**        | Vector-based document retrieval |
| **HTML, JavaScript** | Frontend API interaction |

---

## 📂 Folder Structure
AI-LLM/


│── frontend/                                                         # Frontend module                     


│── youtube_video_summary_generator/                                   # Backend module

                           
│── requirements.txt                                                   # Dependencies


│── README.md                                                          # Project documentation

---

## 🚀 API Endpoints
| Method  | Endpoint             | Description                                      |
|---------|----------------------|--------------------------------------------------|
| `GET`   | `/`                  | Health check (API status)                        |
| `POST`  | `/generate_summary`   | Generates a summary from a YouTube video URL    |
| `POST`  | `/follow_up`          | Provides AI-generated responses based on summary |
| `GET`   | `/suggest_questions`  | Returns suggested follow-up questions           |

---

## 📌 How It Works
1️⃣ User **enters a YouTube URL**  
2️⃣ The backend **fetches transcript & generates summary**  
3️⃣ **Suggested follow-up questions** appear  
4️⃣ User **asks follow-up questions**  
5️⃣ AI **responds with insightful answers**  

🔹 **Perfect for students, researchers, and professionals seeking quick insights from video content.**

---

## 🌍 Future Enhancements
🔜 **Upcoming Features:**
- 🌍 **Multilingual Transcript Summarization**  
- 🎥 **Video Preview & Summary Overlay in UI**  
- 🔄 **AI-Powered Q&A with Context Retention**  

---

The **YouTube Video Summary Generator** showcases **FastAPI, AI-driven text processing, and real-time API handling**—making it a valuable tool for anyone seeking quick insights from videos.  

Would you like to integrate it into your own project or workflow? 🚀**  

🙌 **Contributors Welcome!** 🎉
