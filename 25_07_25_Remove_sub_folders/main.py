#1.Добавление элементов пути каждого фолдера в список (split("/")) - all_folders
#2.Создание пустого фолдера для хранения финальных фолдеров - result_folders
#3.Запуск итерирования по all_folders
#3.1.Если конечный список пустой, то добавляем первый фолдер в result_folders
#4.Запуск итерирования по result_folders
#4.1.Инициализация folder_is_subfolder = False (для выхода из циклов)
#5.Запуск итерирования по folder через enumerate (idx, sub_folder)
#5.1.Если folder_is_subfolder is True, то break
#5.2.Если idx > len(result_folder-1), то folder_is_subfolder = True и break (folder - сабфолдер)
#5.3.Если idx < len(result_folder-1) and idx == len(folder-1),
# то result_folders.remove(result_folder) и break (result_folder - сабфолдер,
# но могут быть и другие сабфолдеры текущего potential_folder)
#5.3.Если idx < len(result_folder-1) and idx < len(folder-1), то:
#5.3.1.Если folder[idx] == result_folder[idx], то continue (переход к следующему элементу для сравнения)
#5.3.2.Если folder[idx] != result_folder[idx], то break (ни один из фолдеров не является сабфолдером другого)
#6.Если folder_is_subfolder is False, то добавление folder в result_folders
#7.Возврат к исходному формату с "/".


def delete_subfolders(all_folders_raw):
    all_folders = [folder[1:].split("/") for folder in all_folders_raw]
    result_folders = []
    for folder in all_folders:
        if len(result_folders) == 0:
            result_folders.append(folder)
        else:
            folder_is_subfolder = False
            for result_folder in result_folders:
                if folder_is_subfolder is True:
                    break
                else:
                    for idx, sub_folder in enumerate(folder):
                        if idx > len(result_folder)-1:
                            folder_is_subfolder = True
                            break
                        elif idx < len(result_folder)-1 and idx == len(folder)-1:
                            result_folders.remove(result_folder)
                            break
                        elif (idx == len(result_folder)-1 and idx == len(folder)-1) or (idx <= len(result_folder)-1 and idx < len(folder)-1):
                            if sub_folder == result_folder[idx]:
                                continue
                            else:
                                break
            if folder_is_subfolder is False:
                result_folders.append(folder)
    return list(map(lambda x: "/"+"/".join(x), result_folders))


# input = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
input = ["/a/b/c","/a/b/ca","/a/b/d"]
output = delete_subfolders(input)
pass
# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]