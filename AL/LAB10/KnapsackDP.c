#include <stdio.h>
#include <stdlib.h>

int max(int a, int b){
    return (a > b) ? a : b;
}

int knapsack(int W, int weight[], int value[], int n){
    int table[n + 1][W + 1];
    for(int i = 0; i <= n; i++){
        for(int j = 0; j <= W; j++){
            if(i == 0 || j == 0)
                table[i][j] = 0;
            else if(j - weight[i - 1] < 0)
                table[i][j] = table[i - 1][j]; 
            else
                table[i][j] = max(table[i - 1][j], value[i - 1] + table[i - 1][j - weight[i - 1]]);
        }
    }
    return table[n][W];
}


int main(){
    int weight[] = {1,2,3};
    int value[] = {10, 15, 40};
    int W = 5;
    int n = 3;
    printf("Max value is: %d", knapsack(W, weight, value, n));
    return 0;
}
