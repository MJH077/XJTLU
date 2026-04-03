import os
def test_os():
    print(os.listdir("E:/XJTLU"))  # 判断路径下的内容
    print(os.path.isdir("E:/XJTLU/简历"))  # 判断指定路径是不是文件夹
    print(os.path.exists("E:/XJTLU1"))  # 判断路径是否存在
test_os()
def get_files(path):
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                get_files(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}不存在")
        return []
    return file_list

