time, team1, team2 = map(int, input().split())

left_time = 90 - time
if left_time % 5 ==0:
    team1 = team1 + (left_time // 5)
else:
    team1 = team1 + (left_time // 5) + 1
    
if team1 == team2:
    print("same")
elif team1 > team2:
    print("win")
else:
    print("lose")