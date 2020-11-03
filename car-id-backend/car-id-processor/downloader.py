import threading
import requests
import base64
import shutil
import time
from functools import wraps
# def get_as_base64(url):
#     return base64.b64encode(requests.get(url).content)


def download(link, filelocation):
    try:
        time.sleep(1/2)
        with requests.get(link, stream=True) as r:
            with open(filelocation, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
          # for chunk in r.iter_content(None):
          #     if chunk:
          #         f.write(chunk)
    except Exception:
        print("Failed to access link: " + link)


def create_new_download_thread(link, filelocation):
    download_thread = threading.Thread(
        target=download, args=(link, filelocation))
    download_thread.start()


def batch_download(file_prefix, links, save_directory):
    for i, link in enumerate(links):
        file = "{}/{}_{}.jpg".format(save_directory, file_prefix, str(i))
        create_new_download_thread(link, file)
