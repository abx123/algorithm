
def missingTwo(arr):
    size = len(arr) + 2
    totalSum = size * (size + 1) / 2
    arrSum = 0
    for i in range (len(arr)):
        arrSum += arr[i]
    pivot = (int) ((totalSum - arrSum) / 2)
    totalLeftXor = 0
    arrLeftXor = 0
    totalRightXor = 0
    arrRightXor = 0
    i = 0
    j = pivot + 1
    while i <= pivot:
        totalLeftXor ^= i
        i +=1
    while j <= size:
        totalRightXor ^= j
        j +=1
    for r in range (len(arr)):
        if arr[r] <= pivot:
            arrLeftXor ^= arr[r]
        else:
            arrRightXor ^= arr[r]
    return [totalLeftXor ^ arrLeftXor, totalRightXor ^ arrRightXor]

def missingOne(arr):
    totalXor = 0
    arrXor = 0
    i = 0
    while i<= len(arr)+1:
        totalXor ^= i
        i += 1
    for i in range (len(arr)):
        arrXor ^= arr[i]

    return totalXor ^ arrXor

print(missingTwo([1,2,5,6,7,8]))
print(missingOne([1,2,3,4,6,7,8]))