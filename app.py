import git
import time

def check_and_update_repo(repo_path):
    """
    Vérifie si de nouveaux commits sont présents dans le dépôt Git spécifié.
    Si oui, effectue un fetch et un pull.

    Args:
        repo_path (str): Chemin vers le répertoire racine du dépôt Git.
    """

    repo = git.Repo(repo_path)

    # Configurer le délai en secondes entre chaque vérification
    check_interval = 60  # 1 minute

    while True:
        try:
            origin = repo.remote(name='origin')
            origin.fetch()

            # Vérifier s'il y a des commits en attente à fusionner
            if repo.index.diff(None):
                repo.remotes.origin.pull()
                print(f"Nouveaux commits trouvés dans {repo_path}. Mise à jour effectuée.")
            else:
                print(f"Aucun nouveau commit dans {repo_path} à {time.strftime('%H:%M:%S')}.")
        except git.exc.GitCommandError as e:
            print(f"Erreur lors de la vérification du dépôt : {e}")

        time.sleep(check_interval)

# Remplacer 'chemin/vers/votre/repo' par le chemin réel de votre dépôt
repo_path = '.'
check_and_update_repo(repo_path)
