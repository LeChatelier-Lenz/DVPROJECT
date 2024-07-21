import os
import shutil

def move_files(source_folder, csv_folder, json_folder):
    """将CSV和JSON文件分别移动到指定文件夹"""
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)
    if not os.path.exists(json_folder):
        os.makedirs(json_folder)
    
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        
        if filename.endswith('.csv'):
            dest_path = os.path.join(csv_folder, filename)
            shutil.move(source_path, dest_path)
            print(f'Moved {filename} to {csv_folder}')
        
        elif filename.endswith('.json'):
            dest_path = os.path.join(json_folder, filename)
            shutil.move(source_path, dest_path)
            print(f'Moved {filename} to {json_folder}')

if __name__ == "__main__":
    source_folder = "D:/Exp2OutputCSV"  # 修改为你的源文件夹路径
    csv_folder = "D:/csvFolder"        # 修改为CSV文件夹路径
    json_folder = "D:/jsonFolder"      # 修改为JSON文件夹路径
    
    move_files(source_folder, csv_folder, json_folder)
