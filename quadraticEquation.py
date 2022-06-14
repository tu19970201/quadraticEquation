def realNum(a,b,c):
    real = b * b - 4 * a * c
    if real > 0: # 有兩個實數解
        real **= 0.5  # 根號相當於0.5次方
        print('此方程式的根為', (-b + real) / (a * 2), (-b - real) / (a * 2))
    elif real < 0: # 無實數解
        print('無實數解')
    else: # 有一個實數解
        print('此方程式的根為', -b / (a * 2))

print('ax + bx^2 + c = 0')
a=int(input('請輸入 a = '))
b=int(input('請輸入 b = '))
c=int(input('請輸入 c = '))

realNum(a,b,c)


