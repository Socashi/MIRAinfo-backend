import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Haupttabelle information erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS information (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    category TEXT,
    source TEXT,
    date TEXT,
    tags TEXT,
    relevance INTEGER,
    author TEXT,
    language TEXT
);
""")

# Optionale Tabelle sources erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS sources (
    source_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    url TEXT,
    type TEXT
);
""")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
