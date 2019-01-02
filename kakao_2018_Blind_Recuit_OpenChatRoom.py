def solution(record):
    answer = []
    user = {}
    for r in record:
        status = r.split(' ')[0]
        if status in ['Enter','Change']:
            user[r.split(' ')[1]] = r.split(' ')[2]
    
    for r in record:
        status = r.split(' ')[0]
        name = user[r.split(' ')[1]]
        if(status == 'Enter'):
            answer.append(name+"님이 들어왔습니다.")
        elif(status == 'Leave'):
            answer.append(name+"님이 나갔습니다.")
            
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))