import re

file_path = "Path_of_your_google_calendar_file.ics"  
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'\b(?:\+33\s?[1-9](?:\s?\d{2}){4}|0[67](?:\s?\d{2}){4})\b'
phone_numbers = re.findall(pattern, content)

i= 0
for number in phone_numbers:
    print(number)
    print (i)
    i = i + 1

output_path = "phone_numbers.txt"
with open(output_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(phone_numbers))
print(f"Phone numbers are save at {output_path}")
print ("\n There is ", i, " phone numbers")
