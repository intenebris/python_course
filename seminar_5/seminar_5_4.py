# Посчитатать список сотрудников.
arr = [18, [[20,[155,7]],15]]

def calculate_staff(arr):
    resault = 0
    for item in arr:
        if type(item) is int:
            resault += item
        else:
            resault += calculate_staff(item)
    return resault

print(calculate_staff(arr))