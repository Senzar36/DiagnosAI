from fastapi import FastAPI
from pydantic import BaseModel
from database import get_connection

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
    return {
        "message": "Registration data received",
        "username": user.username
    }