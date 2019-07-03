import random
list = random.randint(0,101) 

def binarySearch(list, item):

    low = 0
    high = len(list)-1
    found = False

    while low <= high and not found:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid 
            found = True
            print("Brawo! Trafione!")
            
            if guess > item :    # trafiono za duza liczbe 
                high = mid -1
                print("Za duza liczba!")
            else:
                low = mid + 1

    return None
    print("oszukujesz")

print(list)    # wypuszcza mi losową liczbę w terminalu












