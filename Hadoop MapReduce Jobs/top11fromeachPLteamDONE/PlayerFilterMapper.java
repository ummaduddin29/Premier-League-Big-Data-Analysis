package project;

import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class PlayerFilterMapper extends Mapper<LongWritable, Text, Text, Text> {

	private final String[] names = { "Philip Billing", "Dominic Solanke",
			"Lewis Cook", "Lloyd Kelly", "Jaidon Anthony", "Ryan Christie",
			"Marcus Tavernier", "Ryan Fredericks", "Jack Stephens",
			"Mark Travers", "Jack Stacey", "Bukayo Saka", "Martin Ødegaard",
			"Emile Smith Rowe", "Thomas Partey", "Aaron Ramsdale",
			"Kieran Tierney", "Alexandre Lacazette", "Granit Xhaka",
			"Oleksandr Zinchenko", "Nicolas Pépé", "Rob Holding",
			"Lucas Digne", "Emiliano Buendía", "Matty Cash", "John McGinn",
			"Jacob Ramsey", "Ollie Watkins", "Tyrone Mings", "Morgan Sanson",
			"Frédéric Guilbert", "Leander Dendoncker", "Kortney Hause",
			"Ivan Toney", "Thomas Strakosha", "Bryan Mbeumo", "Ben Mee",
			"Rico Henry", "Vitaly Janelt", "Mathias Jensen", "Yoane Wissa",
			"Keane Lewis-Potter", "Kevin Schade", "Pontus Jansson",
			"Leandro Trossard", "Alexis Mac Allister", "Lewis Dunk",
			"Enock Mwepu", "Tariq Lamptey", "Pascal Groß", "Deniz Undav",
			"Jürgen Locadia", "Adam Webster", "Billy Gilmour", "Steven Alzate",
			"Antonio Rüdiger", "N'Golo Kanté", "Raheem Sterling",
			"Reece James", "Édouard Mendy", "Mason Mount", "Timo Werner",
			"Christian Pulisic", "Kalidou Koulibaly", "Ben Chilwell",
			"Hakim Ziyech", "Wilfried Zaha", "Michael Olise",
			"Joachim Andersen", "Eberechi Eze", "Tyrick Mitchell",
			"Odsonne Édouard", "Jean-Philippe Mateta", "Jeffrey Schlupp",
			"Will Hughes", "Sam Johnstone", "Gary Cahill", "Jordan Pickford",
			"Dominic Calvert-Lewin", "Ben Godfrey", "James Tarkowski",
			"Conor Coady", "Demarai Gray", "Michael Keane", "Dwight McNeil",
			"Neal Maupay", "Alex Iwobi", "Tom Davies", "Jean Michaël Seri",
			"Manor Solomon", "Bernd Leno", "Issa Diop", "Harry Wilson",
			"Alfie Mawson", "Marek Rodák", "Antonee Robinson", "Harrison Reed",
			"Bobby De Cordova-Reid", "Layvin Kurzawa", "Illan Meslier",
			"Patrick Bamford", "Jack Harrison", "Pascal Struijk", "Robin Koch",
			"Maximilian Wöber", "Joe Gelhardt", "Luke Ayling", "Liam Cooper",
			"Stuart Dallas", "Crysencio Summerville", "Youri Tielemans",
			"James Maddison", "Jamie Vardy", "Patson Daka", "Ademola Lookman",
			"Timothy Castagne", "Dennis Praet", "Kiernan Dewsbury-Hall",
			"James Justin", "Boubakary Soumaré", "Daniel Amartey",
			"Sadio Mané", "Trent Alexander-Arnold", "Virgil van Dijk",
			"Andrew Robertson", "Ibrahima Konaté", "Joe Gomez",
			"Jordan Henderson", "Naby Keïta", "Xherdan Shaqiri",
			"Curtis Jones", "Konstantinos Tsimikas", "Kevin De Bruyne",
			"Aymeric Laporte", "Jack Grealish", "Riyad Mahrez", "Kyle Walker",
			"Julián Álvarez", "John Stones", "Nathan Aké", "Zack Steffen",
			"Issa Kaboré", "Philippe Sandler", "Paul Pogba", "Jadon Sancho",
			"Marcus Rashford", "Raphaël Varane", "Luke Shaw",
			"Scott McTominay", "Anthony Martial", "Tyrell Malacia",
			"Aaron Wan-Bissaka", "Donny van de Beek", "Harry Maguire",
			"Sven Botman", "Alexander Isak", "Allan Saint-Maximin",
			"Kieran Trippier", "Nick Pope", "Dan Burn", "Matt Targett",
			"Sean Longstaff", "Jonjo Shelvey", "Martin Dúbravka",
			"Ryan Fraser", "Moussa Niakhaté", "Jesse Lingard", "Orel Mangala",
			"Cheikhou Kouyaté", "Loïc Badé", "Joe Worrall", "Ryan Yates",
			"Scott McKenna", "Giulian Biancone", "Sam Surridge",
			"Harry Toffolo", "James Ward-Prowse", "Kyle Walker-Peters",
			"Romain Perraud", "Stuart Armstrong", "Moussa Djenepo",
			"Nathan Redmond", "Adam Armstrong", "Yan Valery",
			"Ainsley Maitland-Niles", "Sékou Mara", "Mateusz Lis",
			"Harry Kane", "Dejan Kulusevski", "Giovani Lo Celso",
			"Yves Bissouma", "Eric Dier", "Oliver Skipp", "Pierluigi Gollini",
			"Djed Spence", "Harry Winks", "Hugo Lloris", "Japhet Tanganga",
			"Declan Rice", "Gianluca Scamacca", "Jarrod Bowen", "Nayef Aguerd",
			"Vladimír Coufal", "Michail Antonio", "Manuel Lanzini",
			"Craig Dawson", "Alex Král", "Arthur Masuaku", "Flynn Downes" }; // Replace
																				// with
																				// actual
																				// names

	@Override
	protected void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {
		String line = value.toString();
		String[] fields = line.split(",");
		String longName = fields[6];

		if (containsName(longName)) {
			context.write(new Text(longName), value);
		}
	}

	private boolean containsName(String longName) {
		for (String name : names) {
			if (longName.contains(name)) {
				return true;
			}
		}
		return false;
	}
}
