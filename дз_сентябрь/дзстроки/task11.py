a = '+79012342452'
b = a.find('+')
print('<a href="tel:' + a[b:b+12:] + '">' + a[b:b+12:] + '</a>')