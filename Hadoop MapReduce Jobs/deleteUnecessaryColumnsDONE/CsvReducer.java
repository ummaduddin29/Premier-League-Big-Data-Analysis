package deleteColumns;
import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class CsvReducer extends Reducer<Text, Text, Text, Text> {

  public void reduce(Text key, Iterable<Text> values, Context context)
      throws IOException, InterruptedException {

    StringBuilder outputCsv = new StringBuilder();

    for (Text value : values) {
      outputCsv.append(value.toString()).append("\n");
    }

    context.write(key, new Text(outputCsv.toString()));
  }
}
