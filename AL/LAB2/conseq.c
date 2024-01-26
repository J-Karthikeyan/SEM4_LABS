#include<stdio.h>
#include<stdlib.h>

typedef struct{
    int op;
    int mn;
}val;

int gcd(int m, int n){
    int op = 0;
    int temp = (m<n) ? m : n;
    while(temp>0){
        op++;
        if(m%temp == 0 && n%temp == 0){
            return op;
        }
        temp--;
    }
}

int main(){
    int m,n,input,i=0;
    val v[100];
    /*do{
        printf("1.inpu 0.exit\n");
        scanf("%d",&input);
        if(input){
            scanf("%d",&m);
            scanf("%d",&n);
            v[i].mn = m+n;
            v[i].op = gcd(m,n);
            i++;
        }
    }while(input);*/
    do{
        scanf("%d",&m);
        scanf("%d",&n);
        v[i].mn = m+n;
        v[i].op = gcd(m,n);
        i++;
    }while(m!=-1);
    for(int j=0; j<i; j++){
        printf("%d,",v[j].mn);
    }
    printf("\n");
    for(int j=0; j<i; j++){
        printf("%d,",v[j].op);
    }
    printf("\n");
}
