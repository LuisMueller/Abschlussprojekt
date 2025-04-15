#!/bin/bash

echo "Neues virtuelles Environment mit Python 3.11 wird erstellt..."

# Prüfen ob python3.11 existiert
if ! command -v python3.11 &> /dev/null
then
    echo "Python 3.11 ist nicht installiert. Bitte zuerst mit 'brew install python@3.11' installieren."
    exit 1
fi

# Venv neu erstellen
rm -rf venv
python3.11 -m venv venv

# Venv aktivieren
source venv/bin/activate

# Pakete installieren
echo "Installiere benötigte Pakete..."
pip install --upgrade pip
pip install fastapi uvicorn psycopg2 python-dotenv

# Test
echo "Alles installiert. Aktive Python-Version:"
python --version

echo "Du kannst jetzt starten mit:"
echo "    source venv/bin/activate"
echo "    uvicorn Backend.main:app --reload"


#Starten mit dem Befehl ./setup.sh im IDE Terminal