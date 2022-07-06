#2022.7.6 18258 큐 c
#include <stdio.h>
#include <string.h>
int main(void){
    int n;
    int num;
    int front=0, rear=-1;
    int stack[2000001];
    char say[10];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        
        scanf("%s",say);
        if(strcmp(say,"push")==0){
            scanf("%d", &num);
            stack[++rear]=num;
        
        }
        else if(strcmp(say,"pop")==0){
            if(rear-front+1==0){
                printf("-1\n");
            }
            else{
                printf("%d\n", stack[front++]);
            }
            
        }
        else if(strcmp(say,"size")==0){
            printf("%d\n",rear-front+1);
        }
        else if(strcmp(say,"empty")==0){
            if(rear-front+1==0){
                printf("1\n");
            }
            else{
                printf("0\n");
            }
        }
        else if(strcmp(say,"front")==0){
            if(rear-front+1==0){
                printf("-1\n");
            }
            else{
                printf("%d\n",stack[front]);
            }
            
        }
        else if(strcmp(say,"back")==0){
            if(rear-front+1==0){
                printf("-1\n");
            }
            else{
                printf("%d\n",stack[rear]);
            }
            
        }
        for(int i=0;i<10;i++){
            say[i]='\0';
        }
        
    }
    return 0;
}
