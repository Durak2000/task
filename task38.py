def find_number(k):
    
    num = ''.join(str(i) for i in range(101, 151))
    
   
    if k % 3 == 0 and (k % 3 == 1 or k % 3 == 2):
        return num[k - 1]  
    else:
        return "k не удовлетворяет условиям."

k = int(input("Введите целое число k (1 <= k <= 150): "))
if 1 <= k <= 150:
    результат = найти_k_ю_цифру(k)
    print(f"{k}-я цифра последовательности: {результат}")
else:
    print("k должно быть в диапазоне от 1 до 150.")
