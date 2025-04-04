import os
from sacremoses import MosesTokenizer

def tokeniser_et_sauvegarder_fichiers(dossier):
    """
    Tokenise le contenu de tous les fichiers .txt d'un dossier donné
    et enregistre les tokens dans de nouveaux fichiers .tokenized.txt.
    
    :param dossier: Chemin du dossier contenant les fichiers .txt
    """
    dossier_tokenized = dossier + "_tokenized"  # Nouveau dossier pour stocker les fichiers tokenisés

    # Vérifier si le dossier existe
    if not os.path.isdir(dossier):
        raise FileNotFoundError(f"Le dossier '{dossier}' n'existe pas.")
    
     # Créer le dossier de sortie s'il n'existe pas
    if not os.path.exists(dossier_tokenized):
        os.makedirs(dossier_tokenized)

    # Parcourir les fichiers .txt
    for fichier in os.listdir(dossier):
        if fichier.endswith(".txt"):
            chemin_fichier = os.path.join(dossier, fichier)
            chemin_fichier_tokenized = os.path.join(dossier_tokenized, fichier.replace(".txt", ".tokenized.txt"))

            # Déduire la langue du fichier à partir de son nom
            langue = fichier.replace(".txt", "").lower()

            try:
                tokenizer = MosesTokenizer(lang=langue)  # Tokenizer pour la langue du fichier

                with open(chemin_fichier, "r", encoding="utf-8") as f:
                    contenu = f.read()
                    tokens = tokenizer.tokenize(contenu)  # Tokenisation
                
                # Sauvegarder les tokens dans un nouveau fichier
                with open(chemin_fichier_tokenized, "w", encoding="utf-8") as f_out:
                    f_out.write(" ".join(tokens))
                
                print(f"Tokenisation terminée : {chemin_fichier_tokenized}")
            except Exception as e:
                print(f"Erreur avec {fichier}: {e}")

# Exemple d'utilisation
dossier_test = "data"
tokeniser_et_sauvegarder_fichiers(dossier_test)
