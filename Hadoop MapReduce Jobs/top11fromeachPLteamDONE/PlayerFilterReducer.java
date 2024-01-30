package project;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class PlayerFilterReducer extends Reducer<Text, Text, Text, Text> {

    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        Set<String> longNames = new HashSet<>();

        for (Text value : values) {
            String[] fields = value.toString().split(",");
            String longName = fields[6];

            if (!longNames.contains(longName)) {
                context.write(null, value);
                longNames.add(longName);
            }
        }
    }
}
