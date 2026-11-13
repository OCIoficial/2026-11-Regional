#include "testlib.h"

int main(int argc, char *argv[]) {
  auto subtask = std::string(argv[1]);

  registerValidation();

  int n = inf.readInt(1, 100'000, "N");
  inf.readSpace();
  int k = inf.readInt(1, n, "K");
  inf.readEoln();
  inf.readInts(n, 1, n, "C");
  inf.readEoln();
  inf.readInts(n, 1, n, "D");
  inf.readEoln();
  inf.readEof();

  if (subtask == "st1") {
    ensuref(k == n, "K debe ser igual a N");
  } else if (subtask == "st2") {
    ensuref(k == 1, "K debe ser 1");
  }
}
