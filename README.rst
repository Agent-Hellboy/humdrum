**humdrum**
===========

::

      This a CLI tool for youtube data v3 API
      
      

**Installation**
----------------

Install with pip:

::

      pip install humdrum

Or from git:

::

    git clone https://github.com/princekrroshan01/humdrum/
    cd humdrum
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
      
**General Info**

::

    Why Two option to download

    if you install using pip than it create a binary/executable in /usr/bin folder.
    You could locate it using locate command line utility of unix/linux.
    if You want to avoid this clone the repo and create an alias.

**Prerequisites**
-----------------

Get the youtube data v3 api key from
(https://console.developers.google.com/apis/) and set a environment
variable with the name API\_KEY Reference for setting environment
variable in linux
(https://www.redhat.com/sysadmin/linux-environment-variables) and for
windows
(https://docs.oracle.com/en/database/oracle/r-enterprise/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0)

 Make a python alias by typing

::

 alias humdrum="python3 (location of file cli.py)" in terminal

 No need to create alias if you download this package using pip

**using**
---------

Type ``humdrum --help`` in terminal This will guide you through the
process

::

    humdrum --help
    Usage: humdrum [OPTIONS]

    Options:
       --count INTEGER  enter the number of video you are looking for.
       --title TEXT     enter the title name of video you are looking for
       --order TEXT     to sort the video by date rating viewCount
       --type TEXT      to search for type of video like channel video playlist
       --help           Show this message and exit.

**Contributing**
----------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
