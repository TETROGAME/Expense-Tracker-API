from pathlib import Path

from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "data" / "db.sqlite"


def main():
    engine = create_engine(url=f"sqlite:///{DB_DIR}", echo=True)


if __name__ == "__main__":
    main()
