def linearnonrec(a, elem):
    for i in range(len(a)):
        if a[i] == elem:
            return  i + 1
    return -1

n = int(input("Enter the size of an array: "))
a = []
for i in range(n):
    x = int(input("Enter the elements: "))
    a.append(x)
elem = int(input("Enter the element to be searched: "))

print(linearnonrec(a, elem))
