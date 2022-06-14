# ES 1
from tokenize import String


lister = [[1, 2, 3], [1.1, 1.2, 1.3], ['abc', 'def', 'ghi']]
print(lister)

for i in lister[0]:
    if isinstance(i, int):
        print("I numeri sono tutti interi")
        
for i in lister[1]:
    if isinstance(i, float):
        print("I numeri sono tutti decimali")

for i in lister[2]:
    if isinstance(i, String):
        print("le stringhe sono tutte stringhe")
        
        
# ES 2
print("\n\n")
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2][1] = 7000
list1.remove(20)
print(list1)

# ES 3
print("\n\n")
print(f"{list(range(0, 9, 2))} {list(range(1, 9, 2))}")


# ES 4
print("\n\n")
frutta = ("mela", "mango", "papaya", "ananas", "ciliegia")
verde, *tropicale, rosso = frutta
print(verde, tropicale, rosso)

# ES 5
print("\n\n")
dict = {1: 'Nicola', 2: 'Giacomo', 3: 'Mario', 4: 'Lorenzo'}
total = 0
for key in dict:
    total += len(dict[key])
    print(len(dict[key]))
    
print(total)