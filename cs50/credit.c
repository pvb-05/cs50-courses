#include <stdio.h>
#include <cs50.h>
int main (void)
{
  long n = get_long ("Number: ");
  long l = n;
  int a = 0, s = 0, f, m, i;
  while ( n > 0 )  {i = n % 10;
                    n = n / 10;
                    int k = 2*i;
                    a++;
                    if ( a % 2 == 0 ) {if ( k / 10 >= 1 ) {    f = 0;
                                                               while ( k > 0) {  f = f + (k % 10);
                                                                                 k = k / 10; };
                                                               s = s + f;                              }
                                       else { s = s + k;}; }
                    else { s = s + i;};};
 while ( l >= 100)  {l = l / 10;}
 m = l;
 if ( s % 10 == 0 ) {if ((m == 34 || m == 37) && a == 15) {printf ("AMEX\n");}
                        else if ((m >= 51 && m <= 55) && a == 16) {printf ("MASTERCARD\n");}
                        else if ( (m / 10 == 4) && ( a == 13 || a == 16)) {printf ("VISA\n");}
                        else {printf ("INVALID\n");}; }
 else {printf ("INVALID\n");};
}
