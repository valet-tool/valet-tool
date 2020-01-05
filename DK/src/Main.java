import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.sql.*;



public class Main {

    // SQLite Database Location
    private final String DbLocation = "/Users/dxkvse/Desktop/Try1/data/Try1.sqlite";

    public static void main(String[] args) {
        Main m = new Main();
        m.Run();
    }

    private void Run(){

        // loop through the records in the download table
        Connection c = null;
        Statement stmt = null;
        try {
            Class.forName("org.sqlite.JDBC");

            c = DriverManager.getConnection("jdbc:sqlite:"+DbLocation);
            c.setAutoCommit(true); // can toggle to false

            stmt = c.createStatement();


            final String sqlAllDown="select * from down where ID > 2  and ID < 5 limit 10;";
//            final String sqlAllDown="select * from down limit 10";

  //          final String outRecords="select * from down where actionTime < \"2019-06-24T00:03:29.658Z\";";
   //         System.out.println(outRecords);

            ResultSet rsAllDown = stmt.executeQuery( sqlAllDown );
            System.out.println(sqlAllDown);

            while (rsAllDown.next()) {

                int downID = rsAllDown.getInt("ID");
                if(!rsAllDown.getString("Tactic").equals("0")){
                   // System.out.println("Tactic: " + rsAllDown.getString("Tactic"));

                    // **** Get the latency


                    // Get startDateTime
                    final String DateStart = rsAllDown.getString("ActionTime").replace("Z","");


                    // Get the time when the tactic ended
                    final String nextTimeSearch="select ID, ActionTime from down where ID = " +  (rsAllDown.getInt("ID") + 1) + ";";
                    ResultSet rsNextTime = stmt.executeQuery( nextTimeSearch );

                    final String DateEnd = rsNextTime.getString("ActionTime").replace("Z","");

                    DateFormat df1 = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS");
                    Date result1 = df1.parse(DateStart);
                    Date result2 = df1.parse(DateEnd);

                    long Latencydiff = Math.abs(result1.getTime() - result2.getTime());

                    String query = "update down set latency = ? where ID = ?";
                    PreparedStatement preparedStmt = c.prepareStatement(query);
                    preparedStmt.setLong   (1, Latencydiff);
                    preparedStmt.setInt   (2, downID);
                    preparedStmt.executeUpdate();
                    preparedStmt.execute();


                    System.out.println("Latency Update -- ID: " +downID + " " + "Latency: " + Latencydiff);


                }else{
                    // Nothing to do since the tactic is 0.
                    System.out.println("Zero: " + rsAllDown.getString("ID"));
                }


                //if the tactic is not 0, then 1) Get the latecy 2) Get the average cost (All 0s before and after)



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
