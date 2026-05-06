# 내장 모듈 : shelve(쉘브)
# 데이터를 영구적으로 저장하고 관리
import shelve

# 데이터 저장 : 딕셔너리 방식: data_file['키'] = 값 형태로 저장
with shelve.open('mydata') as data_file:
    data_file['과일'] = ['사과', '바나나', '딸기']
    data_file['숫자'] = [1, 2, 3, 4, 5]
    data_file['고객정보'] = {'이름': '홍길동', '나이': 30}
    data_file['아이디'] = "오리"
    data_file['비밀번호'] = "1234"

# 데이터 읽기 : JSON처럼 json.load()를 하고 형변환을 고민할 필요 없이, 마치 메모리에 살아있는 변수를 쓰는 것처럼 편하게 사용
with shelve.open('mydata') as data_file:
    print("과일:", data_file['과일'])
    print("숫자:", data_file['숫자'])
    print("고객정보:", data_file['고객정보'])
    print("아이디:", data_file['아이디'])
    print("비밀번호:", data_file['비밀번호'])