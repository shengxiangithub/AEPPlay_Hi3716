# ecoding=utf-8
import os


def get_last_version():
    dirs = os.listdir("./")
    dirs_real = []
    if dirs is not None and len(dirs) > 0:
        for dir_x in dirs:
            if os.path.isdir(dir_x):
                try:
                    int_dir = int(dir_x)
                    if int_dir >= 100:
                        dirs_real.append(int_dir)
                except Exception as e:
                    print(str(e))
    if dirs_real is not None and len(dirs_real) > 0:
        dirs_real.sort()
        dirs_real = dirs_real[::-1]
        for i in range(len(dirs_real)):
            dir_i = dirs_real[i]
            path = os.path.join(os.getcwd(), str(dir_i))
            path = os.path.join(path, "Main.py")
            #print(str(path))
            if os.path.isfile(path):
                cmd = "PYTHONIOENCODING=utf-8 python3.5 " + str(path)
                #print(cmd)
                os.system(cmd)
            else:
                print("未找到Main")
        os.system("reboot")


if __name__ == '__main__':
    get_last_version()
