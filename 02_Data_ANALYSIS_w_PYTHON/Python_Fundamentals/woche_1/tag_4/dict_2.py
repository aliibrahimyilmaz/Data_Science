player = {} # leeres Dict erzeugen
player['name'] = 'Bernd'
player['points'] = 0
player['points'] = 10  # Keys werden überschrieben

print(player)

# Prüfen ob key in player vorhanden
if 'points' in player:
    print(player['points'])

# bessere Methode, auf ein Element zuzugreifen
points = player.get('points', 0)  # Defaultwert ist 0
print('points from get(): ', points)

# mehrere Spieler in einem Dict verwalten
players = {
    'markus': {'points': 100, 'life': 3},
    'bernd': {'points': 10, 'life': 1},
}


