#include <stdio.h>
#include <string.h>

char *SECRET = "GNOSIS1_SUPER4_SECRET3_PASSWORD3";

int main() {
  char buffer[100];
  printf("Enter your password:: ");
  fgets(buffer, 100, stdin);
  buffer[strcspn(buffer, "\n")] = 0;

  if (strcmp(buffer, SECRET) == 0) {
    printf("Correct Password\n");
    printf("The Flag is gnosis{7h15_15_4_5up3r_53cr37_p455w0rd}\n");
  } else {
    printf("Better Luck next time\n");
  }
}
