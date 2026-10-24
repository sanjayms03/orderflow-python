from orderflow.repositories.db import bootstrap
if __name__ == "__main__":
    bootstrap()
    print("Seeded local OrderFlow database")
