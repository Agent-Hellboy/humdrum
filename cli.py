import click
import webbrowser
from apiclient.discovery import build
from helper import API



@click.command()
@click.option('--count', default=5, help='enter the number of video you are looking for.')
@click.option('--title',prompt='title of the video',help='enter the title name of video you are looking for')     
@click.option('--order',help='to sort the video by date rating viewCount') 
@click.option('--type',help='to search for type of video like channel video playlist')
def titles(count,title,order,type):
	obj=API(title,count,order,type)
	l=obj.get_titles()
	for j,i in enumerate(l):
		click.echo('{0} > title {1}'.format(j,i))
	vid=value = click.prompt('type id for more', type=int)
	open_link(obj,vid)


def ffcall(i,obj,vid):
	if(i==0):
		l=obj.get_descriptions()
		print(l[vid])
	if(i==1):
		obj.open_id(vid)
		

def open_link(obj,vid):
	while(1):
		print("0. get video description\n1. open video url")
		l=int(input())
		ffcall(l,obj,vid)
		

	
if __name__ == '__main__':
    titles()
