#include <stdio.h>
#include <vector>
#include <cstring>
#include <math.h>
#include <algorithm>

using namespace std;

#define MAX 10000000

#define SIEVE_SIZE (MAX-1)/2

#define sieveIndexToNatural(j) 2*j+3

#define naturalToSieveIndex(j) (j-3)/2

int primePositions[SIEVE_SIZE];

vector<int> primes{2};

void sieve()
{
    int position = 1, idx_i, idx_j;
    int i;
    for (i = 3; i*i <= MAX; i+=2)
    {   
        idx_i = naturalToSieveIndex(i);
        if(primePositions[idx_i] == 0) //número primo ainda não visitado
        {
            primePositions[idx_i] = position;
            primes.push_back(i);
            position++;
            for(int j = i*i; j <= MAX; j += 2*i)
            {
                idx_j = naturalToSieveIndex(j);
                primePositions[idx_j] = -1; //número não é primo
            }
        }
        
    }

    for (int j = i; j <= MAX; j+=2) 
    {
        idx_j = naturalToSieveIndex(j);
        if(primePositions[idx_j] == 0)
        {   
            primePositions[idx_j] = position;
            primes.push_back(j);
            position++;
        }   
    }
}


int main(int argc, char const *argv[])
{
    long long input;
    
    sieve();

    while(true)
    {
        scanf("%lld", &input);
        
        if(input == 0)
        {
            break;
        }

        input = input < 0 ? -input : input; 

        if(input == 1)
        {
            printf("-1\n");
        }
        else
        {
            int i;
            long long largest = 2;
            int count = 0;
            // if(input % 2 == 0)
            // {
            //     for(; input % 2 == 0; input /= 2)
            //     {
            //         largest = 2;
            //         count++;
            //     }
            // }

            for (i = 0; i < primes.size() && primes[i] <= input; i++)
            {
                for(; input % primes[i] == 0; input /= primes[i])
                {
                    largest = primes[i];
                    count++;
                }
            }

            if(input > primes[primes.size()-1] || primePositions[naturalToSieveIndex(input)] != -1)
            {
                count++;
                largest = max(input, largest);
            }

            if(count < 2)
            {
                printf("-1\n");
            }
            else
            {
                printf("%lld\n", largest);
            }
        }     
         
    }

    return 0;
}
