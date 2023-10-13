favlanguages = {'jen': ['python', 'ruby'], 'sarah': ['c'], 'edwerd': ['ruby', 'go'], 'phill': ['python', 'haskell']}
for name, langs in favlanguages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)