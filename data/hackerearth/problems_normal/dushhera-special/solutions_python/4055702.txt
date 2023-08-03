def main():
    t = int(raw_input())    
    p_k = []
    r = 1
    N = []
    N_len = 0
    while t != 0:    
        t = t - 1
        p_k = map(int,raw_input().split())
        if len(p_k) == 2:
            r = 1
            r = r + p_k[1]       
            N = []
            for i in range(1,(p_k[0]+1)):
                N.append(r * i)
            N_result = ''  
            for i in range(0,len(N)):
                if i == 0:
                    N_result = N_result + str(N[i])
                else:
                    N_result = N_result + ' ' + str(N[i])
            print N_result    
                
            
                
                
   
if __name__ == '__main__':
    main()  
