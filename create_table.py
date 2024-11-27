import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Tabelle erstellen, falls sie nicht existiert
cursor.execute("""
CREATE TABLE IF NOT EXISTS information (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
""")

# Beispielinhalt hinzufügen (optional)
cursor.execute("INSERT INTO information (title, content) VALUES (?, ?)", 
               ("Bananen", "Bananen sind krumm, weil ..."))
cursor.execute("INSERT INTO information (title, content) VALUES (?, ?)", 
               ("Veganismus ungesund?", "Hier sind wissenschaftliche Fakten über Veganismus..."))

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
