n = int(input('Введите число (больше 999)'))
sto = (n//100) % 10
mnogo = (n//1000) % 10
print(f'число тысяч в числе = {mnogo}, число сотен в числе = {sto}')
