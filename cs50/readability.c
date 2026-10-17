#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
int count_letters (string text);
int count_words (string text);
int count_sentences (string text);
int main (void)
{
    // Nhập dữ liệu từ người dùng
    string text = get_string ("Text: ");
    int letters = count_letters (text);
    int words = count_words (text);
    int sentences = count_sentences (text);
    float L = ((float)letters / (float)words)*100;
    float S = ((float)sentences / (float)words)*100;
    float index = 0.0588*L - 0.296*S - 15.8;
    if (index >= 16 ) {printf ("Grade 16+\n");}
    else if (index < 1) {printf ("Before Grade 1\n");}
    else {printf ("Grade %i\n",(int) round (index));};
    return 0;
}
    // Tính số chữ cái trong text
int count_letters (string text)
{
 int n = strlen (text);
 int s = 0;
 for (int i = 0; i < n; i++) {if (isalpha (text[i])) {s += 1;};};
 return s;
}

 int count_words (string text)
{
 int m = strlen (text);
 int q = 0;
 for (int j = 0; j < m; j++) {if (isblank (text[j])) {q += 1;};};
 q = q + 1;
 return q;
}
 int count_sentences (string text)
{
 int o = strlen (text);
 int k = 0;
 for (int l = 0; l < o; l++) {if ( text[l] == '?' || text[l] == '!' || text[l] == '.') {k += 1;};};
 return k;
}
