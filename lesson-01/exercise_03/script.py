# ES 1
listStr = []

def test(str):
    new_str = str[::-1]
    for i in new_str:
        listStr.append(i)
    return listStr
                
print(test("uragano"))


tupleStr = []

def test2(str):
    new_str = str[::-1]
    for i in new_str:
        tupleStr.append(i)
    return tuple(tupleStr)

print(test2("uragano"))


# ES 2
inp = int(input("inserisci un numero compreso tra 1 e 10\n"))

for inp in range(inp, 11):
    print("")
    for y in range(1, 11):
        print(inp * y, end = " ")


# ES 3
list = []

revVocal = str(input("\n\nInserisci una stringa"))

def revealVocal(str):
    for i in str:
        if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
            list.append(i)
    return list        

show = revealVocal(revVocal)
print(show)
print(len(show))


# ES 4
inpStr = str(input("Inserisci un palindromo:\n"))

def isPalindrome(str):
    return str == str[::-1]


palin = isPalindrome(inpStr)
 
if palin:
    print("E un palindromo")
else:
    print("Non e un palindromo")