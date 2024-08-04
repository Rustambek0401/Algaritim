
def liner(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return None

arr = []
a = int(input('Listga nechta son kiritasiz: '))
while a > 0:
    a-=1
    b = int(input('son kiriting: '))
    arr.append(b)
arr.sort()
print(arr)
c = int(input('qaysi sonni izlayopsiz: '))

print(liner(arr,c))
