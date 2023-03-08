string = str(input('Придумайте логин:'))
symbols = '=?*^$№@_'
amount = 1
for i in string:
    if i in symbols:
        print(i)
