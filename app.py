from git import Repo, GitCommandError

# Chemin vers le répertoire git de ton projet
repo_path = '.'  # Utilise le répertoire racine du dépôt

try:
    # Ouvrir le dépôt Git
    repo = Repo(repo_path)

    # Obtenir le commit actuel (HEAD) de la branche locale
    current_commit = repo.head.commit

    # Effectuer un fetch pour récupérer les dernières données du serveur
    repo.remotes.origin.fetch()

    # Obtenir le commit de la branche 'origin/main'
    origin_main_commit = repo.commit('origin/main')

    # Comparer les deux commits
    if current_commit == origin_main_commit:
        print("Le commit actuel est le même que celui de 'origin/main'.")
    else:
        print("Le commit actuel est différent de celui de 'origin/main'.")
        print("fetch du depot")
        repo.remotes.origin.fetch()
        # Effectuer un pull pour mettre à jour la branche locale
        print("Mise à jour du dépôt...")

        repo.remotes.origin.pull()

        print("Mise à jour terminée.")

except GitCommandError as e:
    print(f"Erreur lors de l'exécution des commandes Git : {e}")
except Exception as e:
    print(f"Erreur : {e}")
