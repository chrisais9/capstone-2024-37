import database.repo
import util
from database import User


async def get_user_in_db(google_email: str) -> dict:
    current_user = await database.repo.find_user_by_google_email(google_email)
    return current_user


async def get_user_in_token(token) -> dict:
    return await util.decode_token(token)

async def get_clientid_in_jwt(token) -> dict:
    decoded_jwt = await util.decode_token(token)
    return decoded_jwt['client_id']


