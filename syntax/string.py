# print(Hello world) -> error 발생
print('Hello world')
print("Hello world")

# 큰따옴표, 작은따옴표 둘다 사용가능하지만 섞어서 사용할 순 없다.
# 작은따옴표를 사용하는 빈도가 더 높다.

print("Hello'o' world")
# 위와 같이 작은따옴표를 문자로 쓰고 싶다면 큰따옴표로 감싸면 된다.(반대 경우도 동일)

print("Hell'o' \"w\"orld")
# \(역슬래쉬)를 쓰면 '어떤한 기능을 수행하는 문자'가 아닌 문자 그대로의 사용된다.
# \는 'escape'라고 한다.

# newline 줄바꿈하는 방법(아래 두 방법은 동일하다)
print('H')
print('e')
print('l')
print('l')
print('o')

print('H\ne\nl\nl\no')


# docstring 여러 줄의 문장을 표현할 경우
print('''
H
e
l
l
o
''')
