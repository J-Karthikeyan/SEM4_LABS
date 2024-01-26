#include <stdio.h>

typedef struct{
    int op;
    int mn;
}val;

int gcd(int m, int n) {
    int op = 0;
    int i, j, x = 1, min;
    int mFactors[100], nFactors[100];
    int mSize = 0, nSize = 0;

    for (i = 2; i <= m; i++) {
        while (m % i == 0) {
            mFactors[mSize++] = i;
            m /= i;
        }
        op++;
    }

    for (i = 2; i <= n; i++) {
        while (n % i == 0) {
            nFactors[nSize++] = i;
            n /= i;
        }
        op++;
    }

    i = 0; j = 0;
    while (i < mSize && j < nSize) {
        op++;
        if (mFactors[i] < nFactors[j]) {
            i++;
        } else if (nFactors[j] < mFactors[i]) {
            j++;
        } else {
            min = mFactors[i];
            x *= min;
            i++; j++;
        }
    }

    return op;
}

int main(){
    int m,n,input,i=0;
    val v[100];
    do{
        printf("1.inpu 0.exit\n");
        scanf("%d",&input);
        if(input){
            scanf("%d",&m);
            scanf("%d",&n);
            v[i].mn = m+n;
            v[i].op = gcd(m,n);
            i++;
        }
    }while(input);
    for(int j=0; j<i; j++){
        printf("%d,",v[j].mn);
    }
    printf("\n");
    for(int j=0; j<i; j++){
        printf("%d,",v[j].op);
    }
    printf("\n");
}