humdrum
=========
      
      
      this a CLI tool for youtube data api v3
      
      

**Installation**


	Install with pip:


	      pip install humdrum==0.4
	 
	  Or from git:

	    git clone https://github.com/princekrroshan01/humdrum/
	    cd humdrum
	    virtualenv venv
	    source venv/bin/activate
	    pip install -r requirements.txt
	      
      
**Prerequisites**


	Get the youtube data v3 api key from https://console.developers.google.com/apis/ and set a environment variable with the name API_KEY

	</br>
	Make a python alias by typing 
	alias humdrum="python3 (location of file cli.py)" in terminal
	no need to create alias if you download this package using pip

**using** 

	type humdrum --help in terminal 
	this will guide you through the process




		humdrum --help
		Usage: humdrum [OPTIONS]

		Options:
		  --count INTEGER  enter the number of video you are looking for.
		  --title TEXT     enter the title name of video you are looking for
		  --order TEXT     to sort the video by date rating viewCount
		  --type TEXT      to search for type of video like channel video playlist
		  --help           Show this message and exit.




**Contributing**

	Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

