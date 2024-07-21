import os
import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    """将单个CSV文件转换为JSON文件"""
    data = []
    
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def convert_all_csv_to_json(folder_path):
    """将文件夹中的所有CSV文件转换为JSON文件"""
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(folder_path, filename)
            json_file_name = filename.replace('.csv', '.json')
            json_file_path = os.path.join(folder_path, json_file_name)
            
            csv_to_json(csv_file_path, json_file_path)
            print(f'Converted {filename} to {json_file_name}')

if __name__ == "__main__":
    folder_path = "D:/Exp2OutputCSV"  # 修改为你的文件夹路径
    convert_all_csv_to_json(folder_path)
