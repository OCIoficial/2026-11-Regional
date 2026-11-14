#include "testlib.h"
#include <string>

int main(int argc, char *argv[]) {
  auto subtask = std::string(argv[1]);

  registerValidation();

  int64_t max_h = (subtask == "st1") ? 1'000LL : 1'000'000'000LL;

  int k = inf.readInt(1, 100, "K");
  inf.readEoln();

  for (int i = 0; i < k; i++) {
    inf.readInts(k, 1, 10, "P");
    inf.readEoln();
  }

  inf.readLong(1LL, max_h, "H");
  inf.readSpace();
  inf.readLong(1LL, 100'000'000LL, "A");
  inf.readSpace();
  inf.readInt(1, k, "T");
  inf.readEoln();

  int n = inf.readInt(1, 100, "N");
  inf.readEoln();

  for (int i = 0; i < n; i++) {
    inf.readLong(1LL, max_h, "H_i");
    inf.readSpace();
    inf.readLong(1LL, 100'000'000LL, "A_i");
    inf.readSpace();
    inf.readInt(1, k, "T_i");
    inf.readEoln();
  }

  inf.readEof();
}
