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

public class TVAFile {
    //use this for date conversions
    public static DateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd HH:mm:ss.SSSSSS");

    int length; //is the number of lines in the file

    public ArrayList<TVARow> rows = new ArrayList<TVARow>();

    public Date getTimestamp(int i) {
        return rows.get(i).timestamp;
    }

    public int getServer(int i) {
        return rows.get(i).server;
    }

    public int getTactic(int i) {
        return rows.get(i).tactic;
    }

    public double getLatency(int i) {
        return rows.get(i).latency;
    }

    public double getCost(int i) {
        return rows.get(i).cost;
    }

    public int getReliability(int i) {
        return rows.get(i).reliability;
    }

    public static class TVARow implements Comparable<TVARow> {
        public Date timestamp;
        public int server;
        public int tactic;
        public double latency;
        public double cost;
        public int reliability;

        public TVARow(Date timestamp, int server, int tactic, double latency, double cost, int reliability) {
            this.timestamp = timestamp;
            this.server = server;
            this.tactic =  tactic;
            this.latency = latency;
            this.cost = cost;
            this.reliability = reliability;
        }

        @Override
        public int compareTo(TVARow other) {
            return this.timestamp.compareTo(other.timestamp);
        }

        @Override
        public String toString() {
            return "[timestamp: '" + timestamp + "', server: " + server + ", tactic: " + tactic + ", latency: " + latency + ", cost: " + cost + ", reliability: " + reliability + "]";
        }
    }


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

            String line = bufferedReader.readLine(); //skip the first line

            int i = 1;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println("read: '" + line + "'");
                lines.add(line);
                String[] parts = line.split(",", -1);

                //ignore the first and last entries because of the empty CSV values
                Date timestamp = null;
                try {
                    timestamp = dateFormat.parse(parts[1]);
                } catch (ParseException e) {
                    System.err.println("Error parsing timestamp: " + e);
                    e.printStackTrace();
                    System.exit(1);
                }
                int server = Integer.parseInt(parts[2]);
                int tactic = Integer.parseInt(parts[3]);
                double latency = Double.parseDouble(parts[4]);
                double cost = Double.parseDouble(parts[5]);
                int reliability = Integer.parseInt(parts[6]);

                TVARow row = new TVARow(timestamp, server, tactic, latency, cost, reliability);
                System.out.println("line " + i + " " + row.toString());
                rows.add(row);
                i++;
            }

            length = rows.size();
            Collections.sort(rows);

        } catch (IOException e) {
            System.err.println("ERROR opening TVAFile: '" + filename + "'");
            e.printStackTrace();
            System.exit(1);
        }
    }

}
