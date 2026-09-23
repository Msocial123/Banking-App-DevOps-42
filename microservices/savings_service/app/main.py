from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Clahan Bank Savings Service",
    version="1.0.0",
    description="Savings account microservice for the Clahan-Bank digital banking platform.",
)


class SavingsAccount(BaseModel):
    account_id: str = Field(..., example="SV-1001")
    customer_id: str = Field(..., example="CUST-001")
    balance: float = Field(default=0.0, ge=0)
    interest_rate: float = Field(default=4.5, ge=0)
    status: str = "active"
    account_type: str = "Savings"


accounts_db = [
    SavingsAccount(
        account_id="SV-1001",
        customer_id="CUST-001",
        balance=24560.0,
        interest_rate=4.5,
        status="active",
    ),
    SavingsAccount(
        account_id="SV-1002",
        customer_id="CUST-002",
        balance=120000.0,
        interest_rate=4.8,
        status="active",
    ),
]


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "savings"}


@app.get("/accounts")
def list_accounts():
    return {"accounts": accounts_db}


@app.post("/accounts")
def create_account(account: SavingsAccount):
    accounts_db.append(account)
    return {"message": "Savings account created successfully", "account": account}
