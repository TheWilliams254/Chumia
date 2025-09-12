# import base64
# import httpx
# from datetime import datetime
# from app.core.config import settings

# MPESA_BASE_URL = "https://sandbox.safaricom.co.ke"  # use live URL in production


# async def get_mpesa_access_token() -> str:
#     """
#     Get M-Pesa access token using Consumer Key and Secret
#     """
#     consumer_key = settings.MPESA_CONSUMER_KEY
#     consumer_secret = settings.MPESA_CONSUMER_SECRET
#     auth_string = f"{consumer_key}:{consumer_secret}"
#     encoded = base64.b64encode(auth_string.encode()).decode()

#     url = f"{MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"

#     async with httpx.AsyncClient() as client:
#         response = await client.get(
#             url, headers={"Authorization": f"Basic {encoded}"}
#         )
#         response.raise_for_status()
#         data = response.json()
#         return data["access_token"]


# async def initiate_stk_push(phone_number: str, amount: int, account_reference="OrderPayment", transaction_desc="Payment") -> dict:
#     """
#     Initiates an STK Push payment request
#     """
#     access_token = await get_mpesa_access_token()

#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     password_str = f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}"
#     password = base64.b64encode(password_str.encode()).decode()

#     url = f"{MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest"

#     payload = {
#         "BusinessShortCode": settings.MPESA_SHORTCODE,
#         "Password": password,
#         "Timestamp": timestamp,
#         "TransactionType": "CustomerPayBillOnline",
#         "Amount": amount,
#         "PartyA": phone_number,   # Customer phone number
#         "PartyB": settings.MPESA_SHORTCODE,
#         "PhoneNumber": phone_number,
#         "CallBackURL": settings.MPESA_CALLBACK_URL,
#         "AccountReference": account_reference,
#         "TransactionDesc": transaction_desc,
#     }

#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             url,
#             headers={"Authorization": f"Bearer {access_token}"},
#             json=payload,
#         )
#         response.raise_for_status()
#         return response.json()
