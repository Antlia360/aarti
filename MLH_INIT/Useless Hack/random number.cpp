#include <stdio.h>
#include <stdlib.h>
int main()
{
    int c, n;

    printf("Ten random numbers in [1,200]\n");

    for (c = 1; c <= 10; c++)
    {
        n = rand() % 200 + 1;
        printf("%d\n", n);
    }

    return 0;
}
