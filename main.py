# import our libraries 
from fastapi import FastAPI # our API framework
from fastapi.middleware.cors import CORSMiddleware 
import random # standard python random library

app = FastAPI() # this creates ours FastAPI application

# These are security settings. Don't worry about this too much. This means that multiple
# Web domains can access this API. 
origins = [
    "*",
    "http://localhost",
    "http://localhost:8080",
    "http:localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_origin_regex="https://.*\.herokuapp\.com'",
    allow_methods=["*"],
    allow_headers=["*"],
)

# Our Jokes "Database".
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
        "answer": "Nothing, it just waved."
    },
    {
        "question": "Where do boats go when they're sick?",
        "answer": "To the boat doc."
    },
    {
        "question": "Did you hear the rumor about butter?",
        "answer": "Well, I'm not going to spread it!"
    },
    {
        "question": "What kind of car does an egg drive?",
        "answer": "A yolkswagen."
    },
    {
        "question": "Why didn't the skeleton climb the mountain?",
        "answer": "It didn't have the guts."
    },
    {
        "question": "How many tickles does it take to make an octopus laugh?",
        "answer": "Ten tickles."
    },
    {
        "question": "Why did the math book look so sad?",
        "answer": "Because of all of its problems!"
    },
    {
        "question": "What do you call cheese that isn't yours?",
        "answer": "Nacho cheese."
    },
    {
        "question": "Where do math teachers go on vacation?",
        "answer": "Times Square."
    },
    {
        "question": "What does garlic do when it gets hot?",
        "answer": "It takes its cloves off."
    },
    {
        "question": "What's a robot's favorite snack?",
        "answer": "Computer chips."
    },
    {
        "question": "Why is Peter Pan always flying?",
        "answer": "He neverlands."
    },
    {
        "question": "Why are piggy banks so wise?",
        "answer": "They're filled with common cents."
    },
    {
        "question": "Can February March?",
        "answer": "No, but April May!"
    },
    {
        "question": "What's an astronaut's favorite part of a computer? ",
        "answer": "The space bar."
    },
    {
        "question": "Why are elevator jokes so classic and good?",
        "answer": "They work on many levels."
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