import os
import requests
from zipfile import ZipFile
from pathlib import Path

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def main():

    # checking if downloads folder exists & creating it if not
    if not os.path.exists(r'C:\Users\quinn\OneDrive\Documents\GitHub\data-engineering-practice\Exercises\Exercise-1\downloads'):
        os.makedirs(r'C:\Users\quinn\OneDrive\Documents\GitHub\data-engineering-practice\Exercises\Exercise-1\downloads')
    else:
        print("Folder exists already")

    # download zip files
    def download_files(download_uris, save_location='downloads'):        # create function to make get request to urls

        for url in download_uris:                                   # for each url in the list
           r = requests.get(url)                                    # make get request
           file_name = os.path.basename(url)                        # file name is the tail end of the url
           save_path = os.path.join(save_location, file_name)       # path is 'downloads' in this current directory
           print(f"Status code of {r.url}: {r.status_code}")        # tell me the status

           if r.status_code == 200:
               with open(save_path, 'wb') as file:
                   file.write(r.content)
           else:
               print(f"Skipping download of {url}: HTTP {r.status_code})")

    download_files(download_uris)


    def unzip_files(zip_directory, output_directory):
        current_zip_path = Path(zip_directory)                      # determine where zip files are
        output_path = Path(output_directory)                        # determine where the extracted files go
        output_path.mkdir(parents=True, exist_ok=True)              # create it if it doesn't already exist

        for f in current_zip_path.glob('*.zip'):                    # for each file in the directory
            try:
                with ZipFile(f, 'r') as archive:
                    archive.extractall(path=output_path)            # extract
                    print(f"Extracted contents from '{f.name}' to '{output_path}'")
                f.unlink()
            except Exception as e:
                print(f"Failed to extract {f.name}: {e}")

    unzip_files('downloads', './extracted_files')

if __name__ == "__main__":
    main()

