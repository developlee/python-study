x = input('please input your x ')

nums = []
for i in range(1,int(x)):
    if i%5 == 0 or i%3 == 0:
        nums.append(i)
print(nums)
print(sum(nums))
'''
列表解析表达式
[expr for iter_var in iterable]
[expr for iter_var in iterable if cond_expr]

生成器表达式
(expr for iter_var in iterable)
(expr for iter_var in iterable if cond_expr)
'''
