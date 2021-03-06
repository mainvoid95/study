def solution(n):
    a, b = 0,1
    for i in range(n):
        a , b = b , a + b
    return a % 1234567

    

#     피보나치 수
# 문제 설명
# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

# 예를들어

# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.

# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

# 제한 사항
# * n은 1이상, 100000이하인 자연수입니다.

# 함수를 쓰거나 재귀를 쓰는경우 런타임에러나 시간초과가 발생한다. (아마도 입력값으로 들어오는 숫자가 커서 그런거 같음)
# 피보나치를 구할때 어차피 그전에 있는 수가 있으면 연산하는데 시간이 줄어드니까 저런방식으로 구할수 있다는것를 검색해서 찾았당
# 파이썬은 교환함수가 따로없고 저렇게 변수를 교환시킬수 있음으로 더 짧게 구현가능