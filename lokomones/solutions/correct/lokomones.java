// Calcula en O(1) cuántos ataques necesita cada lokomon para derrotar al otro
// usando división techo. Como Vichochú ataca primero, el lokomon i gana si y
// solo si necesita estrictamente menos ataques que Vichochú.
import java.io.*;
import java.util.*;

class lokomones {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringTokenizer st = new StringTokenizer("");

  static String next() throws IOException {
    while (!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
    return st.nextToken();
  }

  public static void main(String[] args) throws IOException {
    int k = Integer.parseInt(next());
    long[][] p = new long[k + 1][k + 1];
    for (int i = 1; i <= k; i++) {
      for (int j = 1; j <= k; j++) {
        p[i][j] = Long.parseLong(next());
      }
    }

    long h = Long.parseLong(next());
    long a = Long.parseLong(next());
    int t = Integer.parseInt(next());

    int n = Integer.parseInt(next());
    for (int i = 1; i <= n; i++) {
      long hi = Long.parseLong(next());
      long ai = Long.parseLong(next());
      int ti = Integer.parseInt(next());

      long danoV = a * p[t][ti];
      long danoI = ai * p[ti][t];

      long turnosV = (hi + danoV - 1) / danoV;
      long turnosI = (h + danoI - 1) / danoI;

      if (turnosI < turnosV) {
        System.out.println(i);
        return;
      }
    }

    System.out.println(-1);
  }
}
