import os
import datetime
import shutil
import pathlib
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
downloads_directory = config["PATHS"]["downloads_directory"]
document_directory = config["PATHS"]["document_directory"]
images_video_directory = config["PATHS"]["images_video_directory"]
software_directory = config["PATHS"]["software_directory"]
other_directory = config["PATHS"]["other_directory"]
days_old = int(config["FILTER"]["days_old"])
document_extensions = config["EXTENSIONS"]["document_extensions"].split(",")
images_video_extensions = config["EXTENSIONS"]["images_video_extensions"].split(",")
software_extensions = config["EXTENSIONS"]["software_extensions"].split(",")

datetime_threehold = datetime.datetime.now() - datetime.timedelta(days=days_old)
all_files = os.listdir(downloads_directory)

for file in all_files:
    file_path = os.path.join(downloads_directory, file)
    creation_datetime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    if creation_datetime <= datetime_threehold:
        file_ext = pathlib.Path(file_path).suffix
        if file_ext in document_extensions:
            new_file_path = os.path.join(document_directory, file)
            shutil.move(file_path, new_file_path)
        elif file_ext in images_video_extensions:
            new_file_path = os.path.join(images_video_directory, file)
            shutil.move(file_path, new_file_path)
        elif file_ext in software_extensions:
            new_file_path = os.path.join(software_directory, file)
            shutil.move(file_path, new_file_path)
        else:
            new_file_path = os.path.join(other_directory, file)
            shutil.move(file_path, new_file_path)
