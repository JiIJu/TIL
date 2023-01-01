# HSAT 근무시간

data= []
for i in range(5):
    start , end = input().split()
    start = start.split(':')
    end = end.split(':')
    data.append((start,end))
ans_hour , ans_min = 0,0
for start,end in data:
    start_hour ,start_min = start
    end_hour , end_min = end
    start_hour, start_min,end_hour , end_min = int(start_hour), int(start_min),int(end_hour) , int(end_min)
    ans_hour += end_hour-start_hour
    ans_min += end_min - start_min

ans = ans_hour*60 + ans_min
print(ans)