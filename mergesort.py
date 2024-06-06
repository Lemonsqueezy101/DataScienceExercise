import matplotlib.pyplot as plt

# Sortieralgorithmus
def mergeSort(list):
    
    # Bedingung für den rekursiven Aufruf
    if (len(list) > 1):
        
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        mergeSort(left)
        mergeSort(right)

        l, r, i = 0, 0, 0

        # Zusammenfuegen für den Mergesort
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                list[i] = left[l]
                l += 1
            else:
                list[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            list[i] = left[l]
            l += 1 
            i += 1

        while r < len(right):
            list[i] = right[r]
            r += 1
            i += 1

def plotting(my_list, title):
    x = range(len(my_list))
    bars = plt.bar(x,my_list)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title(title)
    for bar in bars:
        height = bar.get_height()  # Höhe des Balkens
        plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')
    plt.xticks(x)
    plt.show()

# Definition der Liste
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plotten der originellen Liste
plotting(my_list, "Unsorted")

# Auführen des Sortieralgorithmus
mergeSort(my_list)

# Plotten der Ergebnisse
plotting(my_list, "Sorted")
