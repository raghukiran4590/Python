import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class CloudSqlPostgresExample {

    public static Connection connectToDatabase(String dbName, String instanceConnectionName, String user, String password) {
        // The JDBC URL for Cloud SQL Postgres with the connector
        String jdbcUrl = String.format(
            "jdbc:postgresql://localhost/%s",
            dbName);

        // Connection properties
        Properties props = new Properties();
        props.setProperty("user", user);
        props.setProperty("password", password);
        // Specify the Cloud SQL connection properties
        props.setProperty("socketFactory", "com.google.cloud.sql.postgres.SocketFactory");
        props.setProperty("cloudSqlInstance", instanceConnectionName);
        // Optional: use private IP (if configured and applicable)
        // props.setProperty("usePrivateIp", "true"); 

        Connection conn = null;
        try {
            // Register the driver (optional for modern JDBC but good practice)
            Class.forName("org.postgresql.Driver");
            
            conn = DriverManager.getConnection(jdbcUrl, props);
            System.out.println("Connection successful!");
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
            System.err.println("Connection failed!");
        }
        return conn;
    }

    public static void main(String[] args) {
        // Replace with your instance details
        String databaseName = "postgres";
        String instanceName = "dig-apm1017605-gld-017n:us-east4:gpgsql-apm1017605-00uat01";
        String dbUser = "srctopology";
        // String dbPassword = "8ZY#REBX3";

        Connection connection = connectToDatabase(databaseName, instanceName, dbUser, dbPassword);
        
        // Use the connection for database operations...

        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();
                System.out.println("Connection closed.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
