package deleteColumns;

import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class NullMapper extends Mapper<LongWritable, Text, LongWritable, Text> {

    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] parts = line.split(",");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < parts.length; i++) {
            if (parts[i].isEmpty()) {
                sb.append("null");
            } else {
                sb.append(parts[i]);
            }
            if (i != parts.length - 1) {
                sb.append(",");
            }
        }
        context.write(key, new Text(sb.toString()));
    }
}
