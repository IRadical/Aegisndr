import uvicorn
from app.db.base import Base
from app.db.session import engine
from app.api.main import app

def init_db():
    print("Initializing database tables...")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)