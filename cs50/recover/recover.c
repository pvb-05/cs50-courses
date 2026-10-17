#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {printf("Usage: ./recover FILE\n");
     return 2;};
     uint8_t buffer[512];
     int numberofimage = 0;
     char *filename = malloc (8);
     FILE *img = NULL;
     while (fread(buffer,sizeof(uint8_t),512,card) == 512)
    {   if (img != NULL) {}
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
         if (img != NULL) {fclose (img);}
         sprintf (filename, "%03i.jpg", numberofimage);
         img = fopen(filename, "w");
         if (img == NULL) {printf("Usage: ./recover FILE\n");
                           fclose (card);
                           return 3;};
         numberofimage++;
        }
        if (img != NULL) {fwrite(buffer,sizeof(uint8_t),512,img);}
    }
    if (img != NULL) {fclose(img);};
    free (filename);
    fclose (card);
}
