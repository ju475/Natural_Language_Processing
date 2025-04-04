import os

def token_count(dossier):
    """
    Compte le nombre de mots dans tous les fichiers .txt d'un dossier donné.
    :param dossier: Chemin du dossier contenant les fichiers .txt
    :return: Dictionnaire avec le nom du fichier et le nombre de mots
    """
    total_mots = 0
    
    # Vérifier si le dossier existe
    if not os.path.isdir(dossier):
        raise FileNotFoundError(f"Le dossier '{dossier}' n'existe pas.")
    
    # Parcourir les fichiers du dossier
    for fichier in os.listdir(dossier):
        if fichier.endswith(".txt"):  # Vérifier l'extension
            chemin_fichier = os.path.join(dossier, fichier)
            try:
                with open(chemin_fichier, "r", encoding="utf-8") as f:
                    contenu = f.read()
                    nombre_token = len(contenu.split())  # Compter les mots
                    print(f"Nombre de token {fichier} : {nombre_token}")
            except Exception as e:
               print(f"Erreur avec {fichier}: {e}")
    
    return total_mots



import random

def extract_subset(input_file, output_file, fraction=0.25):
    with open(input_file, "r", encoding="utf-8") as f:
        remaining_lines = f.readlines()  # Lire le reste du fichier pour l'échantillonnage
    
    subset_size = max(1, int(len(remaining_lines) * fraction))
    subset = random.sample(remaining_lines, subset_size)  # Sélection aléatoire dans le reste du fichier
    
    with open(output_file, "a", encoding="utf-8") as f:  # Mode "a" pour ajouter à la fin
        f.writelines(subset)



# Utilisation
extract_subset("./01-Assigment 1/data/fr(1).txt", "./01-Assigment 1/data/fr.txt")