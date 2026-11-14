#include "testlib.h"
#include <algorithm>
#include <string>
#include <vector>

int main(int argc, char *argv[]) {
  auto subtask = std::string(argv[1]);

  registerValidation();

  int n = inf.readInt(1, 100'000, "N");
  inf.readSpace();
  inf.readInt(1, 1'000'000'000, "E");
  inf.readEoln();

  std::vector<int> x = inf.readInts(n, 1, 1'000'000'000, "x");
  inf.readEoln();
  inf.readEof();

  std::sort(x.begin(), x.end());
  for (int i = 1; i < n; i++) {
    ensuref(x[i] != x[i - 1], "Las posiciones de los meblins deben ser distintas");
  }

  if (subtask == "st1") {
    ensuref(n == 1, "En la subtarea 1 debe cumplirse N = 1");
  } else if (subtask == "st2") {
    ensuref(x.back() - x.front() == n - 1,
            "En la subtarea 2 los meblins deben ocupar N posiciones consecutivas");
  }
}
