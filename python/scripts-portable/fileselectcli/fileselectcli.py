import os

def clear_screen():
    # windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def draw_banner( current_dir ):
    print ("Please select a file or folder from")
    print( current_dir )

def disp_folder_contents( current_dir ):
    print ("=============================================================>" )
    dir_contents = os.listdir( current_dir )

    for i in range(len(dir_contents)):
        print("{}. {}".format(i,dir_contents[i]))
    print ("=============================================================>" )
    return dir_contents

def disp_actions ():
    print ("'u' to move up a directory, 'i' to move into a directory. 's' to select a file or folder.")

def select_fileorfolder ( current_dir, folder_arr ):
    folder_index = int(input("Select a folder: "))
    return current_dir + "/" + folder_arr[folder_index]

def change_dir_up ( current_dir ):
    return current_dir[0:current_dir.rfind("/")]

def get_path( start_dir ):
    current_dir = start_dir
    while True:
        clear_screen()
        draw_banner(current_dir)
        contents = disp_folder_contents(current_dir)
        disp_actions()

        cmd = input("Enter an action: ").lower()
        if ( 'i' in cmd ):
            current_dir = change_dir_in(current_dir, contents)
        if ( 'u' in cmd ): 
            current_dir = change_dir_up(current_dir)            
        if ( 's' in cmd ):
            out = select_fileorfolder(current_dir, contents)
            clear_screen()
            return out

