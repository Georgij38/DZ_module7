import os
import shutil
import sys


def transliteration(name):  # транс літерація
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f",
        "h",
        "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    name = name.translate(TRANS)
    ind = 0
    for el in name:
        if not el.isalnum():
            name = name.replace(el, '_')

        ind += 1
    return name


def del_empty_dirs(path):  # видаленя пустих папок
    for dir in os.listdir(path):
        path_dir = os.path.join(path, dir)
        if os.path.isdir(path_dir):
            del_empty_dirs(path_dir)
            if not os.listdir(path_dir):
                os.rmdir(path_dir)

def file_recording(root,folder_path,  filename, file_extension): #перенесиня файлу
    first_name = filename + file_extension
    new_file_name = transliteration(filename)  # транс літерація
    new_file_name +=  file_extension
    shutil.move(os.path.join(root, first_name), os.path.join(folder_path, new_file_name))

def creating_folder(path, name_folder):
    new_path_folder = os.path.join(path, name_folder)
    if  not os.path.exists(new_path_folder):
        os.mkdir(new_path_folder)
    return new_path_folder


def sorting_files(path):  # створиня папок


    for root, dirs, files in os.walk(path):  # отреманя списку файлів
        # if root  in (audio, images, video, documents, archives):  # пропуск створиних папок
        #     continue

        for file_name in files:
            filename, file_extension = os.path.splitext(file_name)  # отриманя імя та розширеня файлу
            # сортуваня та зпис файлі

            # audio
            if file_extension in ('.mp3', '.ogg', '.wav' ,'.amr'):
                folder_path = creating_folder(path, 'audio')
                file_recording(root, folder_path, filename, file_extension)

            # images
            elif file_extension in ('.jpeg', '.png', '.jpg', '.svg'):
                folder_path =  creating_folder(path, 'images')
                file_recording(root, folder_path, filename, file_extension)

            # video
            elif file_extension in ('.avi', '.mp4', '.mov', '.mkv'):
                folder_path = creating_folder(path, 'video')
                file_recording(root,folder_path,  filename, file_extension)

            # documents
            elif file_extension in ('.dok', '.docx', '.txt', '.pdf', '.xlsx' ,'.pptx'):
                folder_path = creating_folder(path, 'documents')
                file_recording(root, folder_path, filename, file_extension)

            # archives
            elif file_extension in ('.zip', '.gz', '.tar'):
                filename = transliteration(filename)  # транс літерація

                dir_file_name = os.path.join(archives, filename)
                if not os.path.exists(dir_file_name):
                    os.mkdir(dir_file_name)

                new_file_name = filename + file_extension
                shutil.unpack_archive(os.path.join(root, file_name), dir_file_name)
                shutil.move(os.path.join(root, file_name), os.path.join(dir_file_name, new_file_name))

    del_empty_dirs(path)


def start_sort_file_ext():
    path = input('enter the full path to the folder:  ')
    if path == '0':
            exit()
    else:
        this_is_folder(path)

def  this_is_folder(path):
    if os.path.exists(path):
        sorting_files(path)
    else:
        print ('no such folder exists')
        start_sort_file_ext()


def main():
    if  len(sys.argv) == 2:
        path = sys.argv[1]
        this_is_folder(path)
        print (path)
    else:
        start_sort_file_ext()

root = 'D:\Python уроки\PYTEST'
if __name__ == "__main__":
    sorting_files(root)


