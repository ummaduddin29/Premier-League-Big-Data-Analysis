package deleteColumns;

import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CsvFilterMapper extends Mapper<LongWritable, Text, Text, Text> {

    private final Text outKey = new Text();
    private final Text outValue = new Text();

    @Override
    protected void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        String[] tokens = value.toString().split(",");
        String playerName = tokens[6];
        String leagueName = tokens[17];
        if (leagueName.equals("Premier League")) {
            outKey.set(playerName + ":" + leagueName);
            outValue.set(value);
            context.write(outKey, outValue);
        }
    }
}
