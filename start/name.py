'''
Heroes beta -0.1
developlee
2017-12-17
'''
print('welcome to Heros World')
name = input('input your name: ')
if not name:
    name = 'player'
hp = 100
usermsg = [name, hp]
print("your hero's name is:", usermsg[0])