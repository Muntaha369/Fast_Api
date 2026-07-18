from fastapi import FastAPI

app = FastAPI()

users = [
    {"name": "Alice", "age": 25, "country": "USA", "gender": "Female"},
    {"name": "Bob", "age": 30, "country": "Canada", "gender": "Male"},
    {"name": "Charlie", "age": 22, "country": "UK", "gender": "Male"},
    {"name": "Diana", "age": 28, "country": "Australia", "gender": "Female"},
    {"name": "Ethan", "age": 35, "country": "Germany", "gender": "Male"},
    {"name": "Fiona", "age": 27, "country": "France", "gender": "Female"},
    {"name": "George", "age": 31, "country": "India", "gender": "Male"},
    {"name": "Hannah", "age": 24, "country": "Japan", "gender": "Female"},
    {"name": "Ian", "age": 29, "country": "Brazil", "gender": "Male"},
    {"name": "Julia", "age": 26, "country": "South Africa", "gender": "Female"},
]

@app.get("/get_users")
async def FilterCustomer(gender:str, country:str):

    result = []
    for u in users:
        if u["country"] == country and u["gender"] == gender:
            result.append(u)

    return{
        "country":country,
        "gender":gender,
        "res":result
    }