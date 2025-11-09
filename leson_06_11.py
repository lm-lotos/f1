# 12.створіть словник , який відображає інедтифікатор акцій на біржі іещсл

stocks = {
    "IBM": 205.55,
    "FB": 10.75,
    "ACME": 45.23,
    "AAPL": 612.78,
    "HPQ": 37.2
    }

for key, value in stocks.items():
    print(value, key)



# 13. В рядку записаний текст. Словом вважаеться послідовність непробільних символів, які йдуть підряд

# 14 --

text =  "a bb acD bb abc ac BCD a".liwer().srlit()
# ['a' 'bb', 'acD', 'bb', 'abc', 'ac', 'bcd', 'a']

tex_set = set(text) # {'a' 'bb', 'acD', 'bb', 'abc', 'ac', 'bcd',}

result = or word in text: 