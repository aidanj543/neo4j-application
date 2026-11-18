from database import Neo4jDatabase

def main():
    db = None

    try:
        db = Neo4jDatabase()
        db.connect()

    except Exception as e:
        print(f"Database connection failed: {e}")

    finally:
        if db is not None:
            db.close()

if __name__ == "__main__":
    main()