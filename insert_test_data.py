import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Testdaten einfügen
cursor.execute("INSERT INTO information (title, content, category, source, date, tags, relevance, author, language) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
               ("Warum sind Bananen krumm?", "Bananen wachsen zur Sonne hin, was ihre gekrümmte Form verursacht. Sie sind reich an Kalium und Vitaminen.", "Ernährung", "Wikipedia", "2024-01-01", "Bananen, Obst, Ernährung", 3, "Dr. Obst", "DE"))
cursor.execute("INSERT INTO information (title, content, category, source, date, tags, relevance, author, language) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
               ("Wahljahr 2024: Wichtige Parteien und Programme", "Die Bundestagswahl 2024 steht bevor. Hier sind die wichtigsten Parteien und ihre Positionen zu Klima und Wirtschaft.", "Politik", "Bundeszentrale für politische Bildung", "2024-05-10", "Wahl, Politik, Deutschland", 5, "Politik Heute", "DE"))
cursor.execute("INSERT INTO information (title, content, category, source, date, tags, relevance, author, language) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
               ("Klimawandel und seine Auswirkungen auf die Welt", "Der Klimawandel führt zu extremeren Wetterbedingungen und bedroht zahlreiche Ökosysteme.", "Umwelt", "Umweltbundesamt", "2023-11-01", "Klimawandel, Umwelt, Ökologie", 4, "Dr. Grün", "DE"))

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
