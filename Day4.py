file_path = 'Day 4 Input.txt'
games_to_play = []
counter = 0

with open(file_path, 'r') as file:
    total_wins = 0
    for line in file:
        line = line.strip()
        game_id = line[:str(line).find(":")]
        numbers = line[str(line).find(":")+1:].split("|")
        games_to_play.append(line)
        point_value = 0
        card_numbers, winning_numbers = [], []
        for x in str(numbers[0]).replace("  "," ").split(" "):
            if x.isdigit():winning_numbers.append(x)

        for x in str(numbers[1]).replace("  "," ").split(" "):
            if x.isdigit():card_numbers.append(x)

        for x in card_numbers:
            if x in winning_numbers:
                point_value = point_value * 2
                if point_value == 0: point_value = 1
        total_wins += point_value

    print("Total Wins: " + str(total_wins))

while counter < len(games_to_play):
    game = games_to_play[counter]
    card_numbers,winning_numbers,round_wins = [],[],[]
    numbers = game[str(game).find(":")+1:].split("|")
    game_id = game[:str(game).find(":")]
    game_id = game_id.replace("Card ",'')

    for x in str(numbers[0]).replace("  "," ").split(" "):
        if x.isdigit():winning_numbers.append(x)

    for x in str(numbers[1]).replace("  "," ").split(" "):
        if x.isdigit():card_numbers.append(x)

    for x in card_numbers:
        if x in winning_numbers:
            round_wins.append(x)
    y = 1
    if len(round_wins) > 0:
        while y < len(round_wins) + 1:            
            games_to_play.append(games_to_play[int(game_id) + y - 1])
            y += 1
    counter += 1
print(len(games_to_play))
