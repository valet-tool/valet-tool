import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.Date;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.text.ParseException;

public class TVAFile {
    //use this for date conversions
    public static DateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd HH:mm:ss.SSSSSS");

    int length; //is the number of lines in the file

    public Date[] timestamps;
    public int[] servers;
    public int[] tactics;
    public double[] latencies;
    public double[] costs;
    public int[] reliabilities;

    /**
     * Creates a new TimeSeries object from a file
     *
     * @param filename is the TVA file to parse out into separate files for EXAMM
     *
     */
    public TVAFile(String filename) {
        try {
            //create a buffered reader given the filename (which requires creating a File and FileReader object beforehand)
            BufferedReader bufferedReader = new BufferedReader(new FileReader(new File(filename)));
            ArrayList<String> lines = new ArrayList<String>();

            String line;

            while ((line = bufferedReader.readLine()) != null) {
                System.out.println("read: '" + line + "'");
                lines.add(line);

            }

            length = lines.size() - 1;

            timestamps = new Date[length];
            servers = new int[length];
            tactics = new int[length];
            latencies = new double[length];
            costs = new double[length];
            reliabilities = new int[length];

            //skip the first line as it's the column headers
            for (int i = 0; i < length; i++) {
                String[] parts = lines.get(i + 1).split(",", -1);

                //ignore the first and last entries because of the empty CSV values
                try {
                    timestamps[i] = dateFormat.parse(parts[1]);
                } catch (ParseException e) {
                    System.err.println("Error parsing timestamp: " + e);
                    e.printStackTrace();
                    System.exit(1);
                }
                servers[i] = Integer.parseInt(parts[2]);
                tactics[i] = Integer.parseInt(parts[3]);
                latencies[i] = Double.parseDouble(parts[4]);
                costs[i] = Double.parseDouble(parts[5]);
                reliabilities[i] = Integer.parseInt(parts[6]);

                System.out.println("line " + i + " timestamp: '" + timestamps[i] + "', server: " + servers[i] + ", tactic: " + tactics[i] + ", latency: " + latencies[i] + ", cost: " + costs[i] + ", reliability: " + reliabilities[i]);
            }

        } catch (IOException e) {
            System.err.println("ERROR opening TVAFile: '" + filename + "'");
            e.printStackTrace();
            System.exit(1);
        }
    }

}
