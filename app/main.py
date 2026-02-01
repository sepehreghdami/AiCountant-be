from fastapi import FastAPI
from app.dependencies import engine
from app.dependencies import Base, engine
from fastapi.middleware.cors import CORSMiddleware




Base.metadata.create_all(bind=engine)
# app = FastAPI()
# CORS Configuration - Development vs Production
# When deploying to production, uncomment the production settings below and comment out development settings

# DEVELOPMENT SETTINGS (currently active)
# /

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "https://fit.powerlandsport.ir",
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

