from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from firebase_admin import auth as firebase_auth
from firebase_admin._auth_utils import InvalidIdTokenError

class FirebaseAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/public"):
            return await call_next(request)

        auth_header = request.headers.get("authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Authorization header missing or malformed"})

        token = auth_header.split("Bearer ")[1]

        try:
            decoded_token = firebase_auth.verify_id_token(token)
            request.state.user = decoded_token
        except InvalidIdTokenError:
            return JSONResponse(status_code=401, content={"detail": "Token inválido"})
        except Exception:
            return JSONResponse(status_code=401, content={"detail": "Error al verificar el token"})

        return await call_next(request)
