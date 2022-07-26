def my_roman_numerals_converter(num):
    numbers = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,

    }

    ro_num = list(numbers.keys())
    ar_num = list(numbers.values())
    output = ""

    def sort(num, ro, ar):
        i = 0
        while num > 0:
            ro[i] = int(num / ar[i])
            num = num % ar[i]
            i += 1

    sort(num, ro_num, ar_num)
    
    for item in range(len(ro_num)):
        elem = ro_num[item]
        if (isinstance(elem, str)):
            ro_num[item] = 0   

    def convert(val):
        roman_numeral = ""
        i = 0
        ro = list(numbers.keys())
        for item in val:
            while item > 0:
                roman_numeral += ro[i]
                item -= 1
            i += 1  
        return roman_numeral        

    output = convert(ro_num)

    return output    

my_roman_numerals_converter(79)    