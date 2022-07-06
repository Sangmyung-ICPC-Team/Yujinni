#2022.7.6 10828 스택 c
#include <stdio.h>
#include <string.h>
int main(void){
    int n,cnt=0;
    int num;
    int stack[100001];
    char say[10];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        
        scanf("%s",say);
        if(strcmp(say,"push")==0){
            scanf("%d", &num);
            stack[cnt]=num;
            cnt++;
        }
        else if(strcmp(say,"pop")==0){
            if(cnt==0){
                printf("-1\n");
            }
            else{
                printf("%d\n", stack[cnt-1]);
                stack[cnt-1]=0;
                cnt--;
            }
            
        }
        else if(strcmp(say,"size")==0){
            printf("%d\n",cnt);
        }
        else if(strcmp(say,"empty")==0){
            if(cnt==0){
                printf("1\n");
            }
            else{
                printf("0\n");
            }
        }
        else if(strcmp(say,"top")==0){
            if(cnt==0){
                printf("-1\n");
            }
            else{
                printf("%d\n",stack[cnt-1]);
            }
            
        }
        
        
    }
    return 0;
}
