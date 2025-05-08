from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

class Contact(BaseModel):
    name: str
    email: str

contact = Contact(name="Matej", email="fotbalistarb@seznam.cz")

file = Path("memory.json")
if not file.exists():
    file.write_text("[]", encoding="utf-8")

contacts = json.loads(file.read_text(encoding="utf-8"))

if contact.dict() not in contacts:
    contacts.append(contact.dict())
    file.write_text(json.dumps(contacts, indent=4), encoding="utf-8")

@app.get("/")
def root():
    return {"contact": contact}

@app.get("/contacts")
def get_all_contacts():
    return contacts