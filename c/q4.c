#include <stdio.h>
void main()
{
   int n;
   printf("Enter the limit : ");
   scanf("%d", &n);
   if(n==1)
     printf("%d\n", 1);
    else if(n==2)
     printf("%d\n", 2);
    else if(n==3)
     printf("%d\n", 6);
   else
    {
      int a=6,p=3,j=2;
      n=n-3;
      for(int i = 0;i<n;i++)
      {
          a+=(p*p);
          p+=j;
          j++
      }
      printf("sum = ", a);
}
