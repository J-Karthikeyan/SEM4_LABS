#include<stdio.h>
#include<stdlib.h>

int main(){
    printf("Enter the length of array : ");
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0; i<n; i++)
        scanf("%d",&arr[i]);
    
    int opcount = 0;
    int swap = 0;
    for(int i=0; i<n-1; i++){
        for(int j=0; j<n-i-1; j++){
            opcount++;
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swap++;
            }
        }
    }

    for(int i=0; i<n; i++)
        printf("%d ",arr[i]);
    
    printf("\nOPcount is %d\nswaps is %d\n",opcount,swap);
    return 0;
}