#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
bool only_alphas (string s);
char rotate (char a,string b);
int main (int argc, string argv[])
{
    if (argc == 2) {
                    if (only_alphas (argv[1]) == true) {if (strlen (argv[1]) == 26) {string p = get_string ("plaintext: ");
                                                                      printf ("ciphertext: ");
                                                                      for (int i = 0; i < strlen (p) ; i++) {printf ("%c",rotate (p[i],argv[1]));};
                                                                      printf ("\n");
                                                                      return 0;}
                                                        else {printf ("Key must contain 26 charecters.\n");
                                                        return 1;};}
                    else {
                          printf ("Usage: ./substitution key\n");
                          return 1;
                         };
                    }
    else {
          printf ("Usage: ./substitution key\n");
          return 1;
         };
}
bool only_alphas (string s)
{   int n = strlen (s);
    for (int i = 0; i < n; i++) {
                                    if (!isalpha(s[i])) {return false;};
                                    for (int j = i + 1; j < n; j++) {
                                                                     if (toupper(s[j]) == toupper(s[i])) {return false;};
                                                                    };
                                };
    return true;
}


char rotate (char a,string b)
{
    char d;
    if (isalpha (a)) {if (isupper (a)) {int c = (int) (a - 'A');
                                        d = b[c];
                                        return toupper(d);}
                      else {int c = (int) (a - 'a');
                            d = b[c];
                            return tolower(d);};}
    else {return a;};
}
