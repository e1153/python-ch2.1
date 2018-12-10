# 치환문 예
a = 1
b =a+1
print(a, b, sep=',') # sep는 중간에 구분해주는 문자를 출력해줄수 있는 기능이다. 스트링 집어넣을수 있음

# 변수값 할당 오류
#1+ a = c

# 세미콜론으로 치환문을 구분할 수 있다.
e = 3.5; t = 5.3 # 한 줄에 이어 쓰고 싶을때 세미콜론 추가하면 사용 가능함
print(e, t)

# 여러 개를 한 번에 할당할 때 (추천)
e, f = 3.5, 5.3 # 위와 같이 세미콜론 없이도 여러개의 값을 추가 할 수 있음
print(e, f)

# 같은 값을 여러 변수에 할당할 때
x = y = z = 10
print(x, y, z)

# C 스타일은 지원하지 않는다.
#x = (y = 10)

print(e, f)
#e = f
#f = e
#print(e, f)
e, f = f, e
print(e, f)

# 동적 타이핑 : 변수에 새로운 값이 할당되면 기존의 값을 버리고
# 새로운 값으로 치환된다.

a = 1
print(type(a))
a = "hello"
print(type(a))

# 확장 치환문
a = 10
a += 10
print(a)

a -= 3
print(a)

a *= 3
print(a)

a /= 3
print(a)