dic = {}

while True:
    a = input("Enter a fruit type (q to quit): ")
    if a == "q":
        print(dic)
        break
    b = input("Enter the weight in kg: ")
    dic[a] = b