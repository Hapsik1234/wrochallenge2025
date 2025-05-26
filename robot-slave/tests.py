def rotate(arr):
    element = arr.pop()
    arr.insert(0, element)
    return arr

array = [2, 3, 4, 1]

array = rotate(rotate(rotate(array)))

print(array)
if(array == [3, 4, 1, 2]):
    print("Passed")
else:
    raise AssertionError