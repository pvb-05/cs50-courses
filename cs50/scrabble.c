#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
int main (void)
{
    string a = get_string ("Player 1: "), b = get_string ("Player 2: ");
    int n = strlen (a), m = strlen (b);
    int k = 26;
    int s = 0, t = 0;
    string score = "AEILNORSTUDGBCMPFHVWYKJXQZ";
    for ( int i = 0; i < n ; i ++) {   a [i] = toupper (a[i]);
                                       for ( int j = 0; j < k; j ++ ) { if ( a[i] == score [j] &&  j < 10 ) { s = s + 1;}
                                                                      else if ( a[i] == score [j] &&  ( j > 9 && j < 12 ) ) { s = s + 2;}
                                                                      else if ( a[i] == score [j] && ( j > 11 && j < 16 ) ) { s = s + 3;}
                                                                      else if ( a[i] == score [j] && ( j > 15 && j < 21 ) ) { s = s + 4;}
                                                                      else if ( a[i] == score [j] && j == 21 ) { s = s + 5;}
                                                                      else if ( a[i] == score [j] && ( j > 21 && j < 24 ) ) { s = s + 8;}
                                                                      else if ( a[i] == score [j] && ( j > 23 && j < 26 ) ) { s = s + 10;};};};
    for ( int l = 0; l < m ; l ++) {   b[l] = toupper ( b[l]);
                                       for ( int c = 0; c < k; c ++ ) { if ( b[l] == score [c] &&  c < 10 ) { t = t + 1;}
                                                                      else if ( b[l] == score [c] &&  ( c > 9 && c < 12 ) ) { t = t + 2;}
                                                                      else if ( b[l] == score [c] && ( c > 11 && c < 16 ) ) { t = t + 3;}
                                                                      else if ( b[l] == score [c] && ( c > 15 && c < 21 ) ) { t = t + 4;}
                                                                      else if ( b[l] == score [c] && c == 21 ) { t = t + 5;}
                                                                      else if ( b[l] == score [c] && ( c > 21 && c < 24 ) ) { t = t + 8;}
                                                                      else if ( b[l] == score [c] && ( c > 23 && c < 26 ) ) { t = t + 10;};};};
    if ( s > t ) {printf ("Player 1 wins!\n");}
    else if ( s < t ) {printf ("Player 2 wins!\n");}
    else {printf ("Tie!\n");};
}

