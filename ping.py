from web_util import WebUtil

def check_server_status(url: str):
    return WebUtil.is_web_page_accessible(url)
