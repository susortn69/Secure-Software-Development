
# manage.py
from sqlalchemy import inspect
from app import create_app, db
from app import models  # ensure models are imported

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        insp = inspect(db.engine)
        tables = insp.get_table_names()
        print("Database initialized. Tables:", tables)
        # bonus: skriv ut kolonner for rapporten
        for t in tables:
            cols = [c["name"] for c in insp.get_columns(t)]
            print(f" - {t}: {', '.join(cols)}")
