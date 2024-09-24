# Python3 program to find Majority
# element in an array using nested loops

# Function to find the Majority element in an array
def majorityElement(arr):
    n = len(arr)  

    # Loop to consider each element as a candidate for majority
    for i in range(n):
        count = 0

        # Inner loop to count the frequency of arr[i]
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        # Check if count of arr[i] is more than half the size of the array
        if count > n // 2:
            return arr[i]

    # If no majority element found, return -1
    return -1

if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]

    print(majorityElement(arr))
