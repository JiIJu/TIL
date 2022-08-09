def hanoi(N, start, to, via):
    if N == 1:
        print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮깁니다.".format(N, start, to))
    else:
        hanoi(N-1, start, via, to)
        print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮깁니다.".format(N, start, to))
        hanoi(N-1, via, to, start)hanoi(3, 'A', 'C', 'B')