from fastapi import FastAPI
from llm import ask_llm
from typing import Literal
from pydantic import BaseModel
from database import get_connection
import bcrypt
import psycopg

app = FastAPI()

class UserRegistration(BaseModel):
    username: str
    password: str
    full_name: str
    email: str
    dob: str
    gender: str
    blood_type: str
    phone_number: str

class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class LLMRequest(BaseModel):
    messages: list[Message]

@app.get("/")
def home():
    return {"message": "DiagnosAI backend is running"}

@app.get("/test-db")
def test_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT version();")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "database": "connected",
        "version": result[0]
    }

@app.post("/register")
def register_user(user: UserRegistration):
    password_hash = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password_hash, full_name, email, dob, gender, blood_type, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(user.username, password_hash, user.full_name, user.email, user.dob, user.gender, user.blood_type, user.phone_number))
    conn.commit()
    cursor.close()
    conn.close()

    cursor.close()
    conn.close()
    
    return {
        "message": "Registration data received",
        "username": user.username
    }

@app.post("/ask")
def ask_ai(request: LLMRequest):
    messages = [
        {
            "role": "system",
            "content": """
You are an AI healthcare assistant for DiagnosAI.
Explain health-related information clearly.
Do not claim to provide a medical diagnosis.
Act as a professional healthcare assistant and provide accurate information based on the user's query.
Do not provide any medical advice or diagnosis.
Only give information based on the user's query and general health knowledge.
Keep it as simple and brief as possible, and avoid unnecessary details.
A ML model will be used to determine the user's health issue.
Do not assume that as the professional diagnosis.
Do not ask any follow-up questions to the user.
Only give information based on the mentioned query.
"""
        }
    ]

    messages.extend(request.messages)

    answer = ask_llm(messages)

    return {
        "answer": answer
    }