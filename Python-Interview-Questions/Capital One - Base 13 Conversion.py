def convertToBase13(num):
  if num == 0:
    return "0"
  
  base13 = "0123456789ABC"
  digits = ""
  positive = abs(num)
  
  while positive > 0:
    digits += base13[positive % 13]
    positive = positive // 13
  
  reversed_d = digits[::-1]
  if num < 0:
    return "-" + reversed_d
  return reversed_d
	
