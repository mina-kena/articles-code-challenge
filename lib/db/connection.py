import sqlite3
import os

def get_connection():
    
    db_path = 'articles.db'
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  
    return conn

def initialize_database():
    
    conn = get_connection()
    cursor = conn.cursor()