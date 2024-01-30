package deleteColumns;
import java.io.IOException;
import java.util.Arrays;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CsvMapper extends Mapper<LongWritable, Text, Text, Text> {

  private Text outputKey = new Text();
  private Text outputValue = new Text();

  public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {

    String fileName = ((org.apache.hadoop.mapreduce.lib.input.FileSplit) context.getInputSplit())
        .getPath().getName();

    if (fileName.endsWith(".csv")) {
      String[] columns = value.toString().split(",");

      String[] columnsToDrop = {"player_url", "fifa_version", "fifa_update", "fifa_update_date",
          "dob", "club_loaned_from", "club_joined_date", "club_contract_valid_until_year",
          "real_face", "release_clause_eur", "player_face_url"};

      StringBuilder outputRow = new StringBuilder();
      for (int i = 0; i < columns.length; i++) {
        if (!Arrays.asList(columnsToDrop).contains("column" + i)) {
          outputRow.append(columns[i]).append(";");
        }
      }

      outputKey.set(fileName);
      outputValue.set(outputRow.toString());
      context.write(outputKey, outputValue);
    }
  }
}
