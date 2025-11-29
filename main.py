from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Car Backend is running!"}

@app.post("/analyze")
def analyze(data: dict):
    car_model = data.get("car_model")
    km = data.get("km")
    style = data.get("style")

    return {
        "car_model": car_model,
        "km": km,
        "style": style,
        "advice": "Proveri ulje i filtere. Uskoro zameni gume ako voziš sportski stil."
    }
