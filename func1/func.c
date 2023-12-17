#include <stdint.h>
#include <stdio.h>
#include <string.h>

int func() {

#ifndef SKIP
    printf("function1 \n");
#endif

    return 0;
}