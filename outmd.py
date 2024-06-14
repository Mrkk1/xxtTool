import os
import json
import re

def extract_title(filename):
    # 使用正则表达式匹配书名号之间的内容
    match = re.search(r'《(.*?)》', filename)
    if match:
        return match.group(1)
    else:
        return os.path.splitext(filename)[0]  # 如果没有书名号，使用文件名作为标题

def json_to_md(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    md_content = ""
    
    # 居中显示题目md_content
    md_content += f"## <center>{extract_title(os.path.basename(json_file))}学习通题库</center> \n\n"
    
    for item in data:
        if 'type' in item and 'timu' in item and 'answer' in item:
            md_content += f"### {item['type']} "
            md_content += f"   {item['timu']}\n\n"
            if isinstance(item['answer'], list):
                for answer in item['answer']:
                    md_content += f"- {answer}\n"
            else:
                md_content += f"- {item['answer']}\n"
            md_content += "\n"
    
    return md_content

def convert_all_json_to_md(directory='.'):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            json_path = os.path.join(directory, filename)
            md_content = json_to_md(json_path)
            
            # 格式化Markdown文件名
            title = extract_title(filename)
            md_filename = f"2024-2-{title}学习通题库.md"  # 月份使用两位数表示
            md_path = os.path.join(directory, md_filename)
            
            with open(md_path, 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)
            print(f"Converted {json_path} to {md_path}")

# 调用函数，转换当前目录下所有的.json文件
convert_all_json_to_md('.')