def to_roman_numeral(number):
    roman_number = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
              (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    symbol = []
    
    for value, numeral in roman_number:
        while number >= value:
            symbol.append(numeral)
            number -= value
    return ''.join(symbol)

print(to_roman_numeral(800))