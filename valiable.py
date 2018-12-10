# 변수 이름은 문자, 숫자, _ 로 구성된다.
import keyword

friend = 1  # ;세미콜론은 한줄짜리일경우 안달아도 괜찮음
my_name = "이다운" # 파이썬은 낙타표기법 안쓰고 _로 주로 표시하곤함
_yourName = "둘리"
member1 = "도우너"
long_string = """
첫번째 라인
두번째 라인
세번째 라인
"""

# 에러 : 다른 구성의 변수 이름은 사용할 수 없음
#friend$ = 1 $는 변수 선언 불가
#a! =10 !는 변수 선언 불가함
# 1member =10 변수 앞에 숫자가 붙는건 불가능함.

# 에러 : 예약어는 변수 이름으로 사용할 수 없다.
#def = 1 def는 예약어임

print(keyword.kwlist) # import 하는 방법 Alt + Enter
print(len(keyword.kwlist)) # len은 길이를 뜻함

# 한글 이름의 변수도 가능함

가격1 = 2000
print(가격1-200)