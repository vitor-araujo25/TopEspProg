#include<stdio.h>

#define MAX 9

bool check(int table[][MAX]){
	bool repeat[9]={false};
	int row,col,i;
	
	for(row=0;row<MAX;row++){
		for(i=0;i<MAX;i++)
        {
            repeat[i]=false;
        }
		for(col=0;col<MAX;col++)
        {
            if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
        }
	}
	
	for(col=0;col<MAX;col++){
		for(i=0;i<MAX;i++)
			repeat[i]=false;
		for(row=0;row<MAX;row++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	}
	
	for(i=0;i<MAX;i++)
		repeat[i]=false;
	for(row=0;row<3;row++)
		for(col=0;col<3;col++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	
	for(i=0;i<MAX;i++)
		repeat[i]=false;
	for(row=0;row<3;row++)
		for(col=3;col<6;col++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	
	for(i=0;i<MAX;i++)
		repeat[i]=false;
	for(row=0;row<3;row++)
		for(col=6;col<9;col++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	
	for(i=0;i<MAX;i++)
		repeat[i]=false;
	for(row=3;row<6;row++)
		for(col=0;col<3;col++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	
	for(i=0;i<MAX;i++)
		repeat[i]=false;
	for(row=3;row<6;row++)
		for(col=3;col<6;col++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	
	for(i=0;i<MAX;i++)
		repeat[i]=false;
	for(row=3;row<6;row++)
		for(col=6;col<9;col++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	
	for(i=0;i<MAX;i++)
		repeat[i]=false;
	for(row=6;row<9;row++)
		for(col=0;col<3;col++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	
	for(i=0;i<MAX;i++)
		repeat[i]=false;
	for(row=6;row<9;row++)
		for(col=3;col<6;col++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	
	for(i=0;i<MAX;i++)
		repeat[i]=false;
	for(row=6;row<9;row++)
		for(col=6;col<9;col++)
			if(table[row][col]!=0)
				if(!repeat[table[row][col]-1])
					repeat[table[row][col]-1]=true;
				else
					return false;
	return true;
}

void DFS(int table[][MAX],int row,int col,int *count){
	if(*count<2){
		if(col>=MAX)
			row++,col=0;
		if(row>=MAX){
			if(check(table))
				(*count)++;
		}
		else if(table[row][col]==0){
			bool repeat[9]={false};
			for(int i=0;i<MAX;i++)
				if(table[row][i]!=0)
					repeat[table[row][i]-1]=true;
			for(int i=0;i<MAX;i++)
				if(table[i][col]!=0)
					repeat[table[i][col]-1]=true;
			for(int i=1;i<=9;i++){
				table[row][col]=i;
				if(!repeat[i-1]&&check(table))
					DFS(table,row,col+1,count);
				table[row][col]=0;
			}		
		}
		else
			DFS(table,row,col+1,count);
	}
}

int main(){
	int count=1;
	int table[MAX][MAX];
	while(scanf("%d",&table[0][0])==1){
		int i,j;
		for(i=0;i<MAX;i++)
			for(j=0;j<MAX;j++)
				if(i!=0||j!=0)
					scanf("%d",&table[i][j]);
		if(!check(table))
			printf("Case %d: Illegal.\n",count++);
		else{
			int result=0;
			DFS(table,0,0,&result);
			if(result==0)
				printf("Case %d: Impossible.\n",count++);
			else if(result==1)
				printf("Case %d: Unique.\n",count++);
			else
				printf("Case %d: Ambiguous.\n",count++);
		}
	}
	return 0;
}