from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {
    1: {"name": "Alice", "age": 25, "country": "USA", "gender": "Female"},
    2: {"name": "Bob", "age": 30, "country": "Canada", "gender": "Male"},
    3: {"name": "Charlie", "age": 22, "country": "UK", "gender": "Male"},
    4: {"name": "Diana", "age": 28, "country": "Australia", "gender": "Female"},
    5: {"name": "Ethan", "age": 35, "country": "Germany", "gender": "Male"},
    6: {"name": "Fiona", "age": 27, "country": "France", "gender": "Female"},
    7: {"name": "George", "age": 31, "country": "India", "gender": "Male"},
    8: {"name": "Hannah", "age": 24, "country": "Japan", "gender": "Female"},
    9: {"name": "Ian", "age": 29, "country": "Brazil", "gender": "Male"},
    10: {"name": "Julia", "age": 26, "country": "South Africa", "gender": "Female"},
}

@app.get("/users/{customer_id}")
async def get_customer(customer_id:int):
    if customer_id not in users:
        raise HTTPException(
            status_code = 404,
            detail = f"{customer_id} does not exist"
        )

    return{
        "res":users[customer_id]
    }