import sqlite3
import csv

# Verbindung zur bestehenden Datenbank
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# CSV-Datei mit externen Daten laden und in die `information`-Tabelle einfügen
def import_csv_to_db(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Prüfen, ob der Titel bereits existiert
            cursor.execute("SELECT COUNT(1) FROM information WHERE title = ?", (row["title"],))
            if cursor.fetchone()[0] == 0:  # Eintrag nur hinzufügen, wenn er nicht existiert
                cursor.execute("""
                    INSERT INTO information (title, content, category, source, date, tags, relevance, author, language)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, 
                    (row["title"], row["content"], row["category"], row["source"], row["date"], 
                     row["tags"], row["relevance"], row["author"], row["language"]))
    conn.commit()

# Beispielaufruf mit einer Datei 'external_data.csv'
import_csv_to_db("external_data.csv")

# Verbindung schließen
conn.close()
