def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age

    return person

artist = build_person('alishba', 'fatima', 19)
print(artist)
artist = build_person('urooj', 'fatima')
print(artist)