from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Clahan Bank Transactions Service",
    version="1.0.0",
    description="Transactions and ledger processing microservice for the Clahan-Bank banking platform.",
)


class Transaction(BaseModel):
    transaction_id: str = Field(..., example="TX-9001")
    account_id: str = Field(..., example="SV-1001")
    transaction_type: str = Field(..., example="credit")
    amount: float = Field(..., gt=0)
    description: str = Field(..., example="Salary deposit")
    status: str = "posted"


transactions_db = [
    Transaction(
        transaction_id="TX-9001",
        account_id="SV-1001",
        transaction_type="credit",
        amount=48000.0,
        description="Salary deposit",
        status="posted",
    ),
    Transaction(
        transaction_id="TX-9002",
        account_id="CR-2001",
        transaction_type="debit",
        amount=16000.0,
        description="Vendor payment",
        status="posted",
    ),
]


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "transactions"}


@app.get("/transactions")
def list_transactions():
    return {"transactions": transactions_db}


@app.post("/transactions")
def create_transaction(transaction: Transaction):
    transactions_db.append(transaction)
    return {"message": "Transaction recorded successfully", "transaction": transaction}
