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

        # STEP 1: Get search results (basic snippet data)
        search_req = self.youtube.search().list(
            q=self.keyword,
            part="snippet",
            maxResults=self.maxlen,
            type=self.type,
            order=self.order,
        )
        search_response = search_req.execute()

        # STEP 2: Extract video IDs
        video_ids = [
            item["id"]["videoId"]
            for item in search_response["items"]
            if "videoId" in item["id"]
        ]

        # STEP 3: Get detailed video info (snippet + stats + contentDetails)
        if video_ids:
            details_req = self.youtube.videos().list(
                part="snippet,statistics,contentDetails",
                id=",".join(video_ids),
            )
            details_response = details_req.execute()
            self.result = details_response
        else:
            self.result = {"items": []}

    def open_id(self, item_no):
        """Opens the video in default browser of the system."""
        return webbrowser.open(
            "https://www.youtube.com/watch?v="
            + self.result["items"][item_no]["id"]
        )

    def get_titles(self):
        """Returns a list with titles of the videos."""
        return [item["snippet"]["title"] for item in self.result["items"]]

    def get_descriptions(self):
        """Return list with descriptions of the videos."""
        return [item["snippet"]["description"] for item in self.result["items"]]

    def get_image_urls(self):
        """Returns a list of thumbnail image URLs."""
        return [item["snippet"]["thumbnails"]["medium"]["url"] for item in self.result["items"]]

    # NEW: Get channel names
    def get_channels(self):
        """Returns list of channel titles (uploaders)."""
        return [item["snippet"]["channelTitle"] for item in self.result["items"]]

    # NEW: Get publish dates
    def get_publish_dates(self):
        """Returns list of publishedAt dates."""
        return [item["snippet"]["publishedAt"] for item in self.result["items"]]

    # NEW: Get video statistics (views, likes, comments)
    def get_stats(self):
        """Returns list of dicts with video stats."""
        stats_list = []
        for item in self.result["items"]:
            stats = item.get("statistics", {})
            stats_list.append({
                "views": stats.get("viewCount"),
                "likes": stats.get("likeCount"),
                "comments": stats.get("commentCount"),
            })
        return stats_list

    # NEW: Get video durations
    def get_durations(self):
        """Returns list of video durations (ISO 8601 format)."""
        return [item["contentDetails"]["duration"] for item in self.result["items"]]