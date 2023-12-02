file_path = '/Day 2 Input.txt'

import re

# 12 red cubes, 13 green cubes, and 14 blue cubes
with open(file_path, 'r') as file:
    total_amount,total_amount2 = 0,0
    for line in file:
        line = line.strip()
        game_id = line[:line.index(":")+1]
        game_id = game_id.replace("Game","").replace(":","")
        line_parse = line.replace(line[:line.index(":")+1],"")
        cubes = re.split('; |, ', line_parse)
        impossible = False
        blue_max, red_max, green_max = 0,0,0
        for x in cubes:
            if x.count("blue"):
                num_blue = int(x.replace(" blue",""))
                if num_blue > blue_max: blue_max = num_blue
                if num_blue > 14:impossible = True
            if x.count("red"):
                num_red = int(x.replace(" red",""))
                if num_red > red_max: red_max = num_red
                if num_red > 12:impossible = True
            if x.count("green"):
                num_green = int(x.replace(" green",""))
                if num_green > green_max: green_max = num_green
                if num_green > 13:impossible = True    
        if impossible == False:
            total_amount = total_amount + int(game_id)
        total_power = (red_max * green_max) * blue_max
        total_amount2 = total_amount2 + total_power

    print("Total Amount: " + str(total_amount))
    print("Total Power: " + str(total_amount2))
