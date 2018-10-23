from multiprocessing import Pool
import os

def copyTask(dir_name, new_dir_name, file_name):
    "拷贝文件函数"
    fr = open(dir_name + '/' + file_name, mode='rb') # 读取文件句柄
    fw = open(new_dir_name + '/' + file_name, mode='wb')  # 写入文件句柄
    content = fr.read()
    fw.write(content)
    # print('拷贝开始')
    fr.close()
    fw.close()

def main():
    "主函数"
    # 接收用户输入的文件夹名称
    dir_name = input('请输入文件夹名称>>>: ')
    file_names = os.listdir(dir_name) # 拿到文件夹内的全部文件名称
    new_dir_name = dir_name + '-back'
    os.mkdir(new_dir_name)
    pool = Pool(10) # 开启10个进程
    for file_name in file_names:
        pool.apply_async(copyTask, args=(dir_name, new_dir_name, file_name))

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()