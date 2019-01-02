def solution(N, stages):
    answer = []
    slist = {}
    dlist = {}
    sortlist = []
    
    stages = sorted(stages)
    for n in range(1,N+1):
        slist[n] = 0
        dlist[n] = 0
        for s in stages:
            if( s > n):
                slist[n] = slist[n] + 1
            if( s == n ):
                dlist[n] = dlist[n] + 1
        if slist[n] + dlist[n] > 0 :
            slist[n] = float(dlist[n]) / float(slist[n]+dlist[n])
    answer = sorted(slist, key=lambda k : slist[k], reverse=True)
    
    return answer

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n,stages))
n = 4
stages = [4, 4, 4, 4, 4]
print(solution(n,stages))