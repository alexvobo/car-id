import threading
import requests

def download(link, filelocation):
    try:
        r = requests.get(link, stream=True)
        with open(filelocation, 'wb') as f:
            for chunk in r.iter_content(1024):
                if chunk:
                    f.write(chunk)
    except Exception:

        print("Failed to access link: " + link)


def create_new_download_thread(link, filelocation):
    download_thread = threading.Thread(
        target=download, args=(link, filelocation))
    download_thread.start()


def batch_download(file_prefix, links, save_directory):
    for i, link in enumerate(links):
        file = "{}/{}-({}).jpg".format(save_directory, file_prefix, str(i))
        create_new_download_thread(link, file)
