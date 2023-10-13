users=[]
newuser={
    'last': 'fatima',
    'first': 'alishba',
    'username': 'alishbafatima',
 }

users.append(newuser)

newuser = {
    'last': 'fatima',
    'first': 'urooj',
    'username': 'uroojfatima',
 }
users.append(newuser)

for userdict in users:
    for k , v in userdict.items():
        print(k + ": " + v)
        print("\n")