# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child
    right = 2 * i + 2    # Right child

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

# Function to perform Heap Sort
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Driver Code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)

    heap_sort(arr)

    print("Sorted array:", arr)
