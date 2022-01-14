
#숫자는 num에 연산 기호는 operation에 저장한다.
num1=float(input())
operation=input()
num2=float(input())


#조건문을 통해 operation에 입력받은 연산기호에 따라 결과값 출력
if(operation=='+'):
	print('a : 수행할 연산자(+, -, *, /): b : a '+operation+' b =',(num1+num2))
elif(operation=='-'):
	print('a : 수행할 연산자(+, -, *, /): b : a '+operation+' b =',(num1-num2))
elif(operation=='*'):
	print('a : 수행할 연산자(+, -, *, /): b : a '+operation+' b =',(num1*num2))
else:
	print('a : 수행할 연산자(+, -, *, /): b : a '+operation+' b =',(num1/num2))
	











