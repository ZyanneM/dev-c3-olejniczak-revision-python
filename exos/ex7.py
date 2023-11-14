def count_words(input_file, output_file):
    try:
        # Ouvrir le fichier d'entrée en mode lecture
        with open(input_file, 'r', encoding='utf-8') as file:
            # Lire le contenu du fichier
            content = file.read()

            # Compter le nombre de mots
            word_count = len(content.split())

            # Ouvrir le fichier de sortie en mode écriture
            with open(output_file, 'w', encoding='utf-8') as output:
                # Écrire le résultat dans le fichier de sortie
                output.write(f"Le nombre de mots dans le fichier est : {word_count}")
                
        print(f"Le résultat a été écrit dans le fichier {output_file}")

    except FileNotFoundError:
        print(f"Le fichier {input_file} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Utilisation de la fonction avec vos noms de fichiers
count_words("code_passion.txt", "output.txt")