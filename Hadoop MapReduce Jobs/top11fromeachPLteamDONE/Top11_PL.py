#python code original

import csv

# Define the path to the CSV file
filename = "C:/Users/Ummad/Downloads/archive/split_files/extracted.csv"

# Define the list of player names to search for
names = ["Philip Billing", "Dominic Solanke", "Lewis Cook", "Lloyd Kelly", "Jaidon Anthony", "Ryan Christie", "Marcus Tavernier", "Ryan Fredericks", "Jack Stephens", "Mark Travers", "Jack Stacey", "Bukayo Saka", "Martin Ødegaard", "Emile Smith Rowe", "Thomas Partey", "Aaron Ramsdale", "Kieran Tierney", "Alexandre Lacazette", "Granit Xhaka", "Oleksandr Zinchenko", "Nicolas Pépé", "Rob Holding", "Lucas Digne", "Emiliano Buendía", "Matty Cash", "John McGinn", "Jacob Ramsey", "Ollie Watkins", "Tyrone Mings", "Morgan Sanson", "Frédéric Guilbert", "Leander Dendoncker", "Kortney Hause", "Ivan Toney", "Thomas Strakosha", "Bryan Mbeumo", "Ben Mee", "Rico Henry", "Vitaly Janelt", "Mathias Jensen", "Yoane Wissa", "Keane Lewis-Potter", "Kevin Schade", "Pontus Jansson", "Leandro Trossard", "Alexis Mac Allister", "Lewis Dunk", "Enock Mwepu", "Tariq Lamptey", "Pascal Groß", "Deniz Undav", "Jürgen Locadia", "Adam Webster", "Billy Gilmour", "Steven Alzate", "Antonio Rüdiger", "N'Golo Kanté", "Raheem Sterling", "Reece James", "Édouard Mendy", "Mason Mount", "Timo Werner", "Christian Pulisic", "Kalidou Koulibaly", "Ben Chilwell", "Hakim Ziyech", "Wilfried Zaha", "Michael Olise", "Joachim Andersen", "Eberechi Eze", "Tyrick Mitchell", "Odsonne Édouard", "Jean-Philippe Mateta", "Jeffrey Schlupp", "Will Hughes", "Sam Johnstone", "Gary Cahill", "Jordan Pickford", "Dominic Calvert-Lewin", "Ben Godfrey", "James Tarkowski", "Conor Coady", "Demarai Gray", "Michael Keane", "Dwight McNeil", "Neal Maupay", "Alex Iwobi", "Tom Davies", "Jean Michaël Seri", "Manor Solomon", "Bernd Leno", "Issa Diop", "Harry Wilson", "Alfie Mawson", "Marek Rodák", "Antonee Robinson", "Harrison Reed", "Bobby De Cordova-Reid", "Layvin Kurzawa", "Illan Meslier", "Patrick Bamford", "Jack Harrison", "Pascal Struijk", "Robin Koch", "Maximilian Wöber", "Joe Gelhardt", "Luke Ayling", "Liam Cooper", "Stuart Dallas", "Crysencio Summerville", "Youri Tielemans", "James Maddison", "Jamie Vardy", "Patson Daka", "Ademola Lookman", "Timothy Castagne", "Dennis Praet", "Kiernan Dewsbury-Hall", "James Justin", "Boubakary Soumaré", "Daniel Amartey", "Sadio Mané", "Trent Alexander-Arnold", "Virgil van Dijk", "Andrew Robertson", "Ibrahima Konaté", "Joe Gomez", "Jordan Henderson", "Naby Keïta", "Xherdan Shaqiri", "Curtis Jones", "Konstantinos Tsimikas", "Kevin De Bruyne", "Aymeric Laporte", "Jack Grealish", "Riyad Mahrez", "Kyle Walker", "Julián Álvarez", "John Stones", "Nathan Aké", "Zack Steffen", "Issa Kaboré", "Philippe Sandler", "Paul Pogba", "Jadon Sancho", "Marcus Rashford", "Raphaël Varane", "Luke Shaw", "Scott McTominay", "Anthony Martial", "Tyrell Malacia", "Aaron Wan-Bissaka", "Donny van de Beek", "Harry Maguire", "Sven Botman", "Alexander Isak", "Allan Saint-Maximin", "Kieran Trippier", "Nick Pope", "Dan Burn", "Matt Targett", "Sean Longstaff", "Jonjo Shelvey", "Martin Dúbravka", "Ryan Fraser", "Moussa Niakhaté", "Jesse Lingard", "Orel Mangala", "Cheikhou Kouyaté", "Loïc Badé", "Joe Worrall", "Ryan Yates", "Scott McKenna", "Giulian Biancone", "Sam Surridge", "Harry Toffolo", "James Ward-Prowse", "Kyle Walker-Peters", "Romain Perraud", "Stuart Armstrong", "Moussa Djenepo", "Nathan Redmond", "Adam Armstrong", "Yan Valery", "Ainsley Maitland-Niles", "Sékou Mara", "Mateusz Lis", "Harry Kane", "Dejan Kulusevski", "Giovani Lo Celso", "Yves Bissouma", "Eric Dier", "Oliver Skipp", "Pierluigi Gollini", "Djed Spence", "Harry Winks", "Hugo Lloris", "Japhet Tanganga", "Declan Rice", "Gianluca Scamacca", "Jarrod Bowen", "Nayef Aguerd", "Vladimír Coufal", "Michail Antonio", "Manuel Lanzini", "Craig Dawson", "Alex Král", "Arthur Masuaku", "Flynn Downes"] # Replace with actual names

# Create an empty list to store the player data
players = []

# Open the CSV file and read in the data
with open(filename, 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Check if the player's name is in the list of names
        if row['long_name'] in names:
            players.append(row)

# Remove duplicates based on long_name
new_players = []
long_names = set()
for player in players:
    if player['long_name'] not in long_names:
        new_players.append(player)
        long_names.add(player['long_name'])

# Write the player data to a new CSV file
output_filename = "C:/Users/Ummad/Downloads/archive/split_files/player_attributes.csv"
with open(output_filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(new_players[0].keys())
    for player in new_players:
        writer.writerow(player.values())
