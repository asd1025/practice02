# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여
# 출력하세요.

str = input('s = ')
split_str='/usr/local/bin/'
result2 = str.split(split_str)
result1 = str.split('/')
del result1[0]
del result2[0]
result2.insert(0,split_str)

print('실행 결과 :\n',result1)
print ('실행 결과 :\n', result2)