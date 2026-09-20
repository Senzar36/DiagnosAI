from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from llm import ask_llm
from pydantic import BaseModel
from database import get_connection
import bcrypt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserRegistration(BaseModel):
    username: str
    password: str
    full_name: str
    email: str
    dob: str
    gender: str
    blood_type: str
    phone_number: str

class LLMRequest(BaseModel):
    diagnosis: str

class UserLogin(BaseModel):
    username: str
    password: str

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
    
    return {
        "message": "Registration data received",
        "username": user.username
    }

@app.post("/login")
def login_user(user: UserLogin):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash FROM users WHERE username = %s",
        (user.username,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result is None:
        return {
            "message": "Invalid username or password"
        }

    password_hash = result[0]

    if bcrypt.checkpw(
        user.password.encode(),
        password_hash.encode()
    ):
        return {
            "message": "Login successful",
            "username": user.username
        }

    return {
        "message": "Invalid username or password"
    }

@app.post("/ask")
def ask_ai(request: LLMRequest):
    answer = ask_llm(request.diagnosis)

    return {
        "diagnosis": request.diagnosis,
        "explanation": answer
    }