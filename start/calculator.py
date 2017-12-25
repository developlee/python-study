x = int(input('please input your frist key: '))
o = input('please input your operator: ')
y = int(input('please input your second key: '))

operator = {
    '+': x+y,
    '-': x-y,
    '*': x*y,
    '/': x/y,
}
result = operator.get(o, 'input + - * /')
print(result)