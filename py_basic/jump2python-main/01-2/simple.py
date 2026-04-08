languages = ['python', 'javascript', 'perl', 'c', 'c#', 'c++', 'java']

# 주석 : ctrl+/
# 파이썬은 문장 구분을 들여쓰기로 한다.
for lang in languages:
    if lang in ['python', 'javascript', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'c#', 'c++', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")
