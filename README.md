Humdrum🕹️
=======

👉A simple command-line tool built on top of the YouTube Data API v3 that lets you search for and explore YouTube videos directly from your terminal.
With Humdrum, you can quickly fetch video📽️ titles, descriptions, channels, publish dates, thumbnails, and detailed statistics like views, likes, comments, and duration — all without opening a browser.😳
It’s lightweight, easy to install, and ideal for developers, researchers, or anyone who wants quick YouTube insights from the command line.

A. Installation and Usage
------------

Install with **pip**:

`pip install humdrum`

Or install from source:

```   
git clone https://github.com/princekrroshan01/humdrum/
cd humdrum
```
* Create a virtual environment:
```
python -m venv venv  
```
* Activate the environment:
```
source venv/bin/activate   (# On Windows use venv\Scripts\activate)
```
```
pip install -r requirements.txt
```

B. General Info
------------
You can install in two ways:

*   **pip install** → Creates a binary/executable in /usr/bin (or equivalent).
    
*   **git clone** → Lets you run the tool directly and optionally create a shell alias.
    

For example:
`   alias humdrum="python3 path/to/cli.py"   `

If installed with pip, you don’t need to set up the alias.

C. Prerequisites
-------------

1.  Get a **`YouTube Data API v3`** key from the [Google Cloud Console](https://console.developers.google.com/apis/).
    
2.  Set it as an environment variable named **`API\_KEY`**.
Reference for setting environment variable in linux [**from here**](https://www.redhat.com/sysadmin/linux-environment-variables) and for windows [**Check here**](https://docs.oracle.com/en/database/oracle/r-enterprise/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0)

**| Linux / macOS:**

`   export API_KEY="YOUR_YOUTUBE_DATA_API_KEY"   `

**| Windows (PowerShell):**

`   setx API_KEY "YOUR_YOUTUBE_DATA_API_KEY"   `

D. Usage
-----

**Check the CLI options:**
```
humdrum --help
```

**Output:**

```   
Usage: humdrum [OPTIONS]  

Options:    
--count INTEGER  enter the number of video you are looking for.    
--title TEXT     enter the title name of video you are looking for    
--order TEXT     to sort the video by date, rating, viewCount    
--type TEXT      to search for type of video (channel, video, playlist)   
--help           Show this message and exit.   
```

Example:
```
humdrum --title "python tutorial" --count 5 --order viewCount
```

Demo
----
![humdrum (1)](https://github.com/user-attachments/assets/ad56916e-8b13-4071-aa93-8d3430af2a83)


E. Contributing
------------

We welcome all contributions! 🎉 Whether it’s a bug fix, new feature, or documentation improvement, your help is appreciated.

*   For **small changes**, feel free to open a pull request directly.
*   For **major changes**, please open an issue first so we can discuss the approach together.
