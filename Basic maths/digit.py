def digit_extract(n):
    if n == 0:
        return
    digit = n % 10
    print(digit)
    digit_extract(n//10)

def digit_extrac_while(n):
    while n > 0:
        extract_digit = n % 10
        print(extract_digit)
        n = n//10

digit_extract(45678)
digit_extrac_while(332178)