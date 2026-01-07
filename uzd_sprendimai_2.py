import random
import re

name = "Leonardo"
surname = "Dicaprio"

# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus. Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš trijų paskutinių vardo ir pavardės kintamųjų raidžių. Jį atspausdinti.

nickname =  name[-3:]+surname[-3:]
print(nickname)

text =  "An American in Paris"
text.replace("a","*").replace("A","*")
print(text.replace("a","*").replace("A","*"))

res = re.sub("[aeiouyAEIOUY]","*",text)

print(res)

my_text = "6s1df56sd165165asd654asds-;'?!1DAStopIterationdf98"
print(re.sub("[aeiouyAEIOUY]", "*", my_text))
print(re.sub("[a-zA-Z]","*", my_text))
print(re.sub("[0-9]","*", my_text))
print(re.sub("[a-d]","*", my_text))
print(re.sub("[a-z]","*", my_text))
print(re.sub("[^a-z]","*", my_text))
print(re.sub("[a-z]","*", my_text))

starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
print(starWars)
print(starWars[-14])
print(re.sub(r"[^\d]","",starWars))
print(re.sub(r"[^0-9]","",starWars))
print(re.sub(r"[a-zA-Z :-]","",starWars))
print(re.sub(r"[^\d]","",starWars.split("Episode")[1]))

# Sukurk stringą su žodžiu.
#  Atspausdink „Sutampa“, jei pirmoji ir paskutinė raidė vienoda (naudok word[0] ir word[-1]), kitaip „Nesutampa“.

text = 'w'

if text.lower()[0] == text.lower()[-1]:
 print("sutampa")
else:
 print("nesutampa")

 # Sukurk kintamąjį su bet kokiu žodžiu.
 # Atspausdink tą patį žodį, bet visos raidės išskyrus pirmą ir paskutinę turi būti pakeistos į _.
 # Pvz. Python → P____n.
if len(text) > 1:
  print(text[0] + "_" * (len(text) - 2) + text[-1])
else:
  print(f"prasau paduokite texta bent is 2 simboliu. padavete: {text}")

print("5" in "labas")
text = "Man 24 metai"

if '1' in text or '2' in text:
 print("taip")
else:
 print('ne')


if '1' in text or '2' in text:
 print("taip")
else:
 print('ne')







