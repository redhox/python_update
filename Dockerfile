# Spécifie l'image de base à partir de laquelle nous allons construire
FROM python:3.9

# Définit le répertoire de travail dans le conteneur
WORKDIR /app
RUN apt update && apt install git -y
# Copie le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt requirements.txt

# Installe les dépendances listées dans requirements.txt
RUN pip install -r requirements.txt

# Copie le reste du code source dans le répertoire de travail
COPY . .

# Spécifie la commande à exécuter lorsque le conteneur démarre
CMD ["python", "app.py"]
