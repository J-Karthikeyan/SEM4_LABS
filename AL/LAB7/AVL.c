#include<stdio.h>
#include<stdlib.h>

typedef struct treenode{
    int data, height, bf;
    struct treenode * lchild, * rchild;
}treenode;

treenode * create_node(int item){
    treenode * temp = (treenode *)malloc(sizeof(treenode));
    temp->data = item;
    temp->rchild = temp->lchild = NULL;
    return temp;
}

int max(int a, int b){
    return (a > b) ? a : b;
}

void update_bf(treenode * tree){
    int lh, rh;
    if(tree->lchild)
        lh = tree->lchild->height; 
    else
        lh = -1;

    if(tree->rchild)
        rh = tree->rchild->height;
    else
        rh = -1;
    
    tree->height = max(lh, rh) + 1;
    tree->bf = lh - rh;
}

treenode * R(treenode * X){
    treenode * Y = X->lchild;
    treenode * Yl = Y->lchild;

    Y->rchild = X;
    Y->lchild = Yl;
    update_bf(X);
    update_bf(Y);

    return Y; 
}

treenode * L(treenode * X){
    treenode * Y = X->rchild;
    treenode * Yr = Y->rchild;

    Y->rchild = Yr;
    Y->lchild = X;
    update_bf(X);
    update_bf(Y);

    return Y; 
}

treenode * balance(treenode * tree){
    if(tree->bf < -1){
        if(tree->lchild->bf <= 0)
            return R(tree);
        else{
            tree->lchild = L(tree->lchild);
            return R(tree);
        }
    }
    if(tree->bf > 1){
        if(tree->rchild->bf >= 0)
            return L(tree);
        else{
            tree->rchild = R(tree->rchild);
            return L(tree);
        }
    }

    return tree;
}

treenode * insert(treenode * tree,int item){
    if(!tree)
        return create_node(item);
    
    if(item > tree->data)
        tree->rchild = insert(tree->rchild, item);
    else
        tree->lchild = insert(tree->lchild, item);
    
    update_bf(tree);
    return balance(tree);
}

void inorder(treenode * tree) {
    if (tree) {
        inorder(tree->lchild);
        printf("%d ", tree->data);
        inorder(tree->rchild);
    }
}

int main(){
    treenode * tree = NULL;
    printf("Enter the nodes to be inserted (-1) to stop\n");
    int flag = 1;
    do{
        int inp;
        scanf("%d", &inp);
        if(inp==-1){
            flag=0;
            break;
        }
        insert(tree, inp);
    }while(flag);
    printf("\nInorder: \n");
    inorder(tree);

}
