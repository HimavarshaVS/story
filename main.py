from fastapi import FastAPI

from app.Gemini import get_story

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/story")
async def tell_story(prompt: str):
    """Handles user input and returns a corresponding story."""
    story = get_story(prompt.lower())
    return story.text
