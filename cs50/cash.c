#include <stdio.h>
#include <cs50.h>
int main (void)
{
 int n;
 int i = 0;
 do { n = get_int ("Change owed: ");} while ( n < 1);
 while ( n >= 1 )
{
 if ( n >= 25 )                 { n = n - 25;
                                  i++;       }
 else if ( n < 25 && n >= 10)   { n = n - 10;
                                  i++;       }
 else if ( n < 10 && n >= 5)    { n = n - 5;
                                  i++;       }
 else if ( n < 5 && n >= 1)     { n = n - 1;
                                  i++;       };
                                                };
 printf ("%i",i);
 printf ("\n");
}
