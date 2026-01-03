from fastapi import FastAPI
import uvicorn

from app.controllers.contact_controller import contactRouter as contact_router
from app.controllers.donateController import router as donate_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="NGO Backend")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500","http://127.0.0.1:5501",["*"]],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)


app.include_router(contact_router)
app.include_router(donate_router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
