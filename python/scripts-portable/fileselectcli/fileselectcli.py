import os
import getch


def clear_screen():
    # windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def draw_banner(current_dir):
    print("Please select a file or folder from")
    print(current_dir)


def get_folder_contents(current_dir, path_sel):
    dir_contents_unordered = os.listdir(current_dir)

    # sorting contents (first by folder, file then alphabetically)
    tmp_folder_arr = []
    tmp_file_arr = []
    for path in dir_contents_unordered:
        if (os.path.isdir(current_dir + '/' + path)):
            tmp_folder_arr.append(path)
        else:
            tmp_file_arr.append(path)
    tmp_folder_arr.sort()
    tmp_file_arr.sort()
    dir_contents = tmp_folder_arr + tmp_file_arr

    return dir_contents


def disp_folder_contents(contents, path_sel):
    print("===========================================>")
    for i in range(len(contents)):
        if (i == path_sel):
            print("{} *".format(contents[i]))
        else:
            print("{}".format(contents[i]))
    print("===========================================>")


def disp_actions():
    print("'j' to move up, 'k' to move down. 'l' to move into a directory, 'h' to move up a directory.")


def select_fileorfolder(current_dir, dir_contents, pathnum, forcesel=False):
    new_dir = current_dir + "/" + dir_contents[pathnum]
    if (os.path.isdir(new_dir) or forcesel):
        return new_dir
    else:
        return current_dir


def change_dir_up(current_dir):
    new_dir = current_dir[0:current_dir.rfind("/")]
    if (os.path.isdir(new_dir)):
        return new_dir
    else:
        return current_dir


def get_path(start_dir):
    current_dir = start_dir
    pathnum = 0
    while True:
        clear_screen()
        draw_banner(current_dir)
        contents = get_folder_contents(current_dir, pathnum)
        disp_folder_contents(contents, pathnum)
        disp_actions()

        print("Please enter a command: ")
        cmd = getch.getch()
        if ('k' in cmd):
            if (pathnum > 0):
                pathnum -= 1
        elif ('j' in cmd):
            if (pathnum < len(contents)):
                pathnum += 1
        elif ('l' in cmd):
            current_dir = select_fileorfolder(current_dir, contents, pathnum)
            pathnum = 0
        elif ('h' in cmd):
            current_dir = change_dir_up(current_dir)
        elif ('\n' in cmd):
            clear_screen()
            return (select_fileorfolder(current_dir, contents, pathnum, forcesel=True))
