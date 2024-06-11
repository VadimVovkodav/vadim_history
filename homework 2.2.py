number = int(input("введіть п'яти значне число "))

digit5 = number % 10

digit4 = (number // 10) % 10

digit3 = (number // 100) % 10

digit2 = (number // 1000) % 10

digit1 = (number // 10000) % 10

print(digit5, digit4, digit3, digit2, digit1)