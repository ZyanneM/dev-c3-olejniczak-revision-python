def count_words(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            word_count = len(content.split())
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(f"Le nombre de mots dans le fichier est : {word_count}")
                
        print(f"Le résultat a été écrit dans le fichier {output_file}")