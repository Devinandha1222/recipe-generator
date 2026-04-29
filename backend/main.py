from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/generate")
def generate_recipe(ingredient: str):
    prompt = f"""
You are a professional chef and culinary expert.

Your task is to generate a clear, practical, and well-structured recipe using the ingredient: {ingredient}.

Follow these rules strictly:

1. Provide a creative recipe name.
2. List all ingredients with exact measurements.
3. Include preparation time and cooking time.
4. Give step-by-step cooking instructions (numbered).
5. Ensure the recipe is simple and can be made at home.
6. Avoid unnecessary explanations or storytelling.
7. Keep the recipe concise but complete.
8. If the ingredient is unusual, adapt creatively but logically.

Output format:

Recipe Name: <name>

Ingredients:
- item 1 with quantity
- item 2 with quantity

Preparation Time: <time>
Cooking Time: <time>

Instructions:
1. Step one
2. Step two
3. Step three

Optional: Tips:
- useful cooking tip
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return {"recipe": response.text}