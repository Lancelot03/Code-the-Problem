#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
 
    int a,b;
    float x,y;
    scanf("%d %d",&a,&b);
    scanf("%f %f",&x,&y);
    printf("%d %d",a+b,a-b);
    printf("\n%.1f %.1f",x+y,x-y);
    return 0;
}
