# ZADANIE 4.2
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, 
# które zwracają pełny string przez return. 
# Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

def make_ruler(n):
    ruler_upper = "|"
    ruler_bottom = "0"
    for i in range(1, n + 1):
        ruler_upper += "....|"
        ruler_bottom += str(i).rjust(5)

    ruler_upper += "\n" + ruler_bottom

    return ruler_upper

def make_grid(rows, cols):
    rectang = ""

    for i in range(rows * 2 + 1):
        curr_line = ""
        for j in range(cols * 4 + 1):
            if i % 2 == 0:
                curr_line += '+' if j % 4 == 0 else '-'
            else:
                curr_line += '|' if j % 4 == 0 else ' '
        rectang += '\n' + curr_line
    return rectang

print(make_ruler(5))
print(make_grid(3,4))


# ZADANIE 4.3
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factiorial(n):

    fact = 1

    for x in range(1, n+1):
        fact *= x

    return fact

print(factiorial(5))

# ZADANIE 4.4
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    previous = 0
    current = 1

    if n == 0:
        return previous
    elif n == 1:
        return current
    else:
        for x in range (0, n):
            temp = current
            current += previous
            previous = temp
    return previous

print(fibonacci(12))

# ZADANIE 4.5
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów 
# na liście od numeru left do right włącznie. 
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanie_i(L, left, right):
    while(left < right):
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        right -= 1
        left += 1

def odwracanie_r(L, left, right):
    if(left < right):
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        odwracanie_r(L, left+1, right-1)

L = [1, 2, 3, 4, 5]
odwracanie_i(L, 2, 4)
print(L)
odwracanie_r(L, 2, 4)
print(L)


# ZADANIE 4.6
# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, 
# która może zawierać zagnieżdżone podsekwencje. 
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, 
# wykonać przez isinstance(item, (list, tuple)).

def sum_sequence(sequence):
    result = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            result += sum_sequence(i)  
        else:
            result += i
    return result

print(sum_sequence([[1], (2, 3), [4], (5, 6, 7)]))


# ZADANIE 4.7
# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, 
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. 
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę 
# wszystkich elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, 
# a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def flatten(sequence):
    result = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            result += (flatten(i))
        else:
            result.append(i)
    return result

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))   # [1,2,3,4,5,6,7,8,9]