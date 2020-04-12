import click
from apiclient.discovery import build

from helper import Api


@click.command()
@click.option(
    "--count", default=5, help="enter the number of video you are looking for."
)
@click.option(
    "--title",
    prompt="title of the video",
    help="enter the title name of video you are looking for",
)
@click.option("--order", help="to sort the video by date rating viewCount")
@click.option("--type", help="to search for type of video like channel video playlist")
def titles(count, title, order, type):
    """
    Function which acts as an interface with API wrapper and CLI
    obj is the instance of the API class having function
    1 open_id
    2 get_titles
    3 get_description
    and more
    """

    obj = Api(title, count, order, type)
    titles = obj.get_titles()
    for j, i in enumerate(titles):
        click.echo("{0} > title {1}".format(j, i))
    vid = click.prompt("type id for more", type=int)
    open_link(obj, vid)


def ffcall(option, obj, vid):
    """
    helper function to choose between 2 function to call i.e. get_description and open_id
    """

    if option == 0:
        des = obj.get_descriptions()  # function to get description of the video
        print(des[vid])
    if option == 1:
        obj.open_id(
            vid
        )  # function to open the video through default browser of the system


def open_link(obj, vid):
    while True:
        print("0. get video description\n1. open video url")
        option = int(input())
        ffcall(option, obj, vid)


if __name__ == "__main__":
    titles()
