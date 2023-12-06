def simulate_game(time, dist):
    game_wins = []
    button_press = 0
    while button_press < time:
        traveled = (time - button_press) * button_press
        if traveled > dist: game_wins.append(button_press)
        button_press += 1
    wins.append(len(game_wins))
    return game_wins

wins = []
num_wins = []
time = [53, 89, 76, 98]
dist = [313, 1090, 1214, 1201]

simulate_game(time[0],dist[0])
simulate_game(time[1],dist[1])
simulate_game(time[2],dist[2])
simulate_game(time[3],dist[3])
total_win = 1
for win in wins:total_win = total_win * win
print("part 1: " + str(total_win))

time = 53897698
dist = 313109012141201
print("part 2: " + str(len(simulate_game(time,dist))))
