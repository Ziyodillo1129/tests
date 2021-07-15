#Selection sort algorithm

def Selection_sort(a):
    for i in range (0, len(a) -1):
        minx = i
        for j in range (i+1, len(a)):
            if a[j] < a[minx]:
                minx = j
        if minx !=i:
            (a[i], a[minx]) = (a[minx], a[i])

a = [-4, 12, 9, 0, 5, 28]
Selection_sort(a)
print(a)
