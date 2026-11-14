#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int fail(const string &msg) {
  cout << "0.0\n";
  cerr << msg << '\n';
  return 0;
}

int ok() {
  cout << "1.0\n";
  return 0;
}

int main(int argc, char *argv[]) {
  if (argc < 4) {
    cerr << "Uso: checker <in> <expected> <out>\n";
    return 1;
  }

  ifstream inf(argv[1]);
  ifstream expf(argv[2]);
  ifstream outf(argv[3]);

  int k;
  inf >> k;
  vector<vector<int64_t>> p(k + 1, vector<int64_t>(k + 1));
  for (int i = 1; i <= k; i++) {
    for (int j = 1; j <= k; j++) {
      inf >> p[i][j];
    }
  }

  int64_t h, a;
  int t;
  inf >> h >> a >> t;

  int n;
  inf >> n;
  vector<bool> gana(n + 1, false);
  bool alguno_gana = false;

  for (int i = 1; i <= n; i++) {
    int64_t hi, ai;
    int ti;
    inf >> hi >> ai >> ti;

    int64_t dano_v = a * p[t][ti];
    int64_t dano_i = ai * p[ti][t];

    int64_t turnos_v = (hi + dano_v - 1) / dano_v;
    int64_t turnos_i = (h + dano_i - 1) / dano_i;

    if (turnos_i < turnos_v) {
      gana[i] = true;
      alguno_gana = true;
    }
  }

  int expected_ans;
  expf >> expected_ans;

  int64_t user_ans;
  if (!(outf >> user_ans)) {
    return fail("Salida vacia o formato invalido");
  }

  string extra;
  if (outf >> extra) {
    return fail("Salida contiene tokens adicionales");
  }

  if (!alguno_gana) {
    if (user_ans == -1) return ok();
    return fail("Se esperaba -1, pero se imprimio " + to_string(user_ans));
  }

  if (user_ans < 1 || user_ans > n) {
    return fail("Indice fuera de rango: " + to_string(user_ans));
  }

  if (!gana[user_ans]) {
    return fail("El lokomon elegido no derrota a Vichochu");
  }

  return ok();
}
