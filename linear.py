
def linear_search(a, ele):
    if a[i] == ele:
        pos = i + 1
        return pos

    if a[i] >= ele:
        return 0

def recursion(n, a, ele):
    n = int(input("Enter number of elements "))
    a = []
    for i in range(n):
        a = []
        x = int(input("Enter the elements: "))
        a.append(x)
    ele = int(input("Enter the element to be searched: "))

print(linear(a, ele))
