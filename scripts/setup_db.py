from lib.db.connection import initialize_database
from lib.db.seed import seed_database

def main():
    print("Setting up database...")
    initialize_database()
    seed_database()
    print("Database setup complete!")

if __name__ == "__main__":
    main()