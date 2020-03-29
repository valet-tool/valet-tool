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

    public static void main(String[] arguments) {
        if (arguments.length != 2) {
            System.err.println("Incorrect arguments, usage:");
            System.err.println("java CreateExammCSV <ping filename> <tva output filename>");
            System.exit(1);
        }

        PingFile ping = new PingFile(arguments[0]);
        TVAFile tva = new TVAFile(arguments[1]);

        //make an output file for each server and tactic
        BufferedWriter[][] outfiles = new BufferedWriter[8][5];

        try {
            //there are 8 different servers and 5 different tactics
            for (int server = 1; server <= 8; server++) {
                for (int tactic = 1; tactic <= 5; tactic++) {
                    if (outfiles[server-1][tactic-1] == null) {
                        BufferedWriter writer = new BufferedWriter(new FileWriter("tva_server_" + server + "_tactic_" + tactic + ".csv"));
                        outfiles[server-1][tactic-1] = writer;

                        writer.write("time_since_last_recording,latency,cost,reliability");
                        
                        if (tactic == 1) writer.write(",time_since_last_ping,last_ping");
                        writer.write("\n");
                    }

                    BufferedWriter writer = outfiles[server-1][tactic-1];
                }
            }

            Date[][] lastRecordingTime = new Date[8][5];

            //only use pings for tactic 1
            int[] lastPingIndex = new int[8];
            for (int i = 0; i < 8; i++) lastPingIndex[i] = 0;

            for (int i = 0; i < tva.length; i++) {
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

                    writer.write(seconds + "," + ping.pingTime[lastPingIndex[server-1]]);
                }

                writer.write("\n");
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
