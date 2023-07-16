# 读取名为_posts的文件夹中的子文件夹列表。
# 对于每个子文件夹，检查是否存在名为assets的文件夹。
# 如果存在assets文件夹，将其中的所有图片收集起来。
# 将收集到的图片复制到当前位置下的assets文件夹中。
# 检查每个子文件夹是否存在后缀名为.assets的文件夹。
# 如果存在后缀名为.assets的文件夹，将其中的所有图片收集起来。
# 将收集到的图片复制到当前位置下，保持文件夹名不变。

import os
import shutil

def collect_images_from_assets(src_dir, dest_dir):
    # 检查源文件夹是否存在
    if not os.path.isdir(src_dir):
        return

    # 遍历源文件夹中的文件
    for file in os.listdir(src_dir):
        file_path = os.path.join(src_dir, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest_dir)

def collect_dot_assets(src_dir, dest_dir):
    # 检查源文件夹是否存在
    if not os.path.isdir(src_dir):
        return

    # 遍历源文件夹中的文件夹
    for dir_name in os.listdir(src_dir):
        dir_path = os.path.join(src_dir, dir_name)
        if os.path.isdir(dir_path) and dir_name.endswith('.assets'):
            # 创建目标文件夹并复制文件
            target_dir = os.path.join(dest_dir, dir_name)
            os.makedirs(target_dir, exist_ok=True)
            collect_images_from_assets(dir_path, target_dir)
            collect_dot_assets(dir_path, target_dir)

def collect_images_from_sub_dirs(posts_dir, dest_dir,current_dir):
    # 检查_posts文件夹是否存在
    if not os.path.isdir(posts_dir):
        return

    # 遍历_posts文件夹下的子文件夹
    for root, dirs, _ in os.walk(posts_dir):
        for dir_name in dirs:
            sub_dir_path = os.path.join(root, dir_name)
            assets_dir = os.path.join(sub_dir_path, 'assets')

            # 收集assets文件夹中的图片
            collect_images_from_assets(assets_dir, dest_dir)

            # 收集后缀名为.assets的文件夹中的图片及文件夹
            collect_dot_assets(sub_dir_path, current_dir)

def main():
    # 设置当前位置和_posts文件夹路径
    current_dir = os.getcwd()
    posts_dir = os.path.join(current_dir, '_posts')

    # 设置目标assets文件夹路径
    target_assets_dir = os.path.join(current_dir, 'assets')

    # 检查当前路径下是否存在名为 'assets' 的文件夹，没有则创建
    os.makedirs(target_assets_dir, exist_ok=True)

    # 收集图片和文件夹
    collect_images_from_sub_dirs(posts_dir, target_assets_dir,current_dir)



if __name__ == '__main__':
    main()




