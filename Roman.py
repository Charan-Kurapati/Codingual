class RomanNumeral:
    def __init__(self,number):
        self.number = number

    def convert_to_roman(self):
        values = [ 
            (1000,"M"),
            (900,"CM"),
            (500,"C"),
            (400,"CD"),
            (100,"C"),
            (90,"XC"),
            (50,"L"),
            (40,"XL"),
            (10,"X"),
            (9,"IX"),
            (5,"V"),
            (4,"IV"),
            (1,"I")
        ]

        roman = ""

        for value,symbol in values:
            while self.number >= value:
                roman += symbol
                self.number -= value

        return roman

num = int(input("Enter an integer:"))

obj = RomanNumeral(num)

print("Roman Numeral:",obj.convert_to_roman())