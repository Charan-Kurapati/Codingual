s1=[3,4,7,2,9]

s2=["w","u","i","v","k"]

s3=list(zip(s1,s2))

print(s3)

s4=["d","f","k","v","a",]

s5=[3,6,4,9,8]

s6=list(zip(s4,s5[::-1]))

print(s6)

stocks = ['reliance', 'infosys', 'tcs']

prices = [2175, 1127, 2750]

#zip into dictionary

new_dict = {stocks: prices for stocks,prices in zip(stocks, prices)}

print(new_dict)