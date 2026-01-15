import zipfile
import pathlib

def make_archive(filepaths, destdir):
    dest_path = pathlib.Path(destdir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as zip_file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zip_file.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["bonus16.py"], destdir="dest")