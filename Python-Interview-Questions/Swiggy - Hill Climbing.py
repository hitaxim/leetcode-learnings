def climb_hill(n):
    # Base cases
    if n == 0 or n == 1:
        return 1
  
    return climb_hill(n - 1) + climb_hill(n - 2)
