#include <iostream>
#include <cmath>
#include <vector>



/*
1 different function:

-fibonacci:
    input:
        int n     max value of the sum
    output:
        double F/F_1   rate of F/F_1 (where F(n)=(n-2)+(n-1))
                    and F_1=F(n-1) 
*/

extern "C"  // need for a compiler to recognize the function

double fibonacci(int n){
    double F=0;
    double F_1=0;
    if(n<=0){
        return 0;
    } 
    if(n==1){
        F=1;
        F_1=1;
    }
    if(n==2){
        F=1;
        F_1=1;
    }
    else{
        F=1;
        F_1=1;
        double F_2=1;
        for(int i=3;i<=n;i++){
            F_1=F;
            F=F_1+F_2;
            F_2=F_1;
            ;
        }
    }
    return F/F_1;
}


