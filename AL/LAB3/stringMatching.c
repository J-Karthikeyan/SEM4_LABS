#include<stdio.h>
#include<string.h>

int substring(char str[], char substr[]){
    int m = strlen(str);
    int n = strlen(substr);
    int opcount = 0;
    for(int i=0; i<m-n+1; i++){
        int j = 0;
        while(j<n && str[i+j] == substr[j]){
            opcount++;
            j++;
        }
        if(j==n){
            printf("\nFound");
            return opcount;
        }
        opcount++;
    }
    printf("\nNot found");
    return opcount;
}

int main(){
    char str1[100];  
    char str2[100];  
    printf("\nEnter the string :");
    scanf("%s",str1);
    printf("\nEnter the target :");
    scanf("%s",str2);
    int op = substring(str1,str2);
    printf("\nop count : my%d",op);
    printf("\nm+n : %ld\n",strlen(str1)+strlen(str2));
}
