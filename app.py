from git import Repo, GitCommandError

# Chemin vers le répertoire git de ton projet
repo_path = '.git'

# Ouvrir le dépôt Git
repo = Repo(repo_path)

# Obtenir le commit actuel (HEAD) de la branche locale
current_commit = repo.head.commit

# Obtenir le commit de la branche `origin/main`
origin_main_commit = repo.commit('origin/main')

# Comparer les deux commits
if current_commit == origin_main_commit:
    print("Le commit actuel est le même que celui de 'origin/main'.")
else:
    print("Le commit actuel est différent de celui de 'origin/main'.")
    
    try:
        # Faire un fetch pour récupérer les dernières modifications
        repo.remotes.origin.fetch()
        print("Fetch terminé avec succès.")

        # Faire un pull pour mettre à jour la branche locale
        repo.remotes.origin.pull()
        print("Pull terminé avec succès.")
    except GitCommandError as e:
        print(f"Une erreur est survenue lors du fetch ou du pull : {e}")
