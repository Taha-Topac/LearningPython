#include <stdlib.h>
#include <stdio.h>
n=0 
s=0
do
    print("Koklu sayiyi girin : ")
    scanf("%d", &n)
 
    for(s=30; s>0; s--):
   
        if(n%(s*s)==0):
        
            if(s*s==n):
            
                printf("%d", s)
                break
            
            else:
               
                print("%d/%d", s, (n/(s*s)))
                break
            
        
        
print("\n\n\n")
while(n!=-1) 
 
return 0
