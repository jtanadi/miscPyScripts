names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
locations = ["Gotham", "Smallville", "New York City", "Salem Center", "Vancouver"]

print zip(names, heroes, locations)

zipDict = {name: hero for name, hero in zip(names, heroes)}

print zipDict

lenDict = {names[i]: heroes[i] for i in range(len(names))}

print lenDict