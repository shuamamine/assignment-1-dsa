 #include  <stdio.h>
 int main()
 {
      int n = 1;
      for (int i = 0; i < 5; i++)
      {
         for (int j = 0; j < i + 1; j++)
          {
            if (n % 2 != 0)
            {
                printf("*");
            }
             else
             {
                printf("#");
              }
              n++;
        }
            printf("\n");
       }
       return 0;
}
