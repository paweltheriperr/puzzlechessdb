# Użyj obrazu Pythona jako podstawy
FROM python:3.9-slim-buster

# Ustaw katalog roboczy na /app
WORKDIR /puzzlechessdb

# Skopiuj plik requirements.txt do katalogu roboczego
COPY requirements.txt .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę plików do katalogu roboczego
COPY . .

# Uruchom aplikację
CMD [ "python", "./puzzlechessdb.py" ]