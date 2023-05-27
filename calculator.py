def mul(a,b):
        result = a * b
        return result
def div(a, b):
        result = a / b
        return result
def add(a, b):
        result = a + b
        return result
def minus(a, b):
        result = a - b
        return result

formula = input("----이 계산기는 띄어쓰기를 기점으로 수식을 인식합니다 띄어쓰기로 구분을 해주세요---- \n곱하기,나누기를 포함한 연산을 한다면 먼저 작성해주세요.  ---> ")
f =  formula.split(" ")
print("계산을 시작합니다.")
total = int(f[0])
a = 0
b = 0
for i in range((len(f)-1)//2) :
    if f[1+2*i] == "+":
        total = add(total,int(f[2+2*i]))
    elif f[1+2*i] == "-":
        total = minus(total,int(f[2+2*i]))
    elif f[1+2*i] == "*":
        total = mul(total,int(f[2+2*i]))
    elif f[1+2*i] == "/":
        total = div(total,int(f[2+2*i]))
    else :
        print("지원하지 않는 수식입니다.")
print(total)