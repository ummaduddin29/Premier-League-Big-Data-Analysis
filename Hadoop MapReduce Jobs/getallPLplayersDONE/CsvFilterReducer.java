package deleteColumns;

import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class CsvFilterReducer extends Reducer<Text, Text, Text, Text> {

    private final Text outValue = new Text();

    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {
        String playerName = key.toString().split(":")[0];
        for (Text value : values) {
            String[] tokens = value.toString().split(",");
            String currentLeagueName = tokens[17];
            if (currentLeagueName.equals("Premier League")) {
                outValue.set(value);
                context.write(null, outValue);
            }
        }
    }
}
