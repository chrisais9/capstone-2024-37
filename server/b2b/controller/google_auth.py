import requests
from fastapi import APIRouter
from fastapi import HTTPException, status
from starlette.responses import RedirectResponse

from database import User
from database.repo import find_user_by_google_email
from setting import setting

auth_google_router = APIRouter()

@auth_google_router.get("/google-login")
async def google_login():
    url = (
        "https://accounts.google.com/o/oauth2/auth"
        "?response_type=code"
        f"&client_id={setting.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={setting.REDIRECT_URI}"
        "&scope=openid%20email%20profile"
    )
    return RedirectResponse(url)


@auth_google_router.get("/auth/google", response_model=User)
async def auth_google(code: str):
    token_data = {
        "code": code,
        "client_id": setting.GOOGLE_CLIENT_ID,
        "client_secret": setting.GOOGLE_CLIENT_SECRET,
        "redirect_uri": setting.REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    response = requests.post(setting.GOOGLE_TOKEN_ENDPOINT, data=token_data)
    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to exchange authorization code for tokens",
        )

    token_response = response.json()
    access_token = token_response.get("access_token")

    profile_response = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_data = profile_response.json()
    google_email = profile_data['email']

    return await find_user_by_google_email(google_email)