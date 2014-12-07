//
//  FindPrimes.c
//  
//
//  Created by Juan Felipe Méndez on 7/12/14.
//
//

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int FindPrimes(int n);

//para n mayor a 5
int FindPrimes(n){
    int count,r,f;
    count=1;
  
    if(n%2==0){
        count=0;
    }
    else if(n%3==0){
        count=0;
    }
    else{
        r=floor(sqrt(n));
        f=5;
        while(f<=r){
            if(n%f==0){
                count=0;
            }
            if(n%(f+2)==0){
                count=0;
            }
            f=f+6;
        }
    }
    return count;
}
int main(int argc, char **argv)
{
    int i,n,prime;
    n=atoi(argv[1]);
    FILE *in0;
    char filename[100];
    sprintf(filename, "primos_menores_a_%s.dat", argv[1]);
    in0 = fopen(filename,"w");
   
    fprintf(in0,"%d \n",2);
    fprintf(in0,"%d \n",3);
    fprintf(in0,"%d \n",5);
    for(i=6;i<n;i++){
        prime=FindPrimes(i);
        if (prime==1){
            fprintf(in0,"%d \n",i);
        }
    
    }
    
}