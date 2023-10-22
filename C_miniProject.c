
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define DataAcids "Data_Acids_All.txt"
#define nAcids 20
#define nElements 5
#define OxygenAtomicWeight 15.9994
#define CarbonAtomicWeight 12.011
#define NitrogenAtomicWeight 14.00674
#define SulfurAtomicWeight 32.066
#define HydrogenAtomicWeight 1.00794
/*
Mini Project 2
Purpose: Read from a file and store the values in an 2D array
Afterwards have the user declare a min and max for each column
of the array and filter out the rows that don't fit the users
Criteria Print out the acids that match and determine their
atomic weight to be printed
Author: Lawrence Alderton
*/
char elements[nElements][100] = { "Oxygen", "Carbon", "Nitrogen", "Sulfur",
"Hydrogen" };
char acids[nAcids][100] = {""};
int acidVals[nAcids][nElements] = { 0 };
const double atomicWeightsElements[nElements] = { OxygenAtomicWeight,
                                                    CarbonAtomicWeight,
                                                    NitrogenAtomicWeight,
                                                    SulfurAtomicWeight,
                                                    HydrogenAtomicWeight
};
double atomicWeightsAcids[nAcids] = { 0 };
int min[nElements] = { 0 };
int max[nElements] = { 0 };
int matchMatrix[nAcids][nElements] = { 0 };
void FindMatches_Alderton_Lawrence()
{
    int valCheck = 0;
    int numFound = 0;
    double sumWeight = 0;
    double avgWeight = 0;
    printf("\nSearch Results for Your Query\n");
    printf("--------------------------------\n");
    for (int index = 0; index < nAcids; index++)
    {
        for (int index2 = 0; index2 < nElements; index2++)
        {
            if (acidVals[index][index2] >= min[index2] && acidVals[index]
            [index2] <= max[index2])
            {
                matchMatrix[index][index2] = 1;
                valCheck += matchMatrix[index][index2];
            }
            if (valCheck == 5)
            {
                numFound++;
                sumWeight += atomicWeightsAcids[index];
                printf("\t%s (%lf)\n", acids[index],
                atomicWeightsAcids[index]);
            }
        }
            valCheck = 0;
    }
    if (numFound != 0)
    {
        avgWeight = sumWeight / numFound;
        printf("--------------------------------\n");
        printf("Average Weights of ALL Found Acids %lf\n", avgWeight);
    }
    else
    {
        printf("\tNO Results Match Your Query\n");
    }
}
int Alderton_Lawrence()
{
    int index = 0;
    FILE* data = fopen(DataAcids, "r");
    if (data != NULL)
    {
        printf("The file contains %d data points\n", nAcids);
        printf("--------------------------------\n");
        while (!feof(data))
        {
            fscanf(data, "%s %d %d %d %d %d", &acids[index],
            &acidVals[index]
            [0],
            &acidVals[index]
            [1],
            &acidVals[index]
            [2],
            &acidVals[index]
            [3],
            &acidVals[index]
            [4]);
            printf("%d\t%d\t%d\t%d\t%d\n", acidVals[index][0],
            acidVals[index][1],
            acidVals[index][2],
            acidVals[index][3],
            acidVals[index][4]);
            index++;
        }
        printf("--------------------------------\n");
        for (int element = 0; element < nElements; element++)
        {
            printf("Enter the %s Atoms Range (min,max): ",
            elements[element]);
            scanf_s("%d,%d", &min[element], &max[element]);
            if (getchar() != '\n')
            {
            min[element] = -1;
            }
            while (min[element] < 0 || max[element] < 0)
            {
                printf("Please Enter positive values for %s Atoms Range
                (min,max): ", elements[element]);
                scanf_s("%d,%d", &min[element], &max[element]);
                if (getchar() != '\n')
                {
                    min[element] = -1;
                }
            }
        }
        for (int acid = 0; acid < nAcids; acid++)
        {
        for (int element = 0; element < nElements; element++)
        {
        atomicWeightsAcids[acid] += atomicWeightsElements[element]
        * acidVals[acid][element];
        }
        }
        FindMatches_Alderton_Lawrence();
    }
    else
    {
    printf("\n open unsuccessful");
    }
    return 0;
}
