while True: 
    usr = input('Введите что угодно: ')
    if usr == 'quit':
        break
    else:
        fl = open('C:/Users/abusha/Desktop/python/config.txt', 'w')
        fl_out = fl.write(usr)
        print('Было записано байт: ' + str(fl_out))
        fl.close()