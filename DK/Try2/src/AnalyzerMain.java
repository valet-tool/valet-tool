import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.sql.*;


public class AnalyzerMain {

    // SQLite Database Location
//    private final String DbLocation = "/Users/dxkvse/Desktop/Try1/data/Try1.sqlite";
    private final String DbLocation = "/Users/dkrutz/Documents/GIT/valet-tool/DK/data/Try1.sqlite";


    // Your program begins with a call to main().
    // Prints "Hello, World" to the terminal window.
    public static void main(String args[])
    {
       // System.out.println("Hello, World7.2");
        AnalyzerMain m = new AnalyzerMain();
        m.Run();
    }


    private void Run(){


        // loop through the records in the download table
        Connection c = null;
        Statement stmt = null;
        Statement stmt2 = null;
        try {
            Class.forName("org.sqlite.JDBC");

            c = DriverManager.getConnection("jdbc:sqlite:"+DbLocation);
            c.setAutoCommit(true); // can toggle to false

            stmt = c.createStatement();
            stmt2 = c.createStatement();

            final String sqlAllDown="select * from down where ID > 2 limit 1;";
            ResultSet rsAllDown = stmt.executeQuery( sqlAllDown );
            System.out.println(sqlAllDown);

            while (rsAllDown.next()) {
                System.out.println("Record Check: " + rsAllDown.getInt("ID"));


                int downID = rsAllDown.getInt("ID");
                if(rsAllDown.getInt("Tactic") != 0){ // Don't care about tactic 0


                    // **** Get the latency


                    // Get startDateTime
                    final String DateStart = rsAllDown.getString("ActionTime").replace("Z","");


                    // Get the time when the tactic ended
                    final String nextTimeSearch="select ID, ActionTime from down where ID = " +  (downID + 1) + ";";
                    System.out.println(nextTimeSearch);
                    ResultSet rsNextTime = stmt2.executeQuery( nextTimeSearch ); // need to be statement 2 to differentiate it from the other statement



                    final String DateEnd = rsNextTime.getString("ActionTime").replace("Z","");

                    DateFormat df1 = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS");
                    Date resultStart = df1.parse(DateStart);
                    Date resultEnd = df1.parse(DateEnd);

                    long Latencydiff = Math.abs(resultStart.getTime() - resultEnd.getTime());
                    //rsNextTime.close();
                    stmt2.close();

/*
                    String query = "update down set latency = ? where ID = ?";
                    PreparedStatement preparedStmt = c.prepareStatement(query);
                    preparedStmt.setLong   (1, Latencydiff);
                    preparedStmt.setInt   (2, downID);
                    preparedStmt.executeUpdate();
                    preparedStmt.execute();
*/

                    System.out.println("Latency Update -- ID: " +downID + " " + "Latency: " + Latencydiff);


                    // Now get the cost
                    System.out.println("****** Cost ********");



                    // Get Time Range before, during, after


                    // Get Date Before
                    final String findBeforeTime="select ID, ActionTime from down where ID = " +  (downID - 1) + ";";
                   // System.out.println(findBeforeTime);
                    ResultSet rsBeforeTime = stmt2.executeQuery( findBeforeTime ); // need to be statement 2 to differentiate it from the other statement


                    final String DateBefore = rsBeforeTime.getString("ActionTime").replace("Z","");

                    rsBeforeTime.close();

                    System.out.println("Before " + DateBefore);
                   System.out.println("During " + DateStart);
                    System.out.println("End " + DateEnd);


                   // 2019-06-24T00:03:28.000Z
                   // 2019-06-24T00:03:29.658Z
                   // 2019-06-24T00:08:05.000Z
                   // 2019-06-24T00:08:06.376Z

                    // Now get all the cost values for each of the three slots

                    final String findCostBefore="select ID, ActionTime, Cost1, Cost2 from out where ActionTime >= '"+DateBefore+ "' and ActionTime <= '" + DateStart +"';";
                    System.out.println(findCostBefore);
                    ResultSet rsCostBeforeVals = stmt2.executeQuery( findCostBefore ); // need to be statement 2 to differentiate it from the other statement

                    double Cost1Total = 0;
                    double Cost2Total = 0;
                    int RecordCount = 0;

                    //System.out.println(findCostBefore);
                    while (rsCostBeforeVals.next()) {

                           // System.out.println(rsCostBeforeVals.getInt("ID"));
                        RecordCount++;
                        Cost1Total = Cost1Total + rsCostBeforeVals.getDouble("Cost1");
                        Cost2Total = Cost2Total + rsCostBeforeVals.getDouble("Cost2");
                    }

                    rsCostBeforeVals.close();
                    stmt2.close();

                    final int CostBeforeRecordCount = RecordCount;
                    final double Cost1Before = Cost1Total/RecordCount;
                    final double Cost2Before = Cost2Total/RecordCount;

                    System.out.println("Record Count " + CostBeforeRecordCount);
                    System.out.println("Cost1 total " + Cost1Total + "Avg: " + Math.round(Cost1Before));
                    System.out.println("Cost2 total " + Cost2Total+ "Avg: " + Math.round(Cost2Before));





                    // Now Get the Average Cost During
                    final String findCostDuring="select ID, ActionTime, Cost1, Cost2 from out where ActionTime >= '" +DateStart + "' and ActionTime <= '"+  DateEnd  +"';";
                    System.out.println(findCostDuring);
                    ResultSet rsCostDuringVals = stmt2.executeQuery( findCostDuring ); // need to be statement 2 to differentiate it from the other statement

                    Cost1Total = 0;
                    Cost2Total = 0;
                    RecordCount = 0;

                    //System.out.println(findCostBefore);
                    while (rsCostDuringVals.next()) {

                        // System.out.println(rsCostBeforeVals.getInt("ID"));
                        RecordCount++;
                        Cost1Total = Cost1Total + rsCostDuringVals.getDouble("Cost1");
                        Cost2Total = Cost2Total + rsCostDuringVals.getDouble("Cost2");
                    }

                    rsCostDuringVals.close();
                    stmt2.close();

                    final int CostDuringRecordCount = RecordCount;
                    final double Cost1During = Cost1Total/RecordCount;
                    final double Cost2During = Cost2Total/RecordCount;

                    System.out.println("Record Count " + CostDuringRecordCount);
                    System.out.println("Cost1 total " + Cost1Total + "Avg: " + Math.round(Cost1During));
                    System.out.println("Cost2 total " + Cost2Total+ "Avg: " + Math.round(Cost2During));



                // Get the tactic cost for after


                    // Start by getting the end tactic time after

                    final String findCostAfterTactic="select ID, ActionTime from down where ID = " +  (downID + 2) + ";";
                    ResultSet findNextTatcitStartTime = stmt2.executeQuery( findCostAfterTactic ); // need to be statement 2 to differentiate it from the other statement

                    final String lastTacticTime =  findNextTatcitStartTime.getString("ActionTime");

               //     System.out.println("Last Tactic Time = " + lastTacticTime);

                    findNextTatcitStartTime.close();
                    stmt2.close();


                    final String findCostAfter="select ID, ActionTime, Cost1, Cost2 from out where ActionTime >= '" + DateEnd +   "' and ActionTime <= '"+ lastTacticTime +"';";
                    System.out.println(findCostAfter);
                    ResultSet rsCostAfterVals = stmt2.executeQuery( findCostAfter ); // need to be statement 2 to differentiate it from the other statement

                    Cost1Total = 0;
                    Cost2Total = 0;
                    RecordCount = 0;


                    //System.out.println(findCostBefore);
                    while (rsCostAfterVals.next()) {

                        // System.out.println(rsCostBeforeVals.getInt("ID"));
                        RecordCount++;
                        Cost1Total = Cost1Total + rsCostAfterVals.getDouble("Cost1");
                        Cost2Total = Cost2Total + rsCostAfterVals.getDouble("Cost2");
                    }

                    rsCostAfterVals.close();
                    stmt2.close();

                    final int CostAfterRecordCount = RecordCount;
                    final double Cost1After = Cost1Total/RecordCount;
                    final double Cost2After = Cost2Total/RecordCount;

                    System.out.println("Record Count " + CostAfterRecordCount);
                    System.out.println("Cost1 total " + Cost1Total + "Avg: " + Math.round(Cost1After));
                    System.out.println("Cost2 total " + Cost2Total+ "Avg: " + Math.round(Cost2After));



                    // Determine the average Differences
                    final double Cost1AvgDiff = Cost1During - ((Cost1Before + Cost1After)/2);
                    final double Cost2AvgDiff = Cost2During - ((Cost2Before + Cost2After)/2);


                    // Now update the values
                    System.out.println("**************************");
                    System.out.println("DownID: " + downID);
                    System.out.println("Cost1 Before: " + Cost1Before);
                    System.out.println("Cost1 During: " + Cost1During);
                    System.out.println("Cost1 After: " + Cost1After);
                    System.out.println("Avg Diff Cost1: " + Cost1AvgDiff);
                    System.out.println("Cost2 Before: " + Cost2Before);
                    System.out.println("Cost2 During: " + Cost2During);
                    System.out.println("Cost2 After: " + Cost2After);
                    System.out.println("Avg Diff Cost1: " + Cost2AvgDiff);



                    // Save all of the cost results
                    String query = "update down set Cost1 = ?, Cost2 = ?, Cost1Before = ?, Cost1During = ?, Cost1After = ?, Cost2Before = ?, Cost2During = ?, Cost2After = ? where ID = ?";
                    PreparedStatement preparedStmt = c.prepareStatement(query);
                    preparedStmt.setDouble  (1, Cost1AvgDiff);
                    preparedStmt.setDouble  (2, Cost2AvgDiff);
                    preparedStmt.setDouble  (3, Cost1Before);
                    preparedStmt.setDouble  (4, Cost1During);
                    preparedStmt.setDouble  (5, Cost1After);
                    preparedStmt.setDouble  (6, Cost2Before);
                    preparedStmt.setDouble  (7, Cost2During);
                    preparedStmt.setDouble  (8, Cost2After);
                    preparedStmt.setInt   (9, downID);
                    preparedStmt.executeUpdate();
                    preparedStmt.execute();


                    preparedStmt.close();


                    // Cost after

                   // select ID, ActionTime, Cost1, Cost2 from out where ActionTime >= '2019-06-24T00:08:05.000Z' and ActionTime <= '2019-06-24T00:08:06.376Z'


                    // Tactic Time below



                    // Get tactic 0 time before



                    // Get tactic 0 time after

                    // Get all cost values before

                    // Get all cost values after

                    // Get Average cost before, after

                    // Diff the cost during, with the cost after



                }else{
                    // Nothing to do since the tactic is 0.
                    System.out.println("Zero: " + rsAllDown.getString("ID"));
                }



            }

            // close all the connections so the information can be written to the DB. Prevent locking
            stmt.close();
            rsAllDown.close();
            c.close();


        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }

    }



}


// Read in the files



//  Go through the one file

// Find the date range


// Perform the computations


// Loop to the next file





// https://github.com/dan7800/AndroidMParser/tree/bdbe14111a372e0087939ecfcb027fcedc3be806/CommitAnalyzer/src

