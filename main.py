import math
import random

print("Hello world!")
print('Hello world!')
print("prekiu sarasas")

num = 20
print(num)
num = 24
print(num)
num = "dvidesimt septyni"
print("šimtas dvidešimt trys" + "šimtas dvidešimt trys")
print(num)
print("2" + "2")
print(2 + 2)
num = True
print(num)
print("a" + str(2))
print(int("20") + 14)

print(math.ceil(4.1))
print(math.floor(4.9))

rnd_num = random.randint(10,20) # bla bla
print(rnd_num)

if True:
    print("tiesa")
    print(";)")

num = 5
if num > 5:
    print("greiciausiai taip")
else:
    print("greiciausiai ne")

score = random.randint(0, 5)

if score == 0:
    print("terrible")
elif score == 1:
    print('rly bad')
elif score == 2:
    print('bad')
elif score == 3:
    print('meh')
elif score == 4:
    print("ok")
# elif score == 5:
#     print("good")
else:
    print("good")


score = random.randint(1, 100)

print("Random skaicius yra " + str(score))
if score < 10:
    print("maziau nei 10")
elif score >=10 and score < 50:
    print("tarp 10 ir 50")
elif score >= 50 and score <= 100:
    print('tarp 50 ir 100')


rnd_num = random.randint(1,10)

if rnd_num < 5 or rnd_num % 2 != 0:
    print(str(rnd_num) + ' yra arba maziau uz 5 arba neporinis')

# if elif else def while match for class


print(13 / 5) # grazina double reiksme 2.6
print(13 // 5)# grazina int reiksme 2    ---> .6 gražina floor reiksme (apvalina zemyn)
print(13 % 5)# 13 - 5 = 8; 8 - 5 = 3;

if rnd_num % 2 == 0:
    print('skaicius porinis')




score = random.randint(1, 4)

if score == 1:
    print('rly bad')
elif score == 2:
    print('bad')
elif score == 3:
    print('meh')
elif score == 4:
    print("ok")

score = random.randint(1, 4) #3

if score == 1:
    print('rly bad')

if score == 2:
    print('bad')

if score == 3:
    print('meh')

if score == 4:
    print("ok")




a = 1
b = 1
if a == 1: # Sąlyginis sakinys, du identacijos lygiai
    if b == 1:
        print("1 1")
    else:
        print("1 0")
else:
    if b == 1:
        print("0 1")
    else:
        print("0 0")



