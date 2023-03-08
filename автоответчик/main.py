import analyzer
while True:
    req = input('Введите запрос или "off" для завершения работы: ').lower()
    if req == 'off':
        break
    else:
        analyzer.main(req)