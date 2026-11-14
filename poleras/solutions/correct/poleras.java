// Las poleras no usadas quedan al inicio de D en su orden original, así que
// D[0..N-K) debe ser subsecuencia de C. Además C y D deben tener los mismos
// colores. Ambas condiciones bastan.
import java.io.*;
import java.util.*;

class poleras {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringTokenizer st = new StringTokenizer("");

  static String next() throws IOException {
    while (!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
    return st.nextToken();
  }

  public static void main(String[] args) throws IOException {
    int n = Integer.parseInt(next());
    int k = Integer.parseInt(next());
    int[] c = new int[n], d = new int[n];
    for (int i = 0; i < n; i++) c[i] = Integer.parseInt(next());
    for (int i = 0; i < n; i++) d[i] = Integer.parseInt(next());

    HashMap<Integer, Integer> freq = new HashMap<>();
    for (int x : c) freq.merge(x, 1, Integer::sum);
    for (int x : d) freq.merge(x, -1, Integer::sum);

    for (int amount : freq.values()) {
      if (amount != 0) {
        System.out.println("NO");
        return;
      }
    }

    int pos = 0;
    for (int x : c) {
      if (pos < n - k && x == d[pos]) {
        pos++;
      }
    }

    System.out.println(pos == n - k ? "SI" : "NO");
  }
}
