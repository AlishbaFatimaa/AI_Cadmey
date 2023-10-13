bannedusers=['eve', 'fred', 'gary', 'helen']
prompt="\nadd a player to your team."
prompt += "\nenter 'quiet' when you're done. "
players = []
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in bannedusers:
        print(player + " is banned!")
        continue
    else:
        players.append(player)
        print("\nyour team:")

for player in players:
    print(player)