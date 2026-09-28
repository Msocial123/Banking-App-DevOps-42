from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Clahan Bank Current Service",
    version="1.0.0",
    description="Current account microservice for businesses and high-frequency banking users.",
)


class CurrentAccount(BaseModel):
    account_id: str = Field(..., example="CR-2001")
    customer_id: str = Field(..., example="BUS-010")
    balance: float = Field(default=0.0, ge=0)
    overdraft_limit: float = Field(default=50000.0, ge=0)
    status: str = "active"
    account_type: str = "Current"


accounts_db = [
    CurrentAccount(
        account_id="CR-2001",
        customer_id="BUS-010",
        balance=350000.0,
        overdraft_limit=50000.0,
        status="active",
    ),
    CurrentAccount(
        account_id="CR-2002",
        customer_id="BUS-011",
        balance=775000.0,
        overdraft_limit=75000.0,
        status="active",
    ),
]


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "current"}


@app.get("/accounts")
def list_accounts():
    return {"accounts": accounts_db}


@app.post("/accounts")
def create_account(account: CurrentAccount):
    accounts_db.append(account)
    return {"message": "Current account created successfully", "account": account}
