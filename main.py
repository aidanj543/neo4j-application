from database import Neo4jDatabase
from seed import seed_database


def main():
    db = None

    try:
        db = Neo4jDatabase()
        db.connect()

        seed_database(db.driver)

    except Exception as error:
        print(f"Application error: {error}")

    finally:
        if db is not None:
            db.close()


if __name__ == "__main__":
    main()
