import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;



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
            c.setAutoCommit(false);

            stmt = c.createStatement();
//            final String sqlAllApps="select * from down";


            final String outRecords="select * from down where actionTime < \"2019-06-24T00:03:29.658Z\";";
   //         System.out.println(outRecords);

            ResultSet rsAllApps = stmt.executeQuery( outRecords );
            System.out.println(outRecords);

            while (rsAllApps.next()) {


                if(!rsAllApps.getString("Tactic").equals("0")){
                    System.out.println("Tactic: " + rsAllApps.getString("Tactic"));

                    // **** Get the latency

                    // Get the DateTime when the tactic started
                    final String nextRecordSearch="select ID, ActionTime from down where actionTime > \'"+ rsAllApps.getString("ActionTime") + "\' order by ActionTime limit 1;";
                    ResultSet rsNextRecord = stmt.executeQuery( nextRecordSearch );

                    final String DateStart = rsAllApps.getString("ActionTime").replace("Z","");

                    // Get the dateTime for the next tactic
                    final String nextTimeSearch="select ID, ActionTime from down where ID = " +  (rsNextRecord.getInt("ID") + 1) + ";";
                    ResultSet rsNextTime = stmt.executeQuery( nextTimeSearch );
                    System.out.println(rsNextTime.getString("ActionTime"));

                   // final String DateEnd = rsNextTime.getString("ActionTime").replace("T", " ").replace("Z","");
                    final String DateEnd = rsNextTime.getString("ActionTime").replace("Z","");

                    DateFormat df1 = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS");
                    Date result1 = df1.parse(DateStart);
                    Date result2 = df1.parse(DateEnd);

                    long Latencydiff = Math.abs(result1.getTime() - result2.getTime());

                    System.out.println(Latencydiff);


                }else{
                    System.out.println("Zero");
                }


                //if the tactic is not 0, then 1) Get the latecy 2) Get the average cost (All 0s before and after)



            }

            // close all the connections so the information can be written to the DB. Prevent locking
            stmt.close();
            rsAllApps.close();
            c.close();


        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }

    }


    public String convertStringToDate(Date indate)
    {
        String dateString = null;
        SimpleDateFormat sdfr = new SimpleDateFormat("dd/MMM/yyyy");
        /*you can also use DateFormat reference instead of SimpleDateFormat
         * like this: DateFormat df = new SimpleDateFormat("dd/MMM/yyyy");
         */
        try{
            dateString = sdfr.format( indate );
        }catch (Exception ex ){
            System.out.println(ex);
        }
        return dateString;
    }



}


// Read in the files



//  Go through the one file

// Find the date range


// Perform the computations


// Loop to the next file





