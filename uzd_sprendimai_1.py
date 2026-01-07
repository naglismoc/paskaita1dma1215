import random

# Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 4. Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą jį suapvalinę iki 2 skaičių po kablelio.
r1 = random.randint(0,4)
r2 = random.randint(0,4)
print(r1,r2)

if r1 != 0 and r2 != 0:
    if r1 > r2:
        print(round(r1 / r2, 2))
    else:
        print(round(r2 / r1, 2))
else:
    print('dalyba is nulio negalima')


if r1 == 0 or r2 == 0:
    print('dalyba is nulio negalima')
elif r1 > r2:
    print(round(r1 / r2, 2))
else:
    print(round(r2 / r1, 2))

if r1 >= r2 and r2 != 0:
    print(round(r1 / r2, 2))
elif r1 < r2 and r1 != 0:
    print(round(r1 / r2, 2))
else:
    print('dalyba is nulio negalima')

big = max(r1, r2)
small = min(r1, r2)
if small == 0:
    print("Division by zero is not possible")
else:
    print(f"{big / small:.2f}")

print("turime skaicius " + str(r1) + " ir " + str(r2))

# print(f"turime skaicius {r1:^10} ir {r2:^20}")
# print(f"turime skaicius {100:<10} ir {1000:>20}")


# Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 25. Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

r1 = random.randint(0,25)
r2 = random.randint(0,25)
r3 = random.randint(0,25)
r1, r2, r3 = 11, 11, 1
print(r1, r2, r3)
#   1 < 10 < 11
#   11 < 10 < 1
if r1 < r2 < r3 or r1 > r2 > r3:
    print(r2)
elif r2 < r1 < r3 or r2 > r1 > r3:
    print(r1)
elif r2 < r3 < r1 or r2 > r3 > r1:
    print(r3)
else:
    print('Alex sako, kad neatitinka sąlygos')

r1, r2, r3 = 11, 14, 25
if r1 <= r2 <= r3 or r1 >= r2 >= r3:
    print(r2)

if r2 <= r1 <= r3 or r2 >= r1 >= r3:
    print(r1)

if r2 <= r3 <= r1 or r2 >= r3 >= r1:
    print(r3)

sum = r1 + r2 + r3
print(sum - max(r1,r2,r3) - min(r1,r2,r3))



# Sukurkite keturis kintamuosius ir ​random.randint(x,x)​ funkcija sugeneruokite jiems reikšmes nuo 0 iki 2. Suskaičiuokite kiek yra nulių, vienetų ir dvejetų. (sprendimui masyvo nenaudoti).

r1 = random.randint(0,2)
r2 = random.randint(0,2)
r3 = random.randint(0,2)
r4 = random.randint(0,2)
print(r1,r2,r3,r4)
zeros = 0
ones = 0
twos = 0

if r1 == 0:
    zeros += 1
    # zeros = zeros + 1
if r2 == 0:
    zeros += 1
if r3 == 0:
    zeros += 1
if r4 == 0:
    zeros += 1

if r1 == 1:
    ones += 1
if r2 == 1:
    ones += 1
if r3 == 1:
    ones += 1
if r4 == 1:
    ones += 1

if r1 == 2:
    twos += 1
if r2 == 2:
    twos += 1
if r3 == 2:
    twos += 1
if r4 == 2:
    twos += 1

print(zeros,ones,twos)

starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"

print(starWars)


# Padarykite skaitmeninį laikrodį, rodantį valandas, minutes ir sekundes. Valandom, minutėm ir sekundėm sugeneruoti panaudokite funkciją random.randint(x,x). Sugeneruokite skaičių nuo 0 iki 300. Tai papildomos sekundės. Skaičių pridėkite prie jau sugeneruoto laiko. Atspausdinkite laikrodį prieš ir po sekundžių pridėjimo ir pridedamų sekundžių skaičių.

h = random.randint(0,23)
m = random.randint(0,59)
s = random.randint(0,59)
s_add = random.randint(0,300)
h,m,s,s_add = 23,59,59,62
print(h,m,s,s_add, sep=':')

m += (s+s_add) // 60
s = (s+s_add) % 60
h = h + (m // 60) if h + m //60 < 24 else (h +  m //60) - 24
m = m % 60

print(h,m,s, sep=':')