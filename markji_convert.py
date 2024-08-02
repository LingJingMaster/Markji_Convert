import sys
import re
import os

def format_document(input_file, output_dir, pattern):
    patterns = {
        '1': (r'\*(.*?)\*', '[F##\\1]'),  # *文字*
        '2': (r'\*\*(.*?)\*\*', '[F##\\1]'),  # **文字**
        '3': (r'==(.*?)==', '[F##\\1]'),  # ==文字==
        '4': (r'\*\*\*(.*?)\*\*\*', '[F##\\1]')  # ***文字***
    }
    regex, replace_format = patterns.get(pattern, (r'\*(.*?)\*', '[F##\\1]'))  # 默认为 *文字*

    # 提取文件名和扩展名，然后添加 _markji 后缀
    filename = os.path.basename(input_file)
    base, ext = os.path.splitext(filename)
    output_filename = f"{base}_markji{ext}"
    output_file = os.path.join(output_dir, output_filename)

    # 读取原始文件内容
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 处理每一行，移除以 - 或 > 开头的缩进
    processed_lines = []
    for line in content.splitlines():
        # 移除行首的空格及连字符或引用符号后的空格
        stripped_line = re.sub(r'^\s*[->]\s*', '', line)
        processed_lines.append(stripped_line)

    # 将处理后的行合并为单个字符串
    content = '\n'.join(processed_lines)

    # 替换选择的格式
    formatted_content = re.sub(regex, replace_format, content)

    # 将格式化后的内容写入到新文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(formatted_content)


def main(directory, pattern):
    # 创建输出目录名，保证它位于原目录的同级位置
    output_dir_name = f"{os.path.basename(directory)}_markji"
    base_dir = os.path.dirname(directory)
    output_dir = os.path.join(base_dir, output_dir_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历目录下的所有.md文件
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            input_file = os.path.join(directory, filename)
            format_document(input_file, output_dir, pattern)

    # 使用绝对路径输出
    abs_output_dir = os.path.abspath(output_dir)
    print(f"Markji 格式已输出到 : {abs_output_dir}\n")
    print(f"作者 : Ling_Jing_Master")

    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python markji_convert.py <源文件夹> <替换样式编号>\n")
        print("支持以下样式替换:")
        print("1: *text*")
        print("2: **text**")
        print("3: ==text==")
        print("4: ***text***")
        sys.exit(1)

    directory = sys.argv[1]
    pattern = sys.argv[2]
    main(directory, pattern)