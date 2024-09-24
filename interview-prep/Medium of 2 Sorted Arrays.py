# Python Code to find Median of two Sorted Arrays of 
# Different Sizes using Sorting
def median_of_two_sorted_arrays(arr1, arr2):
    # Concatenate the arrays
    arr3 = arr1 + arr2
    # Sort the concatenated array
    arr3.sort()
    # Calculate and return the median
    n = len(arr3)
    # If length of array is even
    if n % 2 == 0:
        mid1 = n // 2
        mid2 = mid1 - 1
        # Check if result is an integer
        median = ((arr3[mid1] + arr3[mid2]) / 2)
        if median.is_integer():
            return int(median)
        return median
    # If length of array is odd
    else:
          return arr3[n // 2]

if __name__ == "__main__":
      
    arr1 = [-5, 3, 6, 12, 15]
    arr2 = [-12, -10, -6, -3, 4, 10]
    
    print(median_of_two_sorted_arrays(arr1, arr2))
