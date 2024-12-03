from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from mangum import Mangum  # For AWS Lambda support

# Initialize FastAPI app
app = FastAPI()

# Request model
class OnboardingRequest(BaseModel):
    email: EmailStr
    company_name: str
    company_address: str
    contact_no: str
    pincode: str

# Handlers
@app.post("/onboard")
async def onboard_user(onboarding_request: OnboardingRequest):
    # Add logic to save data to a database or other processing here.
    # For now, returning success with the submitted data.
    return {
        "message": "Onboarding successful!",
        "data": onboarding_request.dict()
    }

# Lambda handler
handler = Mangum(app)
