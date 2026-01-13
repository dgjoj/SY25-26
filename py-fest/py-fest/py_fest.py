# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

# 1. Add the headliner
headliner = ("The Byte Beats", "Synthwave", 90)
lineup.append(headliner)

# Continue the logic below...

print(lineup)




print("1. View Lineup & Total Time")
print("2. Add a new band")
print("3. Move first band to end(late arrival)")
print("4. Remove a band by name")
print("5. Move band to Specific Position.")
print("6. Exit")
choice = int(input("Choose an option (1-6): "))

