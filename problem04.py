# 문제4
# 반목문을 이용해 369게임에서 박수를 쳐야하는 경우의 수를 순서대로 화면에 출력해보세요
# 1~99까지

clap = (3,6,9)
for  num in range(3,100) :
    cnt = 0
    i = num
    while i!=0 :
        if ( i%10 in clap) :
            cnt+=1
        i=i//10

    cnt!=0 and  print(num,' ','짝'*cnt)
