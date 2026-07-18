from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanRequest(BaseModel):
    age: int
    income: int
    loan_amount: int
    employment_status: str

@app.post("/loan")
async def predict_loan(Application:LoanRequest):
    decision = "accept"
    if Application.age<18:
        decision = "reject"

    if Application.income<10000:
        decision = "reject"

    return{
        decision:decision
    }