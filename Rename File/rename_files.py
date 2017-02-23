import os

def rename_files():
    file_dir = r"C:\Users\Tianyu Xia\Desktop\Python\Rename File\prank"
    file_list = os.listdir(file_dir)
    saved_path = os.getcwd()
    os.chdir(file_dir)

    for file_names in file_list:
        print(file_names)
        print(file_names.translate(None, "0123456789"))
        os.rename(file_names, file_names.translate(None, "0123456789"))

    os.chdir(saved_path)


    # for file_names in file_list:
    #     temp_filename = ""
    #     for file_chars in file_names:
    #         if(!(file_chars.isdigit())):
    #             temp_filename

rename_files()