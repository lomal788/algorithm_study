def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        param = str(bin(i | j))[2: ]
        param = '0' * (n - len(param)) + param
        param = param.replace('1','#')
        param = param.replace('0',' ')
        answer.append(param)
    return answer

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))