#include <stdio.h>
#include <stdlib.h>

#define MAX 10


int g[MAX][MAX];
int V;
int visited[MAX];
int stack[MAX];
int tos = -1;

void push(int x){
    if(tos < MAX)
        stack[++tos] = x;
}

int pop(){
    if(tos == -1)
        return -1;
    return stack[tos--];
}

void dfsv(int v){
	visited[v] = 1;
	for(int i = 0; i < V; i++){
		if(!(visited[i]) && (g[v][i] == 1))
  			dfsv(i);
	}
	push(v);
}

void topoSort(){
	for(int i = 0; i < V; i++){
		if(!visited[i])
  			dfsv(i);
	}
}

int main(){
	printf("Enter the Number of Vertices: \n");
	scanf("%d", &V);
	int i, j;
	printf("Enter the Adjacency Matrix: \n");
	for(i = 0; i < V; i++){
		visited[i] = 0; 
		for(j = 0; j < V; j++)
			scanf(" %d", &g[i][j]);
	}
    printf("\n");
    
	topoSort();
    for(int i=0; i<V; i++){
        printf("%d ", pop());
    }

    printf("\n");
	return 0;
}

/*
sample 6x6 matrix : 

TO BE USED WHILE INPUT

0 1 1 0 0 0 
0 0 0 1 1 0 
0 0 0 1 0 1
0 0 0 0 1 1 
0 0 0 0 0 0 
0 0 0 0 0 0

POP ORDER
0 2 1 3 5 4
*/
