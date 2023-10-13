aliens=[]

for aliennum in range(100):
    newalien = {}
    newalien['color'] = 'green'
    newalien['points'] = 5
    newalien['x'] = 20 * aliennum
    newalien['y'] = 7 * int(newalien['x'])
    aliens.append(newalien)


# Prove the list contains a million aliens.
numaliens = len(aliens)
print("Number of aliens created:")
print(numaliens)
print(aliens)