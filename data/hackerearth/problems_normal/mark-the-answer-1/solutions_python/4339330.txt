Q_D = map(int,raw_input().split())
skip = 0
attempt = 0

if len(Q_D) == 2:
    Q = map(int,raw_input().split())
    if len(Q) == Q_D[0]:        
        for i in Q:
            if skip == 2:
                break
            else:
                if i <= Q_D[1]:
                    attempt = attempt + 1
                else:
                    skip = skip + 1
       
    print attempt
