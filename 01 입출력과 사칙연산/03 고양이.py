# 큰 따옴표로 표현된 문자열 내에 있는 큰 따옴표 앞에는 \를 붙여주어야 한다
# 작은 따옴표로 표현된 문자열 내에 있는 작은 따옴표 앞에는 \를 붙여주어야 한다.
# 큰 따옴표/작은 따옴표로 표현된 문자열 내에 있는 작은 따옴표/큰 따옴표로 표현된 문자는 그냥 출력된다.
# 출력할 문자열이 \라면 일반적으로 \\로 표현해주어야 한다. (뒤에 글자가 ', ", n, t 등의 표현일 수 있기때문에)
# 문자열의 마지막 글자로 혹은 줄바꿈 앞에 \를 표현할 때에도 \\로 표현해주어야한다.
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")  # print안의 문자열을  \\(__)| 로 바꾸더라도 동일한 결과 출력

# print함수 내에서 """출력할 문자열"""의 형태로 사용하게 되면 여러줄의 출력물의 출력할 수 있다.
# print("""\    /\\
#  )  ( ')
# (  /  )
#  \(__)|""")
