
def linear(a, elem):
    if a[i] == elem:
        pos = i + 1
        return pos

    if a[i] >= elem:
        return 0

def withrec(n, a, elem):
    n = int(input("Enter number of elements "))
    a = []
    for i in range(n):
        a = []
        x = int(input("Enter the elements: "))
        a.append(x)
    elem = int(input("Enter the element to be searched: "))

print(linear(a, elem))
