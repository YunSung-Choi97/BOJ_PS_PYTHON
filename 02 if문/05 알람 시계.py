H, M = map(int, input().split())  # H, M : 일어날 시간을 입력받는다 (상근이가 설정해 놓은 알람시간)

# 설정할 알람 시각을 구함
if M >= 45:  # 45분보다 작은 경우에는 시간이 변하기 때문에 우선 조건으로 따져줌
    print(H, M-45)
else:
    if H == 0:  # 시간에서 1을 빼주어야 하는데 0시에서는 23로 바꿔주어야하므로 예외 처리
        print(23, M+15)
    else:
        print(H-1, M+15)