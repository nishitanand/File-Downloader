<h1>File Downloader</h1>

This Program is a File Downloader which can be used to download JPEGs, PNGs, PDFs, Word files, Excel files and Powerpoint files.
It uses mimetypes library to get the file extension and writes the files using file handling. It uses lazy loading method to stream the data in chunks instead of loading it all at the same time, so that the system may not run out of memory. It also uses the tqdm library for showing a live progress bar for the download.

To use it, first write this command in the command line

pip install -r requirements.txt
or (for Mac)
pip3 install -r requirements.txt

and then to run the file write
 
python Nishit-Downloader.py
or (for Mac)
python3 Nishit-Downloader.py

The downloaded files will be saven in the folder named "PyDownloads"
