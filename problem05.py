# 문제5
# 함수 sum을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다

def sum(*num) :
    sum =0
    for i in num :
        sum+=i
    return sum

print(sum(0))