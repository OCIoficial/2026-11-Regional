// Checker para respuestas SI/NO.
//
// Acepta tanto `SI` como `YES` como respuesta positiva, y `NO` como respuesta
// negativa, independiente de cuál de las dos variantes use el enunciado. La
// comparación distingue mayúsculas y minúsculas. Este mismo archivo se usa en
// poleras y zolda.
#include <fstream>
#include <iostream>
#include <string>

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

// 1 si es positiva, 0 si es negativa, -1 si no es válida.
int parse(const string &s) {
  if (s == "SI" || s == "YES") return 1;
  if (s == "NO") return 0;
  return -1;
}

int main(int argc, char *argv[]) {
  if (argc < 4) {
    cerr << "Uso: checker <in> <expected> <out>\n";
    return 1;
  }

  ifstream expf(argv[2]);
  ifstream outf(argv[3]);

  string expected_tok;
  expf >> expected_tok;
  int expected = parse(expected_tok);
  if (expected == -1) {
    cerr << "Salida esperada invalida: " << expected_tok << '\n';
    return 1;
  }

  string user_tok;
  if (!(outf >> user_tok)) {
    return fail("Salida vacia");
  }

  string extra;
  if (outf >> extra) {
    return fail("Salida contiene tokens adicionales");
  }

  int user = parse(user_tok);
  if (user == -1) {
    return fail("Respuesta invalida: " + user_tok);
  }

  if (user != expected) {
    return fail("Se esperaba " + expected_tok + ", pero se imprimio " + user_tok);
  }

  return ok();
}
