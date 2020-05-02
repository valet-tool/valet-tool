import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.text.ParseException;

public class TVAOutput {
    //use this for date conversions
    public static DateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd HH:mm:ss.SSSSSS");

    int server;
    int tactic;

    public ArrayList<TVARow> tvaRows = new ArrayList<TVARow>();
    public ArrayList<PingRow> pingRows = new ArrayList<PingRow>();

    public class TVARow implements Comparable<TVARow> {
        public Date timestamp;
        public double latency;
        public double cost;
        public int reliability;
        public double timeSinceLastRecording = 0;
        public Date pingTimestamp;
        public double timeSinceLastPing = 0;
        public int pingSuccess = 0;
        public double pingTime = 0;

        public TVARow(Date timestamp, double latency, double cost, int reliability) {
            this.timestamp = timestamp;
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

    public class PingRow implements Comparable<PingRow> {
        public Date timestamp;
        public int pingSuccess;
        public double pingTime;

        public PingRow(Date timestamp, int pingSuccess, double pingTime) {
            this.timestamp = timestamp;
            this.pingSuccess = pingSuccess;
            this.pingTime = pingTime;
        }

        @Override
        public int compareTo(PingRow other) {
            return this.timestamp.compareTo(other.timestamp);
        }

        @Override
        public String toString() {
            return "[timestamp: '" + timestamp + "', server: " + server + ", tactic: " + tactic + ", pingSuccess: " + pingSuccess + ", pingTime: " + pingTime + "]";
        }
    }

    public void addTVARow(Date timestamp, int server, int tactic, double latency, double cost, int reliability) {
        if (server != this.server || tactic != this.tactic) {
            System.err.println("Mismatched server and/or tactic for tva:");
            System.err.println("row server: " + server + ", tactic: " + tactic);
            System.err.println("tva server: " + this.server + ", tactic: " + this.tactic);
            System.exit(1);
        }

        tvaRows.add(new TVARow(timestamp, latency, cost, reliability));
        //System.out.println("tva[" + server + "][" + tactic + "]: number ping rows: " + tvaRows.size());

    }

    public void addPingRow(Date timestamp, int server, int tactic, int pingSuccess, double pingTime) {
        if (server != this.server || tactic != this.tactic) {
            System.err.println("Mismatched server and/or tactic for tva:");
            System.err.println("row server: " + server + ", tactic: " + tactic);
            System.err.println("tva server: " + this.server + ", tactic: " + this.tactic);
            System.exit(1);
        }

        pingRows.add(new PingRow(timestamp, pingSuccess, pingTime));
        //System.out.println("tva[" + server + "][" + tactic + "]: number ping rows: " + pingRows.size());
    }

    public void sort() {
        Collections.sort(tvaRows);
        Collections.sort(pingRows);
    }

    public void setTimeSinceLastRecording() {
        sort();
        for (int i = 0; i < tvaRows.size(); i++) {
            if (i == 0) {
                tvaRows.get(i).timeSinceLastRecording = 0;
            } else {
                double seconds = (tvaRows.get(i).timestamp.getTime() - tvaRows.get(i-1).timestamp.getTime())/1000;

                //System.out.println("last time: " + dateFormat.format(tvaRows.get(i-1).timestamp) + ", current time: " + dateFormat.format(tvaRows.get(i).timestamp) + ", difference: " + seconds);
                tvaRows.get(i).timeSinceLastRecording = seconds;
            }
        }
    }

    public void mergePingTimes() {
        if (tactic != 1) return;
        sort();

        int tvaRowIndex = 0;
        int pingRowIndex = 0;

        //System.out.println("tva[" + server + "][" + tactic + "] tvaRows: " + tvaRows.size() + ", pingRows: " + pingRows.size());

        TVARow tvaRow = tvaRows.get(tvaRowIndex);
        PingRow currentPingRow = null;
        PingRow nextPingRow = pingRows.get(pingRowIndex + 1);

        while (tvaRowIndex < tvaRows.size()) {
            //System.out.println("pingRowIndex: " + pingRowIndex + ", tvaRowIndex: " + tvaRowIndex + ", next ping time <= tva time : " + nextPingRow.timestamp.compareTo(tvaRow.timestamp));

            while (nextPingRow.timestamp.compareTo(tvaRow.timestamp) <= 0) {
                pingRowIndex++;

                currentPingRow = nextPingRow;

                if (pingRowIndex + 1 >= pingRows.size()) break; //we're done

                nextPingRow = pingRows.get(pingRowIndex + 1);

                //System.out.println("\tpingRowIndex: " + pingRowIndex + ", tvaRowIndex: " + tvaRowIndex + ", next ping time <= tva time : " + nextPingRow.timestamp.compareTo(tvaRow.timestamp));
                //System.out.println("\tmoving pings forward - current ping time: " + dateFormat.format(currentPingRow.timestamp) + ", tva row time: " + dateFormat.format(tvaRow.timestamp) + ", next ping time: " + dateFormat.format(nextPingRow.timestamp));
            }

            if (currentPingRow != null) {
                //System.out.println("current ping time: " + dateFormat.format(currentPingRow.timestamp) + ", tva row time: " + dateFormat.format(tvaRow.timestamp) + ", next ping time: " + dateFormat.format(nextPingRow.timestamp));
            } else {
                //System.out.println("current ping time: null, tva row time: " + dateFormat.format(tvaRow.timestamp) + ", next ping time: " + dateFormat.format(nextPingRow.timestamp));
            }

            if (currentPingRow != null) {
                double seconds = (tvaRow.timestamp.getTime() - currentPingRow.timestamp.getTime()) /1000;
                tvaRow.pingTimestamp = currentPingRow.timestamp;
                tvaRow.timeSinceLastPing = seconds;
                tvaRow.pingSuccess = currentPingRow.pingSuccess;
                tvaRow.pingTime = currentPingRow.pingTime;
            }

            //System.out.println("SETTING TVA ROW: timeSinceLastPing: " + tvaRow.timeSinceLastPing + ", pingSucces: " + tvaRow.pingSuccess + ", pingTime: " + tvaRow.pingTime);

            tvaRowIndex++;
            if (tvaRowIndex >= tvaRows.size()) return; //we're done

            tvaRow = tvaRows.get(tvaRowIndex);
            //System.out.println();
        }
    }

    public TVARow getLastTVARow() {
        return tvaRows.get(tvaRows.size() - 1);
    }

    public PingRow getLastPingRow() {
        return pingRows.get(pingRows.size() - 1);
    }

    public TVAOutput(int server, int tactic) {
        this.server = server;
        this.tactic = tactic;
    }


    public void updateMinMax(double[] mins, double[] maxs) {
        for (int i = 0; i < tvaRows.size(); i++) {
            TVARow row = tvaRows.get(i);

            double latency = row.latency;
            double cost = row.cost;
            int reliability = row.reliability;
            double timeSinceLastRecording = row.timeSinceLastRecording;
            double timeSinceLastPing = row.timeSinceLastPing;
            int pingSuccess = row.pingSuccess;
            double pingTime = row.pingTime;

           if (latency < mins[0]) mins[0] = latency;
           if (latency > maxs[0]) maxs[0] = latency;

           if (cost < mins[1]) mins[1] = cost;
           if (cost > maxs[1]) maxs[1] = cost;

           if (reliability < mins[2]) mins[2] = reliability;
           if (reliability > maxs[2]) maxs[2] = reliability;

           if (timeSinceLastRecording < mins[3]) mins[3] = timeSinceLastRecording;
           if (timeSinceLastRecording > maxs[3]) maxs[3] = timeSinceLastRecording;

           if (timeSinceLastPing < mins[4]) mins[4] = timeSinceLastPing;
           if (timeSinceLastPing > maxs[4]) maxs[4] = timeSinceLastPing;

           if (pingSuccess < mins[5]) mins[5] = pingSuccess;
           if (pingSuccess > maxs[5]) maxs[5] = pingSuccess;

           if (pingTime < mins[6]) mins[6] = pingTime;
           if (pingTime > maxs[6]) maxs[6] = pingTime;
        }
    }

    public void normalize(double[] mins, double[] maxs) {
        for (int i = 0; i < tvaRows.size(); i++) {
            TVARow row = tvaRows.get(i);

            row.latency = (row.latency - mins[0])/(maxs[0]-mins[0]);
            row.cost = (row.cost - mins[1])/(maxs[1]-mins[1]);
            row.reliability = (int)((row.reliability - mins[2])/(maxs[2]-mins[2]));
            row.timeSinceLastRecording = (row.timeSinceLastRecording - mins[3])/(maxs[3]-mins[3]);
            row.timeSinceLastPing = (row.timeSinceLastPing - mins[4])/(maxs[4]-mins[4]);
            row.pingSuccess = (int)((row.pingSuccess - mins[5])/(maxs[5]-mins[5]));
            row.pingTime = (row.pingTime - mins[6])/(maxs[6]-mins[6]);
        }
    }

    public BufferedWriter getWriter(String outfileType) throws IOException {
        String filename = null;

        if (CreateExammCSV.normalize) {
            filename = "normalized_tva_server_" + server + "_tactic_" + tactic + "_" + outfileType + ".csv";
        } else {
            filename = "tva_server_" + server + "_tactic_" + tactic + "_" + outfileType + ".csv";
        }
        System.out.println("Making new outfile: '" + filename + "'");

        BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
        writer.write("time_since_last_recording,latency,cost,reliability");

        if (tactic == 1) writer.write(",time_since_last_ping,last_ping");
        writer.write("\n");

        return writer;
    }

    public void writeToFile(double trainingPercent, double validationPercent) throws IOException {
        int trainingRows = (int)(tvaRows.size() * trainingPercent);
        int validationRows = (int)(tvaRows.size() * validationPercent);

        BufferedWriter writer = getWriter("train");

        for (int i = 0; i < tvaRows.size(); i++) {
            if (i == trainingRows) {
                writer.close();
                System.out.println("setting outfiles at i: " + i);
                writer = getWriter("test");
            } else if (i == (trainingRows * validationRows)) {
                writer.close();
                System.out.println("setting outfiles at i: " + i);
                writer = getWriter("validation");
            }

            TVARow row = tvaRows.get(i);

            Date timestamp = row.timestamp;
            double latency = row.latency;
            double cost = row.cost;
            int reliability = row.reliability;
            double timeSinceLastRecording = row.timeSinceLastRecording;
            Date pingTimestamp = row.pingTimestamp;
            double timeSinceLastPing = row.timeSinceLastPing;
            int pingSuccess = row.pingSuccess;
            double pingTime = row.pingTime;


            writer.write(dateFormat.format(timestamp) +"," + latency + "," + cost + "," + reliability + "," + timeSinceLastRecording);

            if (tactic == 1) {
                if (pingTimestamp != null) {
                    writer.write("," + dateFormat.format(pingTimestamp) + "," + timeSinceLastPing + "," + pingSuccess + "," + pingTime);
                } else {
                    writer.write(",," + timeSinceLastPing + "," + pingSuccess + "," + pingTime);
                }
            }
            writer.write("\n");
            writer.flush();
        }

        writer.close();
    }
}
