from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow

app = FastAPI()

# Replace with your Google OAuth credentials
CLIENT_SECRETS_FILE = "client_secrets.json"
SCOPES = ["https://www.googleapis.com/auth/userinfo.profile"]
flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, redirect_uri="http://localhost:8000/callback")

@app.get("/login")
def login():
    auth_url, _ = flow.authorization_url()
    return RedirectResponse(auth_url)

@app.get("/callback")
def callback(request: Request):
    flow.fetch_token(authorization_response=str(request.url))
    credentials = flow.credentials
    return {"message": "Login successful"}
