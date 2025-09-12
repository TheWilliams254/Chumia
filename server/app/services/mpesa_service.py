import base64, requests
from datetime import datetime
from app.core.config import settings

def get_mpesa_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET))
    response.raise_for_status()
    return response.json()["access_token"]

def lipa_na_mpesa(phone_number: str, amount: float, account_reference: str, transaction_desc: str):
    access_token = get_mpesa_access_token()

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode((settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode()).decode("utf-8")

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),
        "PartyA": phone_number,      # Customer's phone number
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc
    }

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post("https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest", json=payload, headers=headers)
    response.raise_for_status()
    return response.json()
