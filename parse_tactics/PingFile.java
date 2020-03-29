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

public class PingFile {
    //use this for date conversions
    public static DateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd HH:mm:ss.SSSSSS");
    
    int length; //is the number of lines in the file

    public Date[] timestamps;
    public int[] servers;
    public int[] pingSuccess;
    public double[] pingTime;

    /**
     * Creates a new PingFile object from a file
     *
     * @param filename is the Ping file to parse out into separate files for EXAMM
     *
     */
    public PingFile(String filename) {
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
            pingSuccess = new int[length];
            pingTime = new double[length];

            //skip the first line as it's the column headers
            for (int i = 1; i < length; i++) {
                System.out.println(lines.get(i + 1));

                String[] parts = lines.get(i).split(",", -1);

                try {
                    timestamps[i] = dateFormat.parse(parts[0]);
                } catch (ParseException e) {
                    System.err.println("Error parsing timestamp: " + e);
                    e.printStackTrace();
                    System.exit(1);
                }
                servers[i] = Integer.parseInt(parts[1]);
                pingSuccess[i] = Integer.parseInt(parts[2]);
                pingTime[i] = Double.parseDouble(parts[3]);

                System.out.println("line " + i + " timestamp: '" + timestamps[i] + "', server: " + servers[i] + ", pingSuccess: " + pingSuccess[i] + ", pingTime: " + pingTime[i]);
            }

        } catch (IOException e) {
            System.err.println("ERROR opening PingFile: '" + filename + "'");
            e.printStackTrace();
            System.exit(1);
        }
    }

}
