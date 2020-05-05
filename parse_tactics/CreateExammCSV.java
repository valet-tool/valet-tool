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
    public static DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSSSSS");
    public static int numberServers = 3;
    public static int numberTactics = 5;
    public static boolean normalize;

    public static void main(String[] arguments) {
        if (arguments.length != 5) {
            System.err.println("Incorrect arguments, usage:");
            System.err.println("java CreateExammCSV <ping filename> <tva output filename> <training file percent> <testing file percent> <normalize>");
            System.exit(1);
        }

        String pingFilename = arguments[0];
        String tvaFilename = arguments[1];
        double trainingPercent = Double.parseDouble(arguments[2]);
        double validationPercent = Double.parseDouble(arguments[3]);
        normalize = Integer.parseInt(arguments[4]) != 0;

        //make an output file for each server and tactic

        TVAOutput[][] tvas = new TVAOutput[numberServers][numberTactics];
        for (int i = 0; i < tvas.length; i++) {
            for (int j = 0; j < tvas[i].length; j++) {
                tvas[i][j] = new TVAOutput(i + 1, j + 1);
            }
        }

        try {
            //create a buffered reader given the filename (which requires creating a File and FileReader object beforehand)
            BufferedReader bufferedReader = new BufferedReader(new FileReader(new File(tvaFilename)));
            ArrayList<String> lines = new ArrayList<String>();

            String line = bufferedReader.readLine(); //skip the first line

            int i = 1;
            while ((line = bufferedReader.readLine()) != null) {
                //System.out.println("read: '" + line + "'");
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

                TVAOutput tva = tvas[server - 1][tactic - 1];
                tva.addTVARow(timestamp, server, tactic, latency, cost, reliability);
                //System.out.println("line " + i + " " + tva.getLastTVARow().toString());
                i++;
            }

        } catch (IOException e) {
            System.err.println("ERROR opening TVAFile: '" + tvaFilename + "'");
            e.printStackTrace();
            System.exit(1);
        }

        //sort and set the time since last recordings for each TVA file
        for (int i = 0; i < tvas.length; i++) {
            for (int j = 0; j < tvas[i].length; j++) {
                tvas[i][j].setTimeSinceLastRecording();
            }
        }

        //now read all the ping info

        try {
            //create a buffered reader given the filename (which requires creating a File and FileReader object beforehand)
            BufferedReader bufferedReader = new BufferedReader(new FileReader(new File(pingFilename)));

            String line = bufferedReader.readLine(); //ignore the first line

            int i = 1;
            while ((line = bufferedReader.readLine()) != null) {
                //System.out.println("read: '" + line + "'");

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

                //fix the bug where failed pings will report the tactic as 0
                if (tactic == 0) tactic = 1;

                TVAOutput tva = tvas[server - 1][tactic - 1];
                tva.addPingRow(timestamp, server, tactic, pingSuccess, pingTime);

                //System.out.println("line " + i + " " + tva.getLastPingRow().toString());
                i++;
            }

        } catch (IOException e) {
            System.err.println("ERROR opening PingFile: '" + pingFilename + "'");
            e.printStackTrace();
            System.exit(1);
        }


        //set the ping times for each row
        for (int i = 0; i < tvas.length; i++) {
            for (int j = 0; j < tvas[i].length; j++) {
                tvas[i][j].mergePingTimes();
            }
        }

        if (normalize) {
            double[] mins = new double[7];
            double[] maxs = new double[7];
            for (int i = 0; i < 7; i++) {
                mins[i] = Double.MAX_VALUE;
                maxs[i] = -Double.MAX_VALUE;
            }

            for (int i = 0; i < tvas.length; i++) {
                for (int j = 0; j < tvas[i].length; j++) {
                    TVAOutput tva = tvas[i][j];

                    tva.updateMinMax(mins, maxs);
                }
            }

            System.out.println("latency range:                " + mins[0] + " to " + maxs[0]);
            System.out.println("cost range:                   " + mins[1] + " to " + maxs[1]);
            System.out.println("reliability range:            " + mins[2] + " to " + maxs[2]);
            System.out.println("timeSinceLastRecording range: " + mins[3] + " to " + maxs[3]);
            System.out.println("timeSinceLastPing range:      " + mins[4] + " to " + maxs[4]);
            System.out.println("pingSuccess range:            " + mins[5] + " to " + maxs[5]);
            System.out.println("pingTime range:               " + mins[6] + " to " + maxs[6]);

            for (int i = 0; i < tvas.length; i++) {
                for (int j = 0; j < tvas[i].length; j++) {
                    TVAOutput tva = tvas[i][j];

                    tva.normalize(mins, maxs);
                }
            }

        }

        try {
            for (int i = 0; i < tvas.length; i++) {
                for (int j = 0; j < tvas[i].length; j++) {
                    TVAOutput tva = tvas[i][j];

                    tva.writeToFile(trainingPercent, validationPercent);
                }
            }

        } catch (IOException e) {
            System.err.println("Error writing out files: " + e);
            e.printStackTrace();
        }
    }

}
