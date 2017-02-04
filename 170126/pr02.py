import re           # Regular Expression 모듈

# 테스트용 문자열 저장
text = 'My id number is [G203_5A]'

print(re.findall('a', text))
print(re.findall('A', text))
print(re.findall('i', text))
# 소문자 찾기
print(re.findall('[a-z]', text))
# 소문자 연속해서 찾기
print(re.findall('[a-z]+', text))
# 대문자 찾기
print(re.findall('[A-Z]', text))
# 숫자 찾기
print(re.findall('[0-9]', text))
# 숫자 연속해서 찾기
print(re.findall('[0-9]+', text))
# 영문자 및 숫자 찾기
print(re.findall('[a-zA-Z0-9]',text))
# 영문자 및 숫자 연속해서 찾기
print(re.findall('[a-zA-Z0-9]+',text))
# 영문자/숫자 아닌 문자 찾기
print(re.findall('[^a-zA-Z0-9]',text))
# 영문자 및 '_' 특수기호 찾기
print(re.findall('[\w]', text))
# 영문자 및 '_' 특수기호 연속해서 찾기
print(re.findall('[\w]+', text))
# 영문자 및 '_' 특수기호 아닌 문자 찾기
print(re.findall('[^\w]', text))

