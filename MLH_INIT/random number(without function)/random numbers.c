#include <stdio.h>
#include <stdlib.h>
int main()
{
    for (int i = 0; i < 5; i++)
    {
        int *p;
        p = (int *)malloc(sizeof(int));
        int res = ((int)p % 10) + 20;   
        printf("%d\n", res);
    }
    return 0;
}
