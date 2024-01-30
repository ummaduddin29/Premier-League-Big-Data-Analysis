#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

player_name = ["Brenden Aaronson", "Zach Abbott", "Terry Ablade", "Tammy Abraham", "Adam Armstrong", "Adama Traoré", "Tyler Adams", "Tosin Adarabioyo", "Tayo Adaramola", "Joshua Addae", "Simon Adingra", "Adrián", "Daniel Adu-Adjei", "Nayef Aguerd", "Brandon Aguilera", "Naouirou Ahamada", "Rayan Aït-Nouri", "Kristoffer Ajer", "Manuel Akanji", "Nathan Aké", "Victor Akinwale", "Marc Albrighton", "Carlos Alcaraz", "Ryan Alebiosu", "Ajibola Alese", "Álex Moreno", "Alex Telles", "Trent Alexander-Arnold", "Alisson", "Allan", "César Azpilicueta", "Kwadwo Baah", "Abdul Rahman Baba", "Daniel Bachmann", "Leon Bailey", "Eric Bailly", "Tiémoué Bakayoko", "Lewis Baker", "James Balagizi", "Fabián Balbuena", "Ellery Balcombe", "Gareth Bale", "Folarin Balogun", "Tudor Baluta", "Patrick Bamford", "Beni Baningime", "Scott Banks", "Shandon Baptiste", "Daniel Barden", "Phil Bardsley", "Ross Barkley", "Ashley Barnes", "Mason Barrett", "Louie Barry", "Lewis Bate", "Michy Batshuayi", "Nathan Baxter", "Mads Bech Sørensen", "Owen Beck", "Jan Bednarek", "Charlie Allen", "Max Alleyne", "Dele Alli", "Miguel Almirón", "Marcos Alonso", "Julián Álvarez", "Álvaro Fernández", "William Alves", "Steven Alzate", "Daniel Amartey", "Ethan Ampadu", "Joseph Anang", "Joachim Andersen", "Joseph Anderson", "Florin Andone", "André Gomes", "Andreas Pereira", "Andrey Santos", "Faustino Anjorin", "Jaidon Anthony", "Antonee Robinson", "Michail Antonio", "Antony", "Paul Appiah", "Keenan Appiah-Forson", "Billy Arce", "Cameron Archer", "Alphonse Aréola", "Joe Aribo", "Stuart Armstrong", "Kepa Arrizabalaga", "Harry Arter", "Arthur", "Harrison Ashby", "Ashley Young", "Ryan Astley", "Pierre-Emerick Aubameyang", "Ludwig Augustinsson", "Sèrge Aurier", "Brandon Austin", "Zach Awe", "Taiwo Awoniyi", "Yasin Ayari", "Jordan Ayew", "Luke Ayling", "Miguel Azeez", "César Azpilicueta", "Abdul Rahman Baba", "Baba Fernandes", "Finley Back", "Loïc Badé", "Benoît Badiashile", "Leon Bailey", "Eric Bailly", "Stefan Bajcetic", "Tiémoué Bakayoko", "Lewis Baker", "James Balagizi", "Ellery Balcombe", "Dominic Ballard", "Kofi Balmer", "Folarin Balogun", "Tudor Baluta", "Patrick Bamford", "Mauro Bandeira", "Scott Banks", "Shandon Baptiste", "Ross Barkley", "Harvey Barnes", "Louie Barry", "Ryan Bartley", "Lewis Bate", "Michy Batshuayi", "Nathan Baxter", "Gavin Bazunu", "Eddie Beach", "Mads Bech Sørensen", "Owen Beck", "Jan Bednarek", "Asmir Begovic", "Armel Bella-Kotchap", "Héctor Bellerín", "Filip Benkovic", "Rhys Bennett", "Saïd Benrahma", "Rodrigo Bentancur", "Christian Benteke", "Daniel Bentley", "Lucas Bergström", "Steven Bergwijn", "Di'Shon Bernard", "Bernardo Silva", "Ryan Bertrand", "Marcus Bettinelli", "Owen Bevan", "Giulian Biancone", "Mads Bidstrup", "Mika Biereth", "Philip Billing", "Nathan Bishop", "Yves Bissouma", "Harvey Blair", "David Boateng", "Oscar Bobb", "Lamare Bogarde", "Mateusz Bogusz", "Bendegúz Bolla", "Willy Boly", "Gaëtan Bong", "Sven Botman", "Jamie Bowden", "Jarrod Bowen", "Josh Bowler", "Conor Bradley", "Robert Brady", "Jarrad Branthwaite", "Sammy Braybrooke", "James Bree", "Nathan Broadhead", "Armando Broja", "Josh Brooking", "David Brooks", "Bruno Fernandes", "Bruno Guimarães", "Bruno Jordão", "Lewis Brunt", "Joe Bryan", "Emiliano Buendía", "Hugo Bueno", "Facundo Buonanotte", "Dan Burn", "Finley Burns", "Mason Burstow", "Jack Butland", "Nathan Butler-Oyedeji", "Willy Caballero", "Maliq Cadogan", "Cafú", "Gary Cahill", "Moisés Caicedo", "Jake Cain", "Tom Cairney", "Duje Caleta-Car", "Dominic Calvert-Lewin", "Leonardo Campana", "Vontae Campbell", "Thomas Cannon", "Sergi Canós", "Todd Cantwell", "Elia Caprile", "Cardo Siddik Afraciab", "Carlos Borges", "Carlos Vinícius", "Scott Carson", "Cameron Carter-Vickers", "Cesare Casadei", "Casemiro", "Kaelan Casey", "Matty Cash", "Timothy Castagne", "Edinson Cavani", "Cédric Soares", "Kallum Cesay", "Trevoh Chalobah", "Calum Chambers", "Shea Charles", "Charlie Robinson", "Kgaogelo Chauke", "Daniel Chesters", "Jeremiah Chilokoa-Mullen", "Ben Chilwell", "Chiquinho", "Tahith Chong", "Hamza Choudhury", "Ben Chrisene", "Andreas Christensen", "Christian Marques", "Ryan Christie", "Harry Christy", "Carney Chukwuemeka", "Catalin Cirjan", "CJ Egan-Riley", "Bobby Clark", "Matt Clarke", "Leighton Clarkson", "Regan Clayton", "Nathaniel Clyne", "Conor Coady", "Jack Colback", "Séamus Coleman", "Nathan Collins", "Levi Colwill", "Aaron Connolly", "Lewis Cook", "Liam Cooper", "Theo Corbeanu", "Dominic Corness", "Maxwel Cornet", "Vladimír Coufal", "Conor Coventry", "Brandon Cover", "Matthew Cox", "Amario Cozier-Duberry", "Michael Craig", "Tristan Crama", "Billy Crellin", "Charlie Cresswell", "Cristiano Ronaldo", "Marc Cucurella", "Luke Cundle", "Patrick Cutrone", "Luciano D'Auria-Henry", "Michael Dacosta Gonzalez", "Patson Daka", "Dale Taylor", "Stuart Dallas", "Mikkel Damsgaard", "Daniel Podence", "Danilo", "Arnaut Danjuma", "Karl Darlow", "Josh Dasilva", "David Datro Fofana", "Tom Davies", "Keinan Davis", "Craig Dawson", "Laurens De Bock", "Lucas De Bolle", "Kevin De Bruyne", "Bobby De Cordova-Reid", "David de Gea", "James Debayo", "Liam Delap", "Fabian Delph", "Siriki Dembélé", "Leander Dendoncker", "Will Dennis", "Halil Dervisoglu", "Alfie Devine", "Kiernan Dewsbury-Hall", "Amad Diallo", "Luis Díaz", "Tyler Dibling", "William Dickson", "Diego Carlos", "Diego Costa", "Diego Rosa", "Eric Dier", "Lucas Digne", "Diogo Dalot", "Diogo Jota", "Diogo Monteiro", "Issa Diop", "Elijah Dixon-Bonner", "Moussa Djenepo", "Ben Doak", "Lewis Dobbin", "Matt Doherty", "Jamie Donley", "Aaron Donnelly", "Alfie Dorrington", "Cheick Doucouré", "Douglas Luiz", "Flynn Downes", "Tommy Doyle", "Cody Drameh", "Martin Dúbravka", "Shane Duffy", "Paul Dummett", "Lewis Dunk", "Jhon Durán", "Malcolm Ebiowei", "Ederson", "Odsonne Édouard", "Samuel Edozie", "Khayon Edwards", "Pierre Ekwah", "Anwar El Ghazi", "Anthony Elanga", "Benjamin Elliott", "Mohamed Elyounoussi", "Noam Emeran", "Emerson", "Emerson Royal", "Julio Enciso", "Christian Eriksen", "Pervis Estupiñán", "Jonny Evans", "Oliver Ewing", "Eberechi Eze", "Lukasz Fabianski", "Fabinho", "Fábio Carvalho", "Fábio Silva", "Fábio Vieira", "Fabri", "Wout Faes", "Malachi Fagan-Walcott", "Josh Feeney", "Felipe", "Evan Ferguson", "Enzo Fernández", "Fernandinho", "Billy Fewster", "Ryan Finnigan", "Junior Firpo", "William Fish", "Ethan Fitzhugh", "Marcelo Flores", "Shane Flynn", "Phil Foden", "Wesley Fofana", "Taylor Foran", "Michael Forbes", "Tyrese Fornah", "Pablo Fornals", "Adam Forshaw", "Marcus Forss", "Fraser Forster", "Marlon Fossey", "Tariqe Fosu-Henry", "Chris Francis", "Tyrese Francois", "Ryan Fraser", "Melkamu Frauendorf", "Fred", "Ryan Fredericks", "Tyler Fredricson", "Remo Freuler", "James Furlong", "Gabriel Jesus", "Gabriel Magalhães", "Gabriel Martinelli", "Cody Gakpo", "Conor Gallagher", "Tomas Galvez", "Alejandro Garnacho", "James Garner", "Dwight Gayle", "Paulo Gazzaniga", "Jean-Philippe Gbamin", "Joe Gelhardt", "Brooklyn Genesini", "Saman Ghoddos", "Morgan Gibbs-White", "Lewis Gibson", "Alexander Gibson-Hammond", "Tarik Gidaree", "Bryan Gil", "Alex Gilbert", "Alfie Gilchrist", "Ryan Giles", "Mark Gillespie", "Billy Gilmour", "Ryan Glover", "Wilfried Gnonto", "Ben Godfrey", "Martial Godo", "Pierluigi Gollini", "Claudio Gomes", "Joe Gomez", "Gonçalo Guedes", "Charlie Goode", "Owen Goodman", "Lewis Gordon", "Daniel Gore", "Lewis Grabban", "Hubert Graczyk", "Lee Grant", "Demarai Gray", "Jack Grealish", "Ben Greenwood", "Seán Grehan", "Harvey Griffiths", "Pascal Groß", "Vicente Guaita", "Marc Guéhi", "Idrissa Gueye", "Frédéric Guilbert", "Ilkay Gündogan", "Patrik Gunnarsson", "Gustavo Scarpa", "Malo Gusto", "Darko Gyabi", "Erling Haaland", "Lewis Hall", "Oliver Hammond", "Reece Hannam", "Isak Hansen-Aaröen", "Riley Harbottle", "Bjorn Hardley", "Luke Harris", "Jack Harrison", "Taylor Harwood-Bellis", "Kortney Hause", "Kai Havertz", "Kaine Hayden", "Maxwell Haygarth", "Tom Heaton", "Michael Hector", "Krisztián Hegyi", "Karl Hein", "Hélder Costa", "Jordan Henderson", "Jeff Hendrick", "Wayne Hennessey", "Rico Henry", "Yangel Herrera", "Aaron Hickey", "James Hill", "James Hillson", "Jack Hinchy", "Jack Hinshelwood", "George Hirst", "Leo Hjelde", "Joseph Hodge", "Ki-Jana Hoever", "Rob Holding", "Mason Holgate", "Ethan Horvath", "Conor Hourihane", "Callum Hudson-Odoi", "Will Hughes", "Joe Hugill", "Bashir Humphreys", "Omari Hutchinson", "Hwang Hee-Chan", "Hwang Ui-Jo", "Pierre-Emile Højbjerg", "Bradley Ibrahim", "Kelechi Iheanacho", "Danny Ings", "Nicolas Ioannou", "Tim Iroegbunam", "Alexander Isak", "Ivan Cavaleiro", "Daniel Iversen", "Alex Iwobi", "Eldin Jakupovic", "Reece James", "Vitaly Janelt", "Pontus Jansson", "Julian Jeanvier", "Jack Jenkins", "Teddy Jenks", "Mathias Jensen", "Jeong Sang-Bin", "Raúl Jiménez", "João Cancelo", "João Félix", "João Gomes", "João Moutinho", "João Palhinha", "João Virgínia", "Joelinton", "Kyle John", "Brennan Johnson", "Sam Johnstone", "Curtis Jones", "Jonny", "Jorginho", "José Sá", "Juan Larios", "James Justin", "Issa Kaboré", "Kadan Young", "Sasa Kalajdzic", "Boubacar Kamara", "Harry Kane", "N'Golo Kanté", "Michal Karbownik", "Loris Karius", "Jadel Katongo", "Hayao Kawabe", "Kayky", "Moise Kean", "Michael Keane", "Neeskens Kebano", "Joshua Keeley", "Thilo Kehrer", "Naby Keïta", "Caoimhín Kelleher", "Lloyd Kelly", "Kenedy", "Nohan Kenneh", "Jonjoe Kenny", "Reda Khadra", "Kiko Casilla", "Gavin Kilkenny", "Maximilian Kilman", "Max Kinsey-Wellings", "Alex Kirk", "Jakub Kiwior", "Kristoffer Klaesson", "Mateusz Klich", "Ben Knight", "Anthony Knockaert", "Robin Koch", "Sead Kolasinac", "Ibrahima Konaté", "Terence Kongolo", "Ezri Konsa", "Kalidou Koulibaly", "Billy Koumetio", "Cheikhou Kouyaté", "Mateo Kovacic", "Matej Kovár", "Kacper Kozlowski", "Emil Krafth", "Alex Král", "Rasmus Kristensen", "Victor Kristiansen", "Dejan Kulusevski", "Garang Kuol", "Layvin Kurzawa", "Alexandre Lacazette", "Levi Laing", "Ethan Laird", "Adam Lallana", "Tariq Lamptey", "Daniel Langley", "Will Lankshear", 
               "Manuel Lanzini", "Aymeric Laporte", "Richie Laryea", "Jamaal Lascelles", "Roméo Lavia", "Marcel Lavinier", "Nico Lawrence", "Zan-Luk Leban", "Dexter Lembikisa", "Mario Lemina", "Clément Lenglet", "Bernd Leno", "Léo Bonatini", "Marc Leonard", "Jefferson Lerma", "Thakgalo Leshabela", "Rico Lewis", "Lewis Miley", "Keane Lewis-Potter", "Myles Lewis-Skelly", "Victor Lindelöf", "Hayden Lindley", "Jesse Lingard", "Mateusz Lis", "Tino Livramento", "Diego Llorente", "Hugo Lloris", "Giovani Lo Celso", "Jürgen Locadia", "Ruben Loftus-Cheek", "Joe Lolley", "Andy Lonergan", "Shane Long", "Emmanuel Longelo", "Sean Longstaff", "Ademola Lookman", "Jonas Lössl", "Jamal Lowe", "Luca Ashby-Hammond", "Lucas Moura", "Lucas Paquetá", "Luizão", "Romelu Lukaku", "Sasa Lukic", "Lyanco", "Lyle Taylor", "Brooklyn Lyons-Foster", "Isaac Mabaya", "Alexis Mac Allister", "James Maddison", "Noni Madueke", "Paris Maghoma", "Harry Maguire", "Riyad Mahrez", "Kobbie Mainoo", "Ainsley Maitland-Niles", "Malachi Boateng", "Tyrell Malacia", "Sadio Mané", "Orel Mangala", "Javier Manquillo", "Sékou Mara", "Marc Jurado", "Marçal", "Marcelo Pitaluga", "Solly March", "Emiliano Marcondes", "Pablo Marí", "Dilan Markanday", "Marquinhos", "Filip Marschall", "Anthony Martial", "David Martin", "Emiliano Martínez", "Arthur Masuaku", "Tawanda Maswanhise", "Juan Mata", "Jean-Philippe Mateta", "Matheus Cunha", "Matheus Nunes", "Nemanja Matic", "Joël Matip", "Matthew Craig", "Remi Matthews", "Matty Longstaff", "Neal Maupay", "Konstantinos Mavropanos", "Alfie Mawson", "Kevin Mbabu", "Loïc Mbe Soh", "Luke Mbete", "Bryan Mbeumo", "Xavier Mbuyamba", "James McArthur", "James McAtee", "Kasey McAteer", "Connor McAvoy", "Alfie McCalmont", "Liam McCarron", "Alex McCarthy", "Rowan McDonald", "Callum McFarlane", "Tom McGill", "John McGinn", "Scott McKenna", "Weston McKennie", "Stuart McKinstry", "Dwight McNeil", "Charlie McNeill", "Scott McTominay", "Ben Mee", "Hannibal Mejbri", "Édouard Mendy", "Teden Mengi", "Chris Mepham", "Illan Meslier", "Matt Miazga", "Alex Mighten", "Luka Milivojevic", "Amari Miller", "Stanley Mills", "James Milner", "Yerry Mina", "Takumi Minamino", "Tyrone Mings", "Tyrick Mitchell", "Kaoru Mitoma", "Aleksandar Mitrovic", "Jakub Moder", "Mohamed Elneny", "Mohamed Salah", "Zane Monlouis", "Jacob Montes", "Fionn Mooney", "Kieffer Moore", "Andrew Moran", "Pablo Moreno", "Jimmy Morgan", "Nathan Moriah-Welsh", "Tyler Morton", "Yerson Mosquera", "Malik Mothersille", "Louie Moulden", "Mason Mount", "Fabian Mrozek", "Divin Mubama", "Mykhailo Mudryk", "Marqes Muir", "Romaine Mundle", "Arijanet Muric", "Jacob Murphy", "Sam Murray", "Mateusz Musialowski", "Yoshinori Muto", "Enock Mwepu", "Vitalii Mykolenko", "Daniel N'Lundulu", "Marvelous Nakamba", "Adler Nascimento", "Keylor Navas", "Wilfred Ndidi", "Tanguy Ndombélé", "Reiss Nelson", "Nélson Semedo", "Neto", "Moussa Niakhaté", "Saúl Ñíguez", "Eddie Nketiah", "Niels Nkounkou", "Mark Noble", "James Norris", "Darwin Núñez", "Nuno da Costa", "Nuno Tavares", "Ethan Nwaneri", "Christian Nørgaard", "Jake O'Brien", "Ollie O'Neill", "Tommi O'Reilly", "Michael Obafemi", "Ademipo Odubeko", "Chituru Odunze", "Odeluga Offiah", "Angelo Ogbonna", "Mazeed Ogungbo", "Braian Ojeda", "Sheyi Ojo", "Armstrong Oko-Flex", "Ferdinand Okoh", "Arthur Okonkwo", "Ademola Ola-Adebomi", "Kazeem Olaigbe", "Michael Olakigbe", "Michael Olise", "Robin Olsen", "David Omilabu", "Tobi Omole", "Amadou Onana", "Josh Onomah", "Paul Onuachu", "Tyler Onyango", "Frank Onyeka", "Lewis Orford", "Divock Origi", "Mislav Orsic", "Stefan Ortega", "Detlef Esapa Osong", "Owen Otasowie", "Dango Ouattara", "Salah-Eddine Oulad M'hand", "Alex Oxlade-Chamberlain", "Maximillian Oyedele", "Daniel Oyegoke", "David Ozoh", "Adrion Pajaziti", "Cole Palmer", "Jonathan Panzo", "Stefan Parkes", "Troy Parrott", "Thomas Partey", "Maksim Paskotsi", "Charlie Patino", "Travis Patterson", "Lewis Payne", "Ben Pearson", "Myles Peart-Harris", "Pedro Neto", "Facundo Pellistri", "Nicolas Pépé", "Percy Tau", "Ayoze Pérez", "Ivan Perisic", "Sonny Perkins", "Romain Perraud", "Máximo Perrone", "Cameron Peupion", "Philippe Coutinho", "Nathaniel Phillips", "Jaden Philogene", "Jordan Pickford", "Ethan Pinnock", "Cameron Plain", "Luke Plange", "Paul Pogba", "Euan Pollock", "Nick Pope", "Pedro Porro", "Freddie Potts", "Ian Poveda-Ocampo", "Dennis Praet", "Aaron Pressley", "Isaac Price", "Christian Pulisic", "Jarell Quansah", "Daniel Quick", "Sebastian Quirk", "Luka Racic", "Arjan Raikhy", "Jesurun Rak-Sakyi", "Calvin Ramsay", "Aaron Ramsdale", "Jacob Ramsey", "Darren Randolph", "Dion Rankine", "Raphinha", "Marcus Rashford", "David Raya", "Jadan Raymond", "Tim Ream", "Nathan Redmond", "Harrison Reed", "Sergio Reguilón", "Renan Lodi", "Dominic Revan", "Ricardo Pereira", "Declan Rice", "Taylor Richards", "Richarlison", "Jairo Riedewald", "Matt Ritchie", "Roberto Firmino", "Haydon Roberts", "Andrew Robertson", "Joel Robles", "Max Robson", "Marc Roca", "Marek Rodák", "Kaden Rodney", "Joe Rodon", "Rodri", "Rodrigo", "Rodrigo Muniz", "James Rodríguez", "Mads Roerslev", "Morgan Rogers", "Cristian Romero", "Oriol Romeu", "Connor Ronan", "Salomón Rondón", "Zeno Rossi", "Joe Rothwell", "Rúben Dias", "Rúben Neves", "Rúben Vinagre", "John Ruddy", "Antonio Rüdiger", "Rúnar Rúnarsson", "Georginio Rutter", "Marcel Sabitzer", "Dominic Sadi", "Charles Sagoe Junior", "Allan Saint-Maximin", "Romain Saïss", "Bukayo Saka", "William Saliba", "Mohammed Salisu", "Brice Samba", "Albert Sambi Lokonga", "Lakyle Samuel", "Ishé Samuels-Smith", "Robert Sánchez", "Jadon Sancho", "Dion Sanderson", "Philippe Sandler", "Morgan Sanson", "Pablo Sarabia", "Matija Sarkic", "Jeremy Sarmiento", "Malang Sarr", "Charlie Savage", "Christian Saydee", "Charlie Sayers", "Gianluca Scamacca", "Oliver Scarles", "Dane Scarlett", "Kevin Schade", "Fabian Schär", "Kjell Scherpen", "Jeffrey Schlupp", "Kasper Schmeichel", "Kristian Sekularac", "Antoine Semenyo", "Marcos Senesi", "Jean Michaël Seri", "Steven Sessegnon", "Jamie Shackleton", "Xherdan Shaqiri", "Teddy Sharman-Lowe", "Luke Shaw", "Jonjo Shelvey", "Joe Sheridan", "Shola Shoretire", "Abdallah Sima", "Dynel Simeu", "Ellis Simms", "Kamarai Simon-Swyer", "Xavier Simons", "Viljami Sinisalo", "Luis Sinisterra", "Moussa Sissoko", "Oliver Skipp", "Cieran Slicker", "Gabriel Slonina", "Thierry Small", "William Smallbone", "Matt Smith", "Emile Smith Rowe", "Alex Smithies", "Joe Snowdon", "Dominic Solanke", "Manor Solomon", "Son Heung-Min", "Andreas Söndergaard", "Jude Soonsup-Bell", "Tomás Soucek", "Boubakary Soumaré", "Lino Sousa", "Harry Souttar", "Kamal Sowah", "Çaglar Söyüncü", "Djed Spence", "Jack Spong", "Jack Stacey", "Junior Stanislas", "Jay Stansfield", "Jason Steele", "Jed Steer", "Zack Steffen", "Jack Stephens", "Raheem Sterling", "Finley Stevens", "Layton Stewart", "Jakub Stolarczyk", "John Stones", "James Storer", "Thomas Strakosha", "Robert Street", "Pascal Struijk", "Thanawat Suengchitthawon", "Kamaldeen Sulemana", "Crysencio Summerville", "Sam Surridge", "Will Swan", "Zak Swanson", "Sil Swinkels", "Japhet Tanganga", "Matt Targett", "James Tarkowski", "Marcus Tavernier", "Slobodan Tedic", "Nathan Tella", "Kenny Tete", "Thiago", "Thiago Silva", "Luke Thomas", "Dominic Thompson", "Youri Tielemans", "Kieran Tierney", "Tobias Figueiredo", "Harry Toffolo", "Takehiro Tomiyasu", "James Tomkins", "Ivan Toney", "Lucas Torreira", "Ferran Torres", "Cenk Tosun", "Toti", "Andros Townsend", "Bertrand Traoré", "Mark Travers", "Ryan Trevitt", "Trézéguet", "Trincão", "Kieran Trippier", "Leandro Trossard", "Nathan Trott", "Auston Trusty", "Konstantinos Tsimikas", "Antef Tsoungui", "Axel Tuanzebe", "Matt Turner", "Ed Turns", "Harry Tyrer", "Destiny Udogie", "Deniz Undav", "Harvey Vale", "Joel Valencia", "Yan Valery", "Donny van de Beek", "Sepp van den Berg", "Dani van den Heuvel", "Virgil van Dijk", "Jan Paul van Hecke", "Mikki van Sas", "Raphaël Varane", "Jamie Vardy", "Joël Veltman", "Jannik Vestergaard", "Matthew Vigor", "Matías Viña", "Radek Vítek", "Nikola Vlasic", "Jake Vokins", "Jack Wadham", "Theo Walcott", "Kyle Walker", "Kyle Walker-Peters", "Reuell Walters", "Christian Walton", "Aaron Wan-Bissaka", "Wanya Marçal-Madivadua", "Joel Ward", "James Ward-Prowse", "Lewis Warrington", "Ollie Watkins", "Noah Watson", "Kelland Watts", "Adam Webster", "Wout Weghorst", "Jensen Weir", "Danny Welbeck", "Reece Welch", "Charlie Wellens", "Jack Wells-Morrison", "Timo Werner", "Wesley", "Charlie Whitaker", "Ben White", "Alfie Whiteman", "Joe Whitworth", "George Wickens", "Dylan Williams", "Willian", "Joe Willock", "Keehan Willows", "Harry Wilson", "Thomas Wilson-Brown", "Josh Wilson-Esbrand", "Harry Winks", "Yoane Wissa", "Maximilian Wöber", "Max Woltman", "Chris Wood", "Ben Woodburn", "Freddie Woodman", "Joe Wormleighton", "Joe Worrall", "James Wright", "Xande Silva", "Granit Xhaka", "Yago Alonso", "Andrii Yarmolenko", "Yegor Yarmolyuk", "Ryan Yates", "Brad Young", "Nathan Young-Coombes", "Illia Zabarnyi", "Wilfried Zaha", "Denis Zakaria", "André-Frank Zambo Anguissa", "Jan Zamburek", "Zanka", "Jordan Zemura", "Andi Zeqiri", "Zidane Iqbal", "Oleksandr Zinchenko", "Hakim Ziyech", "Kurt Zouma", "Oliwier Zych", "Martin Ødegaard", "Leo Østigård"]

df = pd.read_csv("extracted.csv", low_memory=False)

player_name = [name.lower() for name in player_name]

matching_players = df[(df['long_name'].str.lower().isin(player_name)) & (df['international_reputation'] >= 1)]

matching_players = matching_players.drop_duplicates(subset=['long_name'])

matching_players['score'] = 0.2*matching_players['international_reputation'] + 0.3*matching_players['overall'] + 0.3*matching_players['value_eur'] + 0.2*matching_players['potential']

grouped_players = matching_players[matching_players['league_name'] == 'Premier League'].groupby('club_name')

top_players = []

for club_name, players in grouped_players:
    if len(players) > 11:
        top_players.extend(players.nlargest(11, 'score').index)
    else:
        top_players.extend(players.index)

top_players_df = df.loc[top_players]

grouped_top_players = top_players_df.groupby('club_name')

for club_name, players in grouped_top_players:
    if len(players) >= 11:
        print(f"Club: {club_name}")
        print(", ".join(players['long_name']))
        print()



# In[6]:


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('player_attributes.csv')

cols_to_keep = ['club_name', 'overall', 'potential', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
data = data[cols_to_keep]

teams_str = input("Enter team names to predict (separated by comma): ")
teams_list = [team.strip() for team in teams_str.split(",")]

club_data = data.groupby('club_name').mean()

club_data = club_data.loc[teams_list]

club_data = (club_data - club_data.mean()) / club_data.std()

games = pd.DataFrame(columns=['home', 'away'] + list(club_data.columns))
for i, team1 in enumerate(club_data.index):
    for j, team2 in enumerate(club_data.index):
        if i < j and (team1 in teams_list) and (team2 in teams_list):
            home_stats = club_data.loc[team1]
            away_stats = club_data.loc[team2]
            games.loc[len(games)] = [team1, team2] + list(home_stats - away_stats)

label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(games.apply(lambda row: 0 if row['home'] < row['away'] else (1 if row['home'] > row['away'] else 2), axis=1))

X_train = games.drop(['home', 'away'], axis=1)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer()
X_train = imputer.fit_transform(X_train)

model = LogisticRegression(max_iter=1000)

try:
    model.fit(X_train, y_train)
except ValueError:
    for i, team1 in enumerate(teams_list):
        for j, team2 in enumerate(teams_list):
            if i < j:
                home_stats = club_data.loc[team1]
                away_stats = club_data.loc[team2]
                home_overall = home_stats['overall'] + home_stats['shooting'] + home_stats['passing'] + home_stats['dribbling'] + home_stats['defending']
                away_overall = away_stats['overall'] + away_stats['shooting'] + away_stats['passing'] + away_stats['dribbling'] + away_stats['defending']
                if home_overall > away_overall:
                    print(f'{team1} vs {team2}: {team1} wins')
                    home_score = int((home_overall - away_overall)/10) + 1
                    away_score = int(0.5*home_score)
                    print(f'Score prediction: {team1} {home_score} - {away_score} {team2}')
                else:
                    print(f'{team1} vs {team2}: {team2} wins')
                    away_score = int((away_overall - home_overall)/10) + 1
                    home_score = int(0.5*away_score)
                    print(f'Score prediction: {team2} {away_score} - {home_score} {team1}')
else:
    for i, team1 in enumerate(teams_list):
        for j, team2 in enumerate(teams_list):
            if i < j:
                home_stats = club_data.loc[team1]
                away_stats = club_data.loc[team2]
                home_overall = home_stats['overall'] + home_stats['shooting'] + home_stats['passing'] + home_stats['dribbling'] + home_stats['defending']
                away_overall = away_stats['overall'] + away_stats['shooting'] + away_stats['passing'] + away_stats['dribbling'] + away_stats['defending']
                X_test = (home_stats - away_stats)
                if home_overall > away_overall:
                    winner = team1
                    home_score = int((home_overall - away_overall)/10) + 2
                    away_score = int(0.5*home_score)
                elif away_overall > home_overall:
                    winner = team2
                    away_score = int((away_overall - home_overall)/10) + 2
                    home_score = int(0.5*away_score)
                else:
                    winner = 'Draw'
                    home_score = random.randint(0, 3)
                    away_score = random.randint(0, 3)
                print(f'{team1} vs {team2}: {winner} wins')
                print(f'Score prediction: {winner} {home_score} - {away_score} {team2 if winner == team1 else team1}') 


# In[ ]:




