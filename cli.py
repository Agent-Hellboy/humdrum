import click
import webbrowser
from apiclient.discovery import build
from helper import API



list=[]

@click.command()
@click.option('--count', default=5, help='enter the number of video you are looking for.')
@click.option('--title',prompt='title of the video',help='enter the title name of video you are looking for')       
def titles(count,title):
	obj=API(title,count)
	l=obj.get_titles()
	for j,i in enumerate(l):
		click.echo('{0} > title {1}'.format(j,i))
	open_link(obj)


def fcall(i,obj):
	switcher={
         0:obj.get_descriptions(),
         1:obj.open_id(2)
         }      
	return switcher.get(i,"invalid option")

def ffcall(i,obj):
	if(i==0):
		l=obj.get_descriptions()
		print(l)
	if(i==1):
		obj.open_id(1)

def open_link(obj):
	while(1):
		print("0. get video description\n1. open video url")
		l=int(input())
		ffcall(l,obj)
		

				
		
		
		
		



	
	
	
		

	
	
	
	

	
if __name__ == '__main__':
    titles()
