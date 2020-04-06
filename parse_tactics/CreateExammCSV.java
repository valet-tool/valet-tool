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
import java.util.List;
import java.util.HashSet;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.text.ParseException;

public class CreateExammCSV {
    //use this for date conversions
    public static DateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd HH:mm:ss.SSSSSS");

    public static BufferedWriter[][] getOutfiles(String outfileType) throws IOException {
        BufferedWriter[][] outfiles = new BufferedWriter[8][5];
        for (int server = 1; server <= 8; server++) {
            for (int tactic = 1; tactic <= 5; tactic++) {
                BufferedWriter writer = outfiles[server-1][tactic-1];
                if (writer == null) {
                    String filename = "tva_server_" + server + "_tactic_" + tactic + "_" + outfileType + ".csv";
                    System.out.println("Making new outfile: '" + filename + "'");

                    writer = new BufferedWriter(new FileWriter(filename));
                    outfiles[server-1][tactic-1] = writer;

                    writer.write("time_since_last_recording,latency,cost,reliability");

                    if (tactic == 1) writer.write(",time_since_last_ping,last_ping");
                    writer.write("\n");
                    writer.flush();
                } else {
                    String filename = "tva_server_" + server + "_tactic_" + tactic + "_" + outfileType + ".csv";
                    System.out.println("Making new outfile: '" + filename + "'");

                    writer.flush();
                    writer.close();
                    writer = new BufferedWriter(new FileWriter(filename));
                }
            }
        }

        return outfiles;
    }


    public static void main(String[] arguments) {
        if (arguments.length != 4) {
            System.err.println("Incorrect arguments, usage:");
            System.err.println("java CreateExammCSV <ping filename> <tva output filename> <training file rows> <testing file rows>");
            System.exit(1);
        }

        PingFile ping = new PingFile(arguments[0]);
        TVAFile tva = new TVAFile(arguments[1]);
        int trainingRows = Integer.parseInt(arguments[2]);
        int validationRows = Integer.parseInt(arguments[3]);

        //make an output file for each server and tactic

        try {
            BufferedWriter[][] outfiles = getOutfiles("train");
            //there are 8 different servers and 5 different tactics

            Date[][] lastRecordingTime = new Date[8][5];

            //only use pings for tactic 1
            int[] lastPingIndex = new int[8];
            for (int i = 0; i < 8; i++) lastPingIndex[i] = 0;

            for (int i = 0; i < tva.length; i++) {
                if (i == (40 * trainingRows)) {
                    System.out.println("setting outfiles at i: " + i);
                    outfiles = getOutfiles("test");
                } else if (i == ((40 * trainingRows) + (40 * validationRows))) {
                    System.out.println("setting outfiles at i: " + i);
                    outfiles = getOutfiles("validate");
                }

                Date timestamp = tva.timestamps[i];
                int server = tva.servers[i];
                int tactic = tva.tactics[i];
                double latency = tva.latencies[i];
                double cost = tva.costs[i];
                int reliability = tva.reliabilities[i];

                //System.out.println("getting writer for server: " + server + ", tactic: " + tactic);

                BufferedWriter writer = outfiles[server-1][tactic-1];

                if (lastRecordingTime[server-1][tactic-1] == null) {
                    //there is no time since last recording for the first entry
                    writer.write("0");
                } else {
                    double seconds = (timestamp.getTime() - lastRecordingTime[server-1][tactic-1].getTime())/1000;

                    //System.out.println("last time: " + dateFormat.format(lastRecordingTime[server-1][tactic-1]) + ", current time: " + dateFormat.format(timestamp) + ", difference: " + seconds);

                    writer.write(Double.toString(seconds));
                }

                lastRecordingTime[server-1][tactic-1] = timestamp;

                writer.write("," + latency + "," + cost + "," + reliability);

                if (tactic == 1) {
                    Date lastPingTime = null;

                    for (int j = lastPingIndex[server-1]; j < ping.length; j++) {
                        if (ping.servers[j] != server) continue;

                        if (ping.timestamps[j].after(timestamp)) {
                            break;
                        } else {
                            lastPingIndex[server-1] = j;
                            lastPingTime = ping.timestamps[j];
                        }
                    }

                    double seconds;
                    if (lastPingTime == null) {
                        System.out.println("lastPingTime == null for server: " + server + ", tactic: " + tactic + " and line: " + i);
                        //if there was no last ping time (for the first downloads) the time since last ping == 0
                        seconds = 0;
                    } else {
                        seconds = (lastRecordingTime[server-1][tactic-1].getTime() - lastPingTime.getTime()) /1000;
                    }

                    writer.write("," + seconds + "," + ping.pingTime[lastPingIndex[server-1]]);
                }

                writer.write("\n");
                writer.flush();
            }

            for (int server = 1; server <= 8; server++) {
                for (int tactic = 1; tactic <= 5; tactic++) {
                    BufferedWriter writer = outfiles[server-1][tactic-1];
                    writer.close();
                }
            }

        } catch (IOException e) {
            System.err.println("Error writing out files: " + e);
            e.printStackTrace();
        }
    }

}