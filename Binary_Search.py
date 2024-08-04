def binary(arr,terget):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2 # mid listdagi sonlarni o'rtadagisini o'ziga oladi
        guess = arr[mid] # bunda o'sha  listni o'rtasidagi elementni oladi
        if guess == terget:
            return guess
        elif guess > terget:
            high = mid - 1
        else:
            low = mid + 1
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
terget = int(input('qaysi sonni izlayopsiz: '))

print(binary(arr,terget))
