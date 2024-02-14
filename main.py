
import logging
import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread


parser = argparse.ArgumentParser(description="sorting folder")
parser.add_argument(name_or_flags = "--source", "-s", help="source folfer", required=True)
parser.add_argument(name_or_flags = "--output", "-o", help="output folfer", default="dist")

print(parser.parse_args())
args = vars(parser.parse_args())
print(args)

source = Path(args.get("source"))
output = Path(args.get("output"))

folders = []

def grabs_folder(path:Path)-> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)



def cjpy_file(path:Path)-> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output/ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder/el.name)
            except OSError as err:
                logging.error(err)
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s  %(message)s')

    folders.append(source)
    grabs_folder(source)

    print(folders)

    threads = []
    for folder in folders:
        th = Thread(target = copyfile, args=(folder, ))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print(f"можна видаляти {source}")
