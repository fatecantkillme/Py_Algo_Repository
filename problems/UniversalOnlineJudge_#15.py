def main():
    N,A,B=tuple(int(x) for x in input().split())
    data_A=[int(x) for x in input().split()]
    data_B=[int(x) for x in input().split()]
    Score_A=0
    Score_B=0
    for i in range(N):
        i_A=(i+1)%A-1 if (i+1)%A != 0 else A-1
        i_B=(i+1)%B-1 if (i+1)%B != 0 else B-1
        if data_A[i_A] == 0:
            if data_B[i_B] == 1 or data_B[i_B] == 4:
                Score_B += 1
            elif data_B[i_B] == 2 or data_B[i_B] == 3:
                Score_A += 1
        elif data_A[i_A] == 1:
            if data_B[i_B] == 0 or data_B[i_B] == 3:
                Score_A += 1
            elif data_B[i_B] == 2 or data_B[i_B] == 4:
                Score_B += 1
        elif data_A[i_A] == 2:
            if data_B[i_B] == 1 or data_B[i_B] == 4:
                Score_A += 1
            elif data_B[i_B] == 0 or data_B[i_B] == 3:
                Score_B += 1
        elif data_A[i_A] == 3:
            if data_B[i_B] == 0 or data_B[i_B] == 1:
                Score_B += 1
            elif data_B[i_B] == 2 or data_B[i_B] == 4:
                Score_A += 1
        elif data_A[i_A] == 4:
            if data_B[i_B] == 0 or data_B[i_B] == 1:
                Score_A += 1
            elif data_B[i_B] == 3 or data_B[i_B] == 2:
                Score_B += 1
    print(Score_A,Score_B)

main()