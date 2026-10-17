#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for ( int i = 0 ; i < height ; i++ )
    {
        for ( int j = 0 ; j < width ; j++)
        {
            int gray = round ((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue)/3.0);
            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
      for ( int i = 0 ; i < height ; i++ )
    {
        for ( int j = 0 ; j < width ; j++)
        {
            int sepiaRed = round (.393*image[i][j].rgbtRed + .769*image[i][j].rgbtGreen + .189*image[i][j].rgbtBlue);
            int sepiaGreen = round (.349*image[i][j].rgbtRed + .686*image[i][j].rgbtGreen + .168*image[i][j].rgbtBlue);
            int sepiaBlue = round (.272*image[i][j].rgbtRed + .534*image[i][j].rgbtGreen + .131*image[i][j].rgbtBlue);
            if (sepiaRed > 255) {image[i][j].rgbtRed = 255;} else {image[i][j].rgbtRed = sepiaRed;}
            if (sepiaGreen > 255) {image[i][j].rgbtGreen = 255;} else {image[i][j].rgbtGreen = sepiaGreen;}
            if (sepiaBlue > 255) {image[i][j].rgbtBlue = 255;} else {image[i][j].rgbtBlue = sepiaBlue;}
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            RGBTRIPLE swap = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = swap;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
        RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

        for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumred = 0,sumgreen = 0,sumblue = 0;
            int count = 0;
            for (int k = -1; k <= 1 ; k ++)
            {
                for(int l = -1; l <= 1; l ++)
                {
                    int n = l + i;
                    int m = k + j;
                    if  ( n >= 0 && n < height && m >=0 && m < width )
                    {
                        sumred += copy[n][m].rgbtRed;
                        sumgreen += copy[n][m].rgbtGreen;
                        sumblue += copy [n][m].rgbtBlue;
                        count ++;
                    }
                }
            }
        image[i][j].rgbtRed = round((float)sumred / count);
        image[i][j].rgbtGreen = round((float)sumgreen / count);
        image[i][j].rgbtBlue = round((float)sumblue / count); }
    }
    return;
}
