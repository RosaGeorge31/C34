#include<stdio.h>
void main()
{
char s[100],ch;
printf("Enter the string : \n");
gets(s);
int i =0,ct=0,pos,f=0;
printf("Enter the character to be searched : \n");
scanf("%c",&ch);
while(s[i]!='\0')
{
	if(s[i]==ch)
	{
	f=1;
	ct++;
	}
	if(f==1 && ct==1)
	pos = i+1;
	++i;
}
printf("Position of %c in string : %d\n",ch,pos);
printf("Repeation of %c in string : %d\n",ch,ct);
}

