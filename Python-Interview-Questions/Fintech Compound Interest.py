def compound_interest(principal, rate, contribution, years):
    r = rate / 100
    initial_compound = principal * ((1 + r)**years)
    contribution_compound = contribution * (((1 + r) ** years - 1) / r)
    total = contribution_compound + initial_compound
    return round(total, 2)
