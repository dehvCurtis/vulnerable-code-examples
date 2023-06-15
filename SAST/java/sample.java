public class Sample {
    public static void main(String[] args) {
      String password = "sensitivePassword";
      System.out.println("Received password: " + password);
    }
  }

// (CWE-259)
// This sample Java file includes code that prints a sensitive password to the console. 
// It can be used to test SAST tools' capability to detect hardcoded passwords.