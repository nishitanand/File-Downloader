#!/usr/bin/env python
# coding: utf-8

# ## Welcome to Nishit's Downloader



# https://file-examples.com/wp-content/uploads/2017/08/file_example_PPT_1MB.ppt
# https://youtu.be/TfYeJZeCCjk
# http://graph.facebook.com/4/picture?type=large
# https://www.hq.nasa.gov/alsj/a17/A17_FlightPlan.pdf
# http://www.africau.edu/images/default/sample.pdf
# https://support.spatialkey.com/spatialkey-sample-csv-data/
# https://easychair.org/publications/easychair.docx
# https://support.oneskyapp.com/hc/en-us/articles/208047697-JSON-sample-files


from tqdm import tqdm
import time
import math
import requests
import mimetypes
i=1
rep="y"
while rep=="y":
    url=str(input("Enter url of the thing to be downloaded "))
    r=requests.get(url,stream=True)
    extn=mimetypes.guess_extension(r.headers["Content-Type"])
    # print(extn)
    if extn != None:
        size=int(r.headers["Content-Length"])
        my_chunk_kaa_size=1024
        no_of_iterations=math.ceil(size/my_chunk_kaa_size)
        with open("PyDownloads/file{}".format(i)+str(extn),"wb") as file: # Write binary file mode
            for chunk in tqdm(r.iter_content(chunk_size=my_chunk_kaa_size),total=no_of_iterations):
                file.write(chunk)
    else:
        print("Either URL is wrong or some other error as from mimetypes, the returned value is None and not an extension")
    i+=1
    rep=input("Do you want to download another file? Type y/n ")






