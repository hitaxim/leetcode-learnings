def intToRoman(num):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = [
        "", "C", "CC", "CCC", "CD", "D", "DC", 
        "DCC", "DCCC", "CM"
    ]
    tens = [
        "", "X", "XX", "XXX", "XL", "L", "LX", 
        "LXX", "LXXX", "XC"
    ]
    ones = [
        "", "I", "II", "III", "IV", "V", "VI", 
        "VII", "VIII", "IX"
    ]

    thousand_part = thousands[num // 1000]
    hundred_part = hundreds[num % 1000 // 100]
    ten_part = tens[num % 100 // 10]
    one_part = ones[num % 10]

    return thousand_part + hundred_part + ten_part + one_part
    
"""
def intToRoman(num):
    rom = {
    1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 
    50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 
    500: 'D', 900: 'CM', 1000: 'M'
    }
    numbers = [
    1000, 900, 500, 400, 100, 
    90, 50, 40, 10, 9, 5, 4, 1
    ]

    roman_number = ''
    index = 0
    while num > 0:
        x = num // numbers[index]
        if x > 0:
            roman_number += (rom[numbers[index]] * x) 
            num -= x * numbers[index]  
            # You can also do num = num % numbers[index]
        index += 1

    return roman_number
 
