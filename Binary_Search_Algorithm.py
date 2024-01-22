def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.

    Args:
        arr (list): Sorted array of elements.
        target: Element to be found in the array.

    Returns:
        int: Index of the target element if found, -1 otherwise.
    """
    # Check if the input array is sorted
    if arr != sorted(arr):
        raise ValueError("Input array must be sorted for binary search.")

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Element not found
