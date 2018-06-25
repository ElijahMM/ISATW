#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "mpi.h"

void startMaster(int n, int m);
void startSlave(int m);
long factorial(int n);
char* transVecInSir(int* vec, int n);
void afiseazaRezultat(int* rezultat, int n);


void main(int argc, char** argv)
{
	int rank;
	int nrNoduri;
	int nrRanduri;
    
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);

	if(rank == 0)
	{	
		MPI_Comm_size(MPI_COMM_WORLD, &nrNoduri);
		printf("\nNumarul de noduri este %d.\n\n", nrNoduri);
		
		printf("Introdu numarul de randuri: ");
		scanf("%d", &nrRanduri);
		printf("\n");
        
		startMaster(nrRanduri, nrNoduri);
	}
	else
	{
		startSlave(rank);
	}

	MPI_Finalize();
}

void startMaster(int n, int m)
{
    MPI_Status status;
    int nrRanduriPerNod = n / (m - 1);
    
	for(int i = 1; i < m; i++)
	{		
		int randuriVec[nrRanduriPerNod + 1];
		
		for(int j = 0; j < nrRanduriPerNod; j++)
		{
			randuriVec[j + 1] = j * (m - 1) + (i - 1);
		}
        
        randuriVec[0] = nrRanduriPerNod;
		char* mesaj = transVecInSir(randuriVec, nrRanduriPerNod + 1);

		MPI_Send(randuriVec, 20, MPI_INT, i, 99, MPI_COMM_WORLD);
        printf("[MASTER] Am trimis randurile: '%s' catre SLAVE[%d].\n", mesaj, i);
        free(mesaj);
	}

    printf("\n");
    
    int totalVec[500];
    int totalLung = 0;

	for(int i = 1; i < m; i++)
	{
        int rezVec[100];
        MPI_Recv(rezVec, 100, MPI_INT, i, 99, MPI_COMM_WORLD, &status);
        
        int lung = rezVec[0];
        totalLung += lung;

        char* mesaj = transVecInSir(rezVec, lung + 1);
        printf("[MASTER] Am primit valorile '%s' de la SLAVE[%d].\n", mesaj, i);
        free(mesaj);
        
        int nrElem = 0;

        for(int rand = 0; rand < nrRanduriPerNod; rand++) {
            int r = rand * (m - 1) + (i - 1);
            int startPos = 0;
            
            if (r > 0) {
                startPos = r * (r + 1) / 2;
            }
            
            for (int j = startPos; j <= startPos + r; j++)
            {
                totalVec[j] = rezVec[nrElem + j - startPos + 1];
            }

            nrElem += r + 1;
        }
	}
 
    printf("\n");
    char* mesaj = transVecInSir(totalVec, totalLung);
    printf("%s\n\n", mesaj);
    afiseazaRezultat(totalVec, n);
}

void startSlave(int m)
{
	MPI_Status status;
    int randuriVec[20];
	MPI_Recv(randuriVec, 20, MPI_INT, 0, 99, MPI_COMM_WORLD, &status);
    
    int n = randuriVec[0];
	char* mesaj = transVecInSir(randuriVec, n + 1);
    printf("[SLAVE-%d] Am primit randurile: '%s'.\n", m, mesaj);
    
    int rezVec[100];

    int lungCurenta = 1;

    for(int i = 1; i < n + 1; i++) {

        for(int j = 0; j <= randuriVec[i]; j++)
        {
            rezVec[lungCurenta++] = factorial(randuriVec[i]) / (factorial(j) * factorial(randuriVec[i] - j));
        }
    }

    rezVec[0] = lungCurenta - 1;

    MPI_Send(rezVec, 100, MPI_INT, 0, 99, MPI_COMM_WORLD);
    mesaj = transVecInSir(rezVec, lungCurenta);
    printf("[SLAVE-%d] Am trimis urmatoarele valori: '%s'\n\n", m, mesaj);
    free(mesaj);
}

long factorial(int n)
{
	if(n <= 1) return 1;
	return n * factorial(n - 1);
}

char* transVecInSir(int vec[], int n)
{
	char* sir = (char*) malloc(n * sizeof(char) * 4 + 2);
    sir[0] = '\0';

    strcat(sir, "[");
    
	for(int i = 0; i < n; i++)
	{	
		char buffer[4];
        
		if (i < n - 1)
		{
			sprintf(buffer, "%d,", vec[i]);
		} 
		else
		{
			sprintf(buffer, "%d", vec[i]);
		}

		strcat(sir, buffer);
	}
    
    strcat(sir, "]\0");
    
	return sir;
}

void afiseazaRezultat(int* rezultat, int n)
{
	int nrElem = 0;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= (n - i - 2); j++)
        {
            printf(" ");
        }

        for (int j = 0; j <= i; j++) {
            printf("%1d ", rezultat[nrElem + j]);
        }

        nrElem += i + 1;

        printf("\n");
    }
}

