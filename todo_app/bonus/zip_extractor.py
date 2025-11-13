import pathlib
import zipfile

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive(pathlib.Path("dest", "compressed.zip"), "dest")
