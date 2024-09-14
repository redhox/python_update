import git
import docker
import time

def update_and_restart(repo_path):
    """
    Args:
        repo_path (str): Chemin vers le répertoire racine du dépôt Git.
        docker_compose_file (str): Chemin vers le fichier docker-compose.yml.
    """

    repo = git.Repo(repo_path)

    while True:
        try:
            origin = repo.remote(name='origin')
            origin.fetch()
            repo.remotes.origin.pull()
            print("Dépôt mis à jour.")
            
        except:
            print("wait 60s")
            time.sleep(60)  # Attendre 60 secondes avant la prochaine vérification
        print("wait 60s")

        time.sleep(60)  # Attendre 60 secondes avant la prochaine vérification

# Remplacer par les chemins de votre dépôt et de votre fichier docker-compose
repo_path = "/.git"
print("start")
update_and_restart(repo_path)
