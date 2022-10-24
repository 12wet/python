# ZADANIE 3.1
# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
# for i in "axby": if ord(i) < 100: print (i)
# for i in "axby": print (ord(i) if ord(i) < 100 else i)

# NIE BYŁ PONIEWAŻ PYTHON JEST NEWLINE SENSITIVE ORAZ NIE WYMAGA ';'.
# Poprawiona wersja:

x = 2; y = 3
if (x > y):
    result = x
else:
    result = y
for i in "axby": 
    if ord(i) < 100: 
        print (i)

for i in "axby": 
    print(ord(i) if ord(i) < 100 else i)

# ZADANIE 3.2
# Co jest złego w kodzie:

# L = [3, 5, 4] ; L = L.sort()
# x, y = 1, 2, 3
# X = 1, 2, 3 ; X[1] = 4
# X = [1, 2, 3] ; X[3] = 4
# X = "abc" ; X.append("d")
# L = list(map(pow, range(8)))

# KOD JEST NIECZYTELNY PRZEZ DEKLAROWANIE KILKU OPERACJI W JEDNEJ LINII

# ZADANIE 3.3
# Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.

for x in range(0, 31):
    if x % 3 != 0:
        print(x)

# ZADANIE 3.4
# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. 
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

while True:
    user_input = input('Enter your digit:\n')
    if user_input == "stop":
        break
    try:
        input_float = float(user_input)
        print('{0} {1}'.format(input_float, input_float**3))
    except:
        print('Not a digit')

# ZADANIE 3.5
# Napisać program rysujący "miarkę" o zadanej długości. 
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). 
# Należy zbudować pełny string, a potem go wypisać.

# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12

length = int(input("Length:\n"))

ruler_upper = "|"
ruler_bottom = "0"
for i in range(1, length + 1):
    ruler_upper += "....|"
    ruler_bottom += str(i).rjust(5)

ruler_upper += "\n" + ruler_bottom

print(ruler_upper)

# ZADANIE 3.6
# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   | 
# +---+---+---+---+

rectang = ""

x = int(input("X:\n"))
y = int(input("Y:\n"))

for i in range(y * 2 + 1):
    curr_line = ""
    for j in range(x * 4 + 1):
        if i % 2 == 0:
            curr_line += '+' if j % 4 == 0 else '-'
        else:
            curr_line += '|' if j % 4 == 0 else ' '
    rectang += '\n' + curr_line
print(rectang)

# ZADANIE 3.8
# Dla dwóch sekwencji liczb lub znaków znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), 
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).


first = "agdhjsghkads687976"
second = "opiaudsgriau297863"

print("Intersection: {0}".format(set(list(first)).intersection(second)))
print("Union: {0}".format(set(first).union(second)))

# ZADANIE 3.9
# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. Znaleźć listę zawierającą sumy liczb z tych sekwencji. 
# Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

seq = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

for i in seq:
    print(sum(i))

# ZADANIE 3.10
# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). 
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

roman_int = {
    'I': 1, 
    'V': 5, 
    'X': 10,
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000
}

roman_int = dict({
    'I': 1, 
    'V': 5, 
    'X': 10,
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000
})
roman_int = dict([
    ('I', 1),
    ('V', 5), 
    ('X', 10),
    ('L', 50),
    ('C', 100), 
    ('D', 500),
    ('M', 1000)
])