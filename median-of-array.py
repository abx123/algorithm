import math

def subArray(start, end, arr):
    if start > end:
        raise Exception("error")
    if end > len(arr):
        raise Exception("error2")
    return arr[int(start):end-int(start)+1]


def median(arr):
    if (len(arr) % 2 == 0):
        return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) // 2
    return arr[(len(arr) - 1)//2]


def getMedian(arr1, arr2):
    if len(arr1) == 0 or len(arr1) != len(arr2):
        raise Exception("error3")
    return calculateMedian(arr1, arr2)


def calculateMedian(arr1, arr2):
    if len(arr1) == 1:
        return (arr1[0]+arr2[0]) / 2
    if len(arr1) == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
    median1 = median(arr1)
    median2 = median(arr2)
    if median1 == median2:
        return median1
    if median1 > median2:
        return calculateMedian(subArray((len(arr2) - 1) / 2, len(arr2), arr2), subArray(0, math.floor(len(arr1) / 2), arr1))
    return calculateMedian(subArray((len(arr1) - 1) / 2, len(arr1), arr1), subArray(0, math.floor(len(arr2) / 2), arr2))


print('median:', getMedian([1, 3, 5], [2, 4, 6]))
