// Recorre la cadena llevando la cantidad actual de ceros consecutivos y el
// máximo visto hasta el momento.
import java.io.*;

class horario {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = br.readLine().trim();

    int actual = 0, mejor = 0;
    for (int i = 0; i < s.length(); i++) {
      if (s.charAt(i) == '0') {
        actual++;
        mejor = Math.max(mejor, actual);
      } else {
        actual = 0;
      }
    }

    System.out.println(mejor);
  }
}
