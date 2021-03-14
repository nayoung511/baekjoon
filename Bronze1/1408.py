import datetime

def main():
    now = str(input())
    goal = str(input())

    #list로 변환 
    now = now.split(':')
    now = [int(i) for i in now]
    goal = goal.split(':')
    goal = [int(i) for i in goal]

    start_time = now[0] * 3600 + now[1] * 60 + now[2]

    if(goal[0] < now[0]):
        goal_time = (goal[0] * 3600) + 86400 + goal[1] * 60 + goal[2]
    else:
       goal_time = goal[0] * 3600 + goal[1] * 60 + goal[2]

    answer = goal_time - start_time

    answer = str(datetime.timedelta(seconds=answer)).zfill(8)

    print(answer)


""""
    start_time = datetime.time(now[0], now[1], now[2])
    
    #goal time이 다음 날 새벽일 경우
    if(goal[0] < now[0]):
        goal_time = datetime.timedelta(hours=goal[0] + 24, minutes=goal[1], seconds = goal[2])
    else:
        goal_time = datetime.time(goal[0], goal[1], goal[2])


    print(goal_time)


    date = datetime.date(1,1,1)
    start_time = datetime.datetime.combine(date, start_time)
    #goal_time = datetime.datetime.combine(date, goal_time)

    

    answer = str(goal_time - start_time).zfill(8)

    print(answer)
"""
main()