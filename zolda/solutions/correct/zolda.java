// El costo mínimo es max(x) + N - 1: Lonk avanza de izquierda a derecha hasta
// x_i - 1 y dispara a x_i a distancia 1 (dejando libre x_i para poder pisarla
// si el siguiente meblin está en x_i + 1).
import java.io.*;
import java.util.*;

class zolda {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringTokenizer st = new StringTokenizer("");

  static String next() throws IOException {
    while (!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
    return st.nextToken();
  }

  public static void main(String[] args) throws IOException {
    int n = Integer.parseInt(next());
    long e = Long.parseLong(next());

    long mx = 0;
    for (int i = 0; i < n; i++) {
      long x = Long.parseLong(next());
      mx = Math.max(mx, x);
    }

    System.out.println(mx + n - 1 <= e ? "YES" : "NO");
  }
}
