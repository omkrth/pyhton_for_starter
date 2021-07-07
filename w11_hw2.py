print("학번:2021312031, 이름:윤태현\n<inch->cm 출력 프로그램>\n")

def inchToCenti (a):
    return 2.54*a

num=float(input("inch 입력 : "))
final_num=float(inchToCenti (num))
print("\t=> %.2f cm" %final_num)
