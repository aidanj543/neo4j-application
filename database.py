import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

class Neo4jDatabase:
    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        username = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")

        if not all([uri, username, password]):
            raise ValueError("Connection settings are missing")

        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def connect(self):
        self.driver.verify_connectivity()
        print("Successfully connected to Neo4j")

    def close(self):
        self.driver.close()