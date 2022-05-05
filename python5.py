import random
import time

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")
print()

li = []
while True:
    a = input("메뉴 추가: ")
    if a not in li:
        li.append(a)
        print("현재 메뉴 수 = " + str(len(li)))
        print()
    else:
        print("이미 있는 메뉴예요! 다른 메뉴를 입력해주세요.")
        print("현재 메뉴 수 = " + str(len(li)))
        print()

    if len(li) == 5:
        break
print()

for i in range(3):
    print(3 - i)
    time.sleep(1)

print()
print(li)
print("과연 오늘의 메뉴는?")
print()

for i in range(3):
    print(3 - i)
    time.sleep(1)
r = random.choice([0, 1, 2, 3, 4])
print()
print("오늘의 메뉴는 " + str(r + 1) + "번째 메뉴, " + li[r] + " 입니다.")
