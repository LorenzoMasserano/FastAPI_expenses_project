import auth.service as auth_service
from auth.schemas import TokenResponse
from config import settings

def refresh_token(refresh_token: str) -> TokenResponse:

    credential_id = auth_service.verify_token_validity(token= refresh_token, secret_key=settings.SECRET_KEY)

    tokens = auth_service.generate_jwt(credential_id= credential_id, secret_key=settings.SECRET_KEY)

    return TokenResponse(
        token= tokens[auth_service.TokenType.ACCESS],
        refresh_token= tokens[auth_service.TokenType.REFRESH]
    ) 
