from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.auth import router as auth_router
from app.api.admin import router as admin
from app.api.product import router as product_router
from app.api.media import router as media_router
from app.api.order import router as order_router
from app.api.payment import router as payment_router
from app.api.mpesa import router as  mpesa_router
from app.models import * 

import os
from dotenv import load_dotenv

load_dotenv()

from app.utils.email_util import send_email  

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL",)], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is working! Welcome to Chumia"}

@app.get("/test-email")
async def test_email():
    try:
        await send_email(
            subject="Chumia Test Email",
            body="Hello, this is a test email from your FastAPI backend.",
            email_to=os.getenv("TEST_RECEIVER_EMAIL", "test@example.com")
        )
        return {"status": "Email sent successfully"}
    except Exception as e:
        return {"error": str(e)}
    
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(admin)
app.include_router(product_router)
app.include_router(media_router)
app.include_router(order_router)
app.include_router(payment_router)
app.include_router(mpesa_router)