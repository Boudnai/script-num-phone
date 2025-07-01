import re

# Lire le contenu du fichier .ics
file_path = "Efoil_Cogolin_qqquf6itrgkuqg03u7epud71b8@group.calendar.google.com.ics"  # Remplacez par le chemin de votre fichier
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Rechercher les numéros de téléphone
pattern = r'\b(?:\+33\s?[1-9](?:\s?\d{2}){4}|0[67](?:\s?\d{2}){4})\b'
phone_numbers = re.findall(pattern, content)

# Afficher les numéros trouvés
i= 0
for number in phone_numbers:
    print(number)
    print (i)
    i = i + 1

# Si vous voulez sauvegarder les numéros dans un fichier :
output_path = "phone_numbers.txt"
with open(output_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(phone_numbers))
print(f"Les numéros de téléphone ont été sauvegardés dans {output_path}")
print ("\n il y a ", i, " numéros de téléphone")