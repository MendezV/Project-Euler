//
//  12.c
//  
//
//  Created by Juan Felipe Méndez on 9/12/14.
//
//

#include <stdio.h>
#include <math.h>


// A function to return the number of divisors of a given number
int NumberOfDivisors(int n)
{
    int count=0;
    int divisors=1;
    //count the number of 2's
    while (n%2 == 0)
    {
        //printf("%d ", 2);
        n = n/2;
        count+=1;
    }
   
    
    divisors=divisors*(count+1);

    

    for (int i = 3; i <= n; i = i+2)
    {
        count=0;
        
        while (n%i == 0)
        {
          //  printf("%d ", i);
            n = n/i;
            count+=1;
        }
       
        divisors=divisors*(count+1);
    }
    
  
    return divisors;
}


int main(){
    int i,s,count ;
    i=1;
    s=0;
    count=0;
    while(count<500){
    s=s+i;
    count= NumberOfDivisors(s);
    i++;
    }
    printf("%d \n",s);
    count= NumberOfDivisors(76576500 );
    printf("%d \n",count);
}
