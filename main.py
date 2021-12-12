# import our libraries 
from fastapi import FastAPI # our API framework
import random # standard python random library

app = FastAPI() # this creates ours FastAPI application

# this defines our root endpoint
@app.get("/")
async def root():
    return {"message": "This is a jokes API"}

# this endpoint returns a random joke
@app.get("/random") 
async def random_joke():
    jokes = [
        {
            "question": "What do you call a fish wearing a bowtie?",
            "answer": "Sofishticated."
        },
        {
            "question": "What did the ocean say to the beach?",
            "answer:": "Nothing, it just waved."
        }
    ]
    return random.choice(jokes)


@app.get("/joke-of-the-year") 
async def joke_of_the_year():
    joke = {
            "question": "Where do fruits go on vacation?",
            "answer": "Pear-is!"
        }
    return joke

    