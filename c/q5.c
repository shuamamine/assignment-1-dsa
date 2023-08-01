#include <stdio.h>
void main()
{
int k,n,b;
printf("Enter limit!"); 
scanf("%d", &n);
int a[n];
printf("Enter elements of array); 
for (int i=0; i<n;i++)
{
  scanf("%d", &a[i]);
}
printf("Enter location : ");
scanf("%d", 4k);
printf("Enter number :"); 
scanf("%d", 4b);
if(k < 0 || k > n)
{
 printf("Invalid location\n"); 
 return 0;
}
for (int i= n; i>=k; i--)
{
a[i] = a[i-1];
}
a[k] = b;
printf(" New array:");
for (int i=0; i<=n; i++)
{ 
printf("%d", a[i]);
}
printf("\n");
return 0;
}
