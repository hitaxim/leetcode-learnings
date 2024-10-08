import re

def simplify_expression(expr: str) -> str:
    # Step 1: Remove spaces
    expr = expr.replace(' ', '')
    
    # Step 2: Handle multiplications (convert `a*4` to `4a`)
    expr = re.sub(r'(\d+)\*([a-z])', r'\1\2', expr)  # Handles cases like `4*a`
    expr = re.sub(r'([a-z])\*(\d+)', r'\2\1', expr)  # Handles cases like `a*4`
    
    # Step 3: Prepare the expression by replacing '-' with '+-' for easier splitting
    expr = expr.replace('-', '+-')
    
    # Step 4: Tokenize by '+' separator
    tokens = expr.split('+')
    
    # Step 5: Dictionary to store the coefficients for each variable
    terms = {}
    
    # Step 6: Process each token and update the terms dictionary
    for token in tokens:
        if token:  # Ignore empty tokens
            # Match the coefficient and variable part
            match = re.match(r'(-?\d*)([a-z]*)', token)
            if match:
                coeff_str, variable = match.groups()
                
                # If coefficient is empty, it means it's either 1 or -1
                if coeff_str in ['', '-']:
                    coeff = int(coeff_str + '1') if coeff_str else 1
                else:
                    coeff = int(coeff_str)
                
                # Add the coefficient to the respective variable in the terms dictionary
                if variable in terms:
                    terms[variable] += coeff
                else:
                    terms[variable] = coeff
    
    # Step 7: Construct the simplified expression from the terms dictionary
    simplified = []
    for var, coeff in sorted(terms.items(), key=lambda x: x[0]):  # Sort by variable for consistency
        if coeff == 0:
            continue
        if var == '':  # This is the constant term
            simplified.append(str(coeff))
        elif coeff == 1:
            simplified.append(f"{var}")
        elif coeff == -1:
            simplified.append(f"-{var}")
        else:
            simplified.append(f"{coeff}{var}")
    
    # Join the terms and handle clean up of signs
    result = '+'.join(simplified).replace('+-', '-')
    
    # If the result is empty, return '0'
    return result if result else '0'

# Example usage

expression = "a + a * 4 - b + c + 3 * b"
print("Original:", expression)
expression = expression.replace(' ', '')  # Clean up spaces for simplicity
print("Simplified:", simplify_expression(expression))  # Expected Output: "5a + 2b + c"
