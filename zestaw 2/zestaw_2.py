line = "djsa adks alds GvR alsdjsa ldj" # 5 wyrazów
L = [1, 42, 123, 5, 163, 69, 213, 745]
number = 21903213021314065450458648065845860 # 6 zer

# ZADANIE 2.10
# Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. 
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

def word_count(line):
    return len(line.split())

print(word_count(line))

# ZADANIE 2.11
# Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

def underscore_inserter(word = "word"):
    return '_'.join(word[i:i+1] for i in range(0, len(word), 1))

print(underscore_inserter())

# ZADANIE 2.12
# Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.

def first_and_last(line):
    firsts = ""
    lasts = ""
    line = line.split()
    for x in range(len(line)):
        firsts += line[x][0]
        lasts += line[x][-1]
    return firsts, lasts

print(first_and_last(line))

# ZADANIE 2.13
# Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().

def letter_counter(line):
    sum = 0
    for x in line.split():
        sum += len(x)
    return sum

print(letter_counter(line))

# ZADANIE 2.14
# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

def longest_finder(line):
    longest = max(line.split(), key=len)
    return longest, len(longest)

print(longest_finder(line))

# ZADANIE 2.15
# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

def concatenator(L):
    return ''.join(str(int) for int in L)

print(concatenator(L))

# ZADANIE 2.16
# W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

def rossumer(line):
    return line.replace("GvR", "Guido van Rossum")

print(rossumer(line))

# ZADANIE 2.17
# Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().

def sorter(line):
    return sorted(line.split(), key=str.lower), sorted(line.split(), key=len)

print(sorter(line))

# ZADANIE 2.18
# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

def zero_counter(number):
    return str(number).count('0')

print(zero_counter(number))

# ZADANIE 2.19
# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków, 
# gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

def tri_blocker(L):
    blocks = ""
    L = list(map(str, L))
    for x in range(len(L)):
        L[x] = L[x].zfill(3)
    return " ".join(L)

print(tri_blocker(L))