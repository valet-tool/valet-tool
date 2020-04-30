import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.text.ParseException;

public class PingFile {
    //use this for date conversions
    public static DateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd HH:mm:ss.SSSSSS");
    
    int length; //is the number of lines in the file
    public ArrayList<PingRow> rows = new ArrayList<PingRow>();

    public Date getTimestamp(int i) {
        return rows.get(i).timestamp;
    }

    public int getServer(int i) {
        return rows.get(i).server;
    }

    public int getPingSuccess(int i) {
        return rows.get(i).pingSuccess;
    }

    public double getPingTime(int i) {
        return rows.get(i).pingTime;
    }

    public static class PingRow implements Comparable<PingRow> {
        public Date timestamp;
        public int server;
        public int pingSuccess;
        public double pingTime;

        public PingRow(Date timestamp, int server, int pingSuccess, double pingTime) {
            this.timestamp = timestamp;
            this.server = server;
            this.pingSuccess = pingSuccess;
            this.pingTime = pingTime;
        }

        @Override
        public int compareTo(PingRow other) {
            return this.timestamp.compareTo(other.timestamp);
        }

        @Override
        public String toString() {
            return "[timestamp: '" + timestamp + "', server: " + server + ", pingSuccess: " + pingSuccess + ", pingTime: " + pingTime + "]";
        }
    }

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

            String line = bufferedReader.readLine(); //ignore the first line

            int i = 1;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println("read: '" + line + "'");

                String[] parts = line.split(",");

                Date timestamp = null;
                try {
                    timestamp = dateFormat.parse(parts[0]);
                } catch (ParseException e) {
                    System.err.println("Error parsing timestamp: " + e);
                    e.printStackTrace();
                    System.exit(1);
                }

                int server = Integer.parseInt(parts[1]);
                int tactic = Integer.parseInt(parts[2]);
                int pingSuccess = Integer.parseInt(parts[3]);

                double pingTime = 0.0;
                if (parts.length >= 5) {
                    pingTime = Double.parseDouble(parts[4]);
                }

                PingRow row = new PingRow(timestamp, server, pingSuccess, pingTime);
                rows.add(row);
                System.out.println("line " + i + " " + row.toString());
                i++;
            }

            length = rows.size();
            Collections.sort(rows);

        } catch (IOException e) {
            System.err.println("ERROR opening PingFile: '" + filename + "'");
            e.printStackTrace();
            System.exit(1);
        }
    }

}
