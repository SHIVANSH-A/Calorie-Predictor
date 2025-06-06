from fastapi import FastAPI, Form, Request, Depends
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
import pickle
import pandas as pd

load_dotenv()

# Get the path from .env
pickle_path = os.getenv("PICKLE_PATH")
app = FastAPI()


with open("pickle_path", "rb") as f:
    pipeline = pickle.load(f)


templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(
    request: Request,
    Gender: str = Form(...),
    Age: float = Form(...),
    Height: float = Form(...),
    Weight: float = Form(...),
    Duration: float = Form(...),
    Heart_Rate: float = Form(...),
    Body_Temp: float = Form(...)
):
    sample = pd.DataFrame({
        "Gender": [Gender],
        "Age": [Age],
        "Height": [Height],
        "Weight": [Weight],
        "Duration": [Duration],
        "Heart_Rate": [Heart_Rate],
        "Body_Temp": [Body_Temp]
    }, index=[0])

    result = pipeline.predict(sample)[0]
    
    return templates.TemplateResponse("result.html", {"request": request, "calories": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)