'''
Heroes beta-0.2-1
登陆处理
'''
import os

welcome = 'welcome to hero\'s world!'
print(welcome)

i = 0
while True:
    if os.path.isfile('lock.log'):
        print('locked!')
        break
    username = input('login: ')
    password = input('password: ')
    i += 1
    if username == 'leson' and password == '123456':
        print(welcome)
    else:
         if i == 3:
            open('lock.log','w').write(username)
            print('locked by %s'%username)
            break
    continue
    print(welcome)