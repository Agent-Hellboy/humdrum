"""
Contains a class Api having implementation of youtube data v3 client.
"""
import os
from typing import Any

import webbrowser
from apiclient.discovery import build


class Api:
    """
    Class which acts as a client to the youtube data v3 API,
    having attributes as the query parameter for API.
    """

    maxlen: Any

    def __init__(self, keyword, maxlen, order="relevance", type="video"):
		try:
        	self.__API_KEY = os.environ.get(
        	    "API_KEY"
        	)  # link to get the api key is in readme file
		except Exception:
			raise TypeError("You must have API_KEY set as an environment variable")        
		youtube = build("youtube", "v3", developerKey=self.__API_KEY)
        self.keyword = keyword
        self.maxlen = maxlen
        self.order = order
        self.type = type
        req = youtube.search().list(
            q=self.keyword,
            part="snippet",
            maxResults=self.maxlen,
            type=self.type,
            order=self.order,
        )
        self.result = req.execute()

    def open_id(self, item_no):
        """"Opens the video in default browser of the system."""
        return webbrowser.open(
            "https://www.youtube.com/watch?v="
            + self.result["items"][item_no]["id"]["videoId"]
        )

    def get_titles(self):
        """"Returns a list with title of the videos."""
        rslt = []
        for i in range(self.maxlen):
            rslt.append(self.result["items"][i]["snippet"]["title"])
        return rslt

    def get_descriptions(self):
        """"Return list with description of the video."""
        rslt = []
        for i in range(self.maxlen):
            rslt.append(self.result["items"][i]["snippet"]["description"])
        return rslt

    def get_image_urls(self):

        """
        Function to get the image url which will be used for retriving the icon image of
        the youtube video.
        """

        rslt = []
        for _ in range(self.maxlen):
            rslt.append(
                self.result["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
            )
        return rslt
