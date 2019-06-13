# 문제3.
# 1)다음 문자열을 모든 소문자를 대문자로 변환하고,
# 문자 ',' '.'  '\n' 를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.


s= '''
 
We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors 
through the process. 

'''

str=s.upper()
str=str.replace(',','').replace('.','').replace('\n','').split()
d={}
for word in str :
     d.update( {word:d.setdefault(word,0)+1})
d= sorted(d.items())
for i in d :
    print("{0}:{1}".format(i[0],i[1]))