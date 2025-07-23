#Получение списка файлов/папок из фолдера Downloads
#Сортировка файлов по дате добавления - системным аргументом передать 3 дня, 7 дней или месяц (дефолт 7 дней)
#Группировка отсортированных файлов по формату - documents, images, software, other
#Трансфер групп файлов по соответствующим фолдерам
#Отчет о проделанной работе в телеграм

import os
import sys
import datetime
import shutil
import pathlib

downloads_dir = "/Users/kirylvialichka/Downloads"
document_extensions = ".doc, .docx, .pdf, .txt, .odt, .rtf, .xls, .xlsx, .ppt, .pptx, .csv, .tex, .epub, .pages, .md, .xml, .json"
document_directory = "/Users/kirylvialichka/DesktopCopy/Documents"
images_video_extensions = ".jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp, .svg, .psd, .heic, .raw, .ico, .jfif, .ai, .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .3gp, .mpeg, .mpg, .m4v"
images_video_directory = "/Users/kirylvialichka/DesktopCopy/PhotosVideos"
software_extensions = ".exe, .msi, .apk, .app, .bat, .sh, .jar, .com, .bin, .cmd, .deb, .rpm, .dmg, .run"
software_directory = "/Users/kirylvialichka/DesktopCopy/Software"
other_directory = "/Users/kirylvialichka/DesktopCopy/Other"
extensions = [document_extensions, images_video_extensions, software_extensions]

if len(sys.argv) > 1:
    try:
        days = int(sys.argv[1])
    except:
        raise ValueError("Please provide a correct number of days to determine 'old' files")
else:
    days = 7

datetime_threehold = datetime.datetime.now() - datetime.timedelta(days=days)

all_files = os.listdir(downloads_dir)

for file in all_files:
    file_moved = False
    file_path = os.path.join(downloads_dir, file)
    creation_datetime = datetime.datetime.fromtimestamp(os.path.bir(file_path))
    if creation_datetime <= datetime_threehold:
        for extension in extensions:
            if file.endswith(extension):
                if extension in document_extensions:
                    new_file_path = os.path.join(document_directory, file)
                    shutil.move(file_path, new_file_path)
                    file_moved = True
                    break
                elif extension in images_video_extensions:
                    new_file_path = os.path.join(images_video_directory, file)
                    shutil.move(file_path, new_file_path)
                    file_moved = True
                    break
                elif extension in software_extensions:
                    new_file_path = os.path.join(software_directory, file)
                    shutil.move(file_path, new_file_path)
                    file_moved = True
                    break
        if file_moved is False:
            new_file_path = os.path.join(other_directory, file)
            shutil.move(file_path, new_file_path)


