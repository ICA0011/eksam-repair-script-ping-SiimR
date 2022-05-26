import socket
from urllib.parse import urlparse


class WebUtil:
    @staticmethod
    def is_web_page_accessible(url):
        url = urlparse(url).hostname
        try:
            socket.gethostbyname(url)
            return True
        except:
            return False
