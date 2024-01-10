#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

typedef struct Node {
    struct Node *next;
    int toVertex;
    int weight;
} Node;

typedef struct Graph {
    struct Graph *down;
    Node *components;
    int fromVertex;
} Graph;

Node *createNode(int toVertex, int weight) {
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->next = NULL;
    temp->toVertex = toVertex;
    temp->weight = weight;
    return temp;
}

Graph *createVertex(int from, int to, int weight) {
    Graph *temp = (Graph *)malloc(sizeof(Graph));
    temp->fromVertex = from;
    temp->components = createNode(to, weight);
    temp->down = NULL;
    return temp;
}

void connect(Graph **g, int from, int to, int weight) {
    if ((*g) == NULL) {
        (*g) = createVertex(from, to, weight);
        return;
    }
    Graph *temp = *g;
    while (temp->down != NULL) {
        if (temp->fromVertex == from) {
            Node *node = temp->components;
            while (node->next != NULL) {
                node = node->next;
            }
            node->next = createNode(to, weight);
            return;
        } else {
            temp = temp->down;
        }
    }
    if (temp->fromVertex == from) {
        Node *node = temp->components;
        while (node->next != NULL) {
            node = node->next;
        }
        node->next = createNode(to, weight);
        return;
    }
    temp->down = createVertex(from, to, weight);
}

void displayList(Graph *g) {
    while (g) {
        printf("%d : ", g->fromVertex);
        Node *node = g->components;
        while (node) {
            printf("(%d,%d) ", node->toVertex, node->weight);
            node = node->next;
        }
        g = g->down;
        printf("\n");
    }
}

void displayMatrix(Graph *g) {
    Graph *temp = g;
    int max = 0;
    while (temp) {
        if (temp->fromVertex > max)
            max = temp->fromVertex;
        temp = temp->down;
    }

    int matrix[max][max];
    for (int i = 0; i < max; i++) {
        for (int j = 0; j < max; j++) {
            matrix[i][j] = 0;
        }
    }

    temp = g;
    while (temp) {
        Node *node = temp->components;
        while (node) {
            matrix[temp->fromVertex - 1][node->toVertex - 1] = node->weight;
            node = node->next;
        }
        temp = temp->down;
    }

    for (int i = 0; i < max; i++) {
        printf("%d : ", i + 1);
        for (int j = 0; j < max; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    Graph *g = NULL;
    int input;
    do {
        printf("1.Insert,\n2.Print Adjacency list\n3.Print Adjacency Matrix\n-1.Exit");
        printf("\nEnter the input : ");
        scanf("%d", &input);
        int from, to, weight;
        switch (input) {
            case 1:
                printf("\nEnter the from vertex : ");
                scanf("%d", &from);
                printf("\nEnter the to vertex : ");
                scanf("%d", &to);
                printf("\nEnter the weight : ");
                scanf("%d", &weight);
                connect(&g, from, to, weight);
                break;
            case 2:
                printf("Adjacency list\n");
                displayList(g);
                break;
            case 3:
                printf("Adjacency matrix\n");
                displayMatrix(g);
                break;
            case -1:
                input = -1;
                break;
            default:
                input = -1;
                break;
        }
    } while (input != -1);
    return 0;
}
