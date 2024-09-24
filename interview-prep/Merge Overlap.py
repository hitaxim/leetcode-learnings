def merge_overlap(arr):
    # Sort intervals based on start values
    arr.sort(key=lambda x: x[0])

    res = [arr[0]]

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current overlaps with the last
        # merged, merge them
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            # Add current to the result
            res.append(curr)

    return res

# Driver Code
if __name__ == "__main__":
    arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
    res = merge_overlap(arr)

    print("The Merged Intervals are: ", end="")
    for interval in res:
        print(f"[{interval[0]}, {interval[1]}]", end=" ")
    print()
