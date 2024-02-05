#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N;

int **cost_matrix;

int *temporary_permutation;

int *best_permutation;
int best_cost;

int iter;

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int cost() {
    int c = 0;
    for (int i = 0; i < N; i++) {
        iter++;
        c += cost_matrix[i][temporary_permutation[i]];
    }
    return c;
}

void init() {

    temporary_permutation = malloc(N * sizeof(int));
    best_permutation = malloc(N * sizeof(int));

    for (int i = 0; i < N; i++) {
        iter++;
        best_permutation[i] = i;
        temporary_permutation[i] = i;
    }

    best_cost = cost();
}

void permute(int i) {
    if (i == N) {
        int alt_cost = cost();
        if (alt_cost < best_cost) {
            memcpy(best_permutation, temporary_permutation, N * sizeof(int));
            best_cost = alt_cost;
        }
        return;
    }

    for (int j = i; j < N; j++) { 
        iter++;
        swap(temporary_permutation + i, temporary_permutation + j);
        permute(i + 1);
        swap(temporary_permutation + i, temporary_permutation + j);
    }
}

int main() {
    while (1) {
        printf("\nHow many people (or jobs): ");
        scanf("%d", &N);

        cost_matrix = malloc(N * sizeof(*cost_matrix));
        for (int i = 0; i < N; i++) {
            printf("\nEnter the %d costs for person %d: ", N, i);

            cost_matrix[i] = malloc(N * sizeof(**cost_matrix));
            for (int j = 0; j < N; j++) 
                scanf("%d", &(cost_matrix[i][j]));
        }

        init();

        iter = 0;

        permute(0);
        
        for (int i = 0; i < N; i++) 
            printf("\nperson %d = job %d \n", i, best_permutation[i]);

        printf("\nIterations = %d\n", iter);
    }
}
