# download_file.py
#
# This is a short program  to download the contents
# of a URL from the web and save it into a file on the local hard drive.
# The program doesn't attempt to do anything interesting with the file;
# it saves whatever the web server sends back into the file, without
# regard to what it is, formatting concerns, or anything else; it is
# what it is.


import urllib.error
import urllib.request


def run() -> None:
    url = _choose_url()

    if len(url) == 0:
        return
    else:
        print()
        save_path = _choose_save_path()

        if len(save_path) == 0:
            return
        else:
            _download_url(url, save_path)



def _choose_url() -> str:
    print('Choose a URL to download (press Enter or Return to quit)')
    return input('URL: ').strip()



def _choose_save_path() -> str:
    print('Choose where you\'d like to save the file you download')
    return input('Path: ').strip()



import urllib.request

def _download_url(url_to_download: str, file_path: str) -> None:
    response = None
    file_to_save = None

    try:
        response = urllib.request.urlopen(url_to_download)

        file_to_save = open(file_path, "wb")

        while True:
            chunk = response.read()
            if not chunk:
                break
            file_to_save.write()

    except Exception as e:
        print(f"Error downloading {url_to_download}: {e}")

    finally:
        # Ensure resources are properly closed
        if file_to_save:
            file_to_save.close()
        
        if response:
            response.close()




if __name__ == '__main__':
    run()