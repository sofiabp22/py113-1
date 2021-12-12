# import our libraries 
from fastapi import FastAPI # our API framework
import random # standard python random library

app = FastAPI() # this creates ours FastAPI application

JOKES = [
    {
       "question": "Where do fruits go on vacation?",
        "answer": "Pear-is!"
    },
    {
        "question": "What do you call a fish wearing a bowtie?",
        "answer": "Sofishticated."
    },
    {
        "question": "What did the ocean say to the beach?",
        "answer:": "Nothing, it just waved."
    }
]


# this defines our root endpoint
@app.get("/")
async def root():
    return {"message": "This is a jokes API"}

# this endpoint returns a random joke
@app.get("/random") 
async def random_joke():
    return random.choice(JOKES)


@app.get("/joke-of-the-year") 
async def joke_of_the_year():
    return JOKES[0]

@app.get("/all-jokes") 
async def all_jokes():
    return JOKES