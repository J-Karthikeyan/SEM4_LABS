#include<stdio.h>
#include<stdlib.h>

typedef struct TreeNode{
	int data;
	struct TreeNode *left, *right;
}TreeNode;

TreeNode * createNode(int item){
	TreeNode * temp = (TreeNode *)malloc(sizeof(TreeNode));
	temp->data = item;
	temp->left = temp->right = NULL;
}

void insert(TreeNode ** root, int item){
    if( (*root)== NULL){
        *root = createNode(item);
    }else{
        if(item < (*root)->data)
            insert((&(*root)->left) , item);
        else if(item > (*root)->data)
            insert(&((*root)->right) , item);
        else{
            printf("key found (%d)\n",item);
            return;
        }
    }
}

void inorder(TreeNode * root){
    if((root) != NULL){
        inorder(root->left);
        printf("%d ",root->data);
        inorder(root->right);
    }
}

void preorder(TreeNode * root){
    if((root) != NULL){
        printf("%d ",root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void postorder(TreeNode * root){
    if((root) != NULL){
        postorder(root->left);
        postorder(root->right);
        printf("%d ",root->data);
    }
}

int main(){
    int input;
    TreeNode * root = NULL;
    do{
        scanf("%d",&input);
        if(input!=-1) insert(&root, input);
    }while(input!=-1);

    printf("\ninorder :"); inorder(root);
    printf("\npreorder : "); preorder(root);
    printf("\npostorder : "); postorder(root);
}
