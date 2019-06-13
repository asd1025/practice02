# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여
# 출력하세요.

s = '/usr/local/bin/python'

result2 = s.rsplit('/',1)
result1 = s.split('/')
del result1[0]

print('실행 결과 :\n',result1)
print ('실행 결과 :\n', result2)