# from fastapi import Depends, HTTPException, status
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from sqlalchemy.orm import Session
# from app.dependencies import get_db
# from app.utils.jwt_service import get_user_from_token
# from app.crud.auth import get_user_by_phone
# from typing import Optional
# import logging

# logger = logging.getLogger(__name__)

# security = HTTPBearer()

# def get_current_user(
#     credentials: HTTPAuthorizationCredentials = Depends(security),
#     db: Session = Depends(get_db)
# ):
#     """
#     Get the current authenticated user from JWT token.
    
#     Args:
#         credentials: HTTP Bearer token credentials
#         db: Database session
        
#     Returns:
#         User: The authenticated user
        
#     Raises:
#         HTTPException: If token is invalid or user not found
#     """
#     try:
#         # Extract token from credentials
#         token = credentials.credentials
        
#         # Get user info from token
#         user_info = get_user_from_token(token)
#         if not user_info:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="توکن نامعتبر است",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
        
#         # Get user from database
#         user = get_user_by_phone(db, user_info["phone_number"])
#         if not user:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="کاربر یافت نشد",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
        
#         # Check if user is verified
#         if not user.is_verified:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="حساب کاربری تأیید نشده است",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
        
#         logger.info(f"User authenticated: {user.id}")
#         return user
        
#     except HTTPException:
#         raise
#     except Exception as e:
#         logger.error(f"Authentication error: {str(e)}")
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="خطا در احراز هویت",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

# def get_current_user_optional(
#     credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
#     db: Session = Depends(get_db)
# ):
#     """
#     Get the current user if authenticated, otherwise return None.
#     This is useful for endpoints that work with both authenticated and anonymous users.
    
#     Args:
#         credentials: Optional HTTP Bearer token credentials
#         db: Database session
        
#     Returns:
#         Optional[User]: The authenticated user or None
#     """
#     try:
#         if not credentials:
#             return None
        
#         return get_current_user(credentials, db)
        
#     except HTTPException:
#         return None
#     except Exception as e:
#         logger.error(f"Optional authentication error: {str(e)}")
#         return None
