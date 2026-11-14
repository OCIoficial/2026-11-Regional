#include "testlib.h"

int main() {
  registerValidation();

  inf.readToken("[01]{10}", "S");
  inf.readEoln();
  inf.readEof();
}
