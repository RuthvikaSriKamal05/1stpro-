from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    name: str
    age: int
    course: str

@app.get("/")
def home():
    return {"message": "Student API Running"}

@app.post("/add-student")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully"}

@app.get("/get-students")
def get_students():
    return students
