input_data = input()

row = int(input_data[1])

# ord를 사용하면 해당 문자의 ASCII 코드로 반환을 해준다
# 지금 현재 문자들이 소문자로 들어오기에 뒤에 a의 아스키코드를 빼준다
# 예를 들면 앞에 h가 들어오면 ord(h) 시 104가 반환되고 a의 아스키 코드 97을 빼 a가 0부터일 때 7번째 숫자임을 보여준다
column = int(ord(input_data[0])) - int(ord('a')) + 1

