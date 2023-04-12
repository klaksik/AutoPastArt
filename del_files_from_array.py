import os


def del_files_from_array(array):
    i = 0
    print(array)
    for file in array:
        try:
            os.remove(array[i])
        except:
            print("не получилось удалить, ну и похуй")
        finally:
            print(f"удалил {i} файл из папки")
            i =+ 1
