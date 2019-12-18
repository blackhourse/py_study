#  if else   elif  后要跟 :
age = 1
if age <= 18:
    print('You age is ', age)
    print('a')
    print('ss')
    print('fd')
else:
    print('什么都不是')

if age <= 18:
    print('你还是个孩子')
elif age <= 30:
    print('结婚了吗')
else:
    print('ssssss')

if 1:
    print('true')
else:
    print('false')

# 将输入的数组（字符串）  转为int
s = 1

a = int(s)
if a:
    print('true')
else:
    print('false')
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = 1.75
weight = 80.5

a = weight / (height * height).__setattr__()
print('BMI指数为', a)
if a <= 18.5:
    print('过轻')
elif a <= 25:
    print('正常')
elif a <= 28:
    print('过重')
elif a <= 32:
    print('肥胖')
else:
    print('严重肥胖')
