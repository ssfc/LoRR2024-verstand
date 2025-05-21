"""
Prompt:

已知random_32_32_20.tasks的内容是：
# version for LoRR 2024
100000
627,871
802,623
783,962
340,251
277,1009
764,513
344,686
...
100000是下面有100000行的意思。我省略没有写全。

编写python代码，在每行的两个数字后再添加一个数字。要求添加的这个数字不能和本行的前两个数字相同，同时这个数字还必须在其他行出现过。

"""
import random
import argparse
import os


def modify_tasks_file(input_file):
    # 获取输入文件所在的目录
    input_dir = os.path.dirname(os.path.abspath(input_file))
    input_filename = os.path.basename(input_file)  # 获取输入文件的文件名部分
    filename_without_ext, ext = os.path.splitext(input_filename)  # 分离文件名和扩展名

    # 根据输入文件名动态生成输出文件名
    output_file = os.path.join(input_dir, f"{filename_without_ext}_4_errands{ext}")  # 新的输出文件路径

    with open(input_file, 'r') as file:
        lines = file.readlines()

    # 从第一行获得数量信息，跳过文件头部信息
    num_lines = int(lines[1].strip())
    data_lines = [line.strip() for line in lines[2:2 + num_lines]]

    # 解析数据行并存储所有出现的数字
    all_numbers = set()
    parsed_lines = []
    for line in data_lines:
        num1, num2 = map(int, line.split(','))
        parsed_lines.append((num1, num2))
        all_numbers.update([num1, num2])

    # 为每行添加2个符合条件的数字
    count = 0
    modified_lines = []
    for num1, num2 in parsed_lines:
        count += 1
        if count % 400 == 0:
            print(count)

        # 从所有数字中去掉本行的两个数字，确保它们是可选的
        valid_numbers = list(all_numbers - {num1, num2})
        if len(valid_numbers) < 2:
            raise ValueError("无法找到至少两个符合条件的数字")

        # 随机选择两个不同的有效数字
        num3 = random.choice(valid_numbers)
        valid_numbers.remove(num3)  # 确保第二个数字与第一个不同
        num4 = random.choice(valid_numbers)

        modified_lines.append(f"{num1},{num2},{num3},{num4}")

    # 写入到新的文件中
    with open(output_file, 'w') as file:
        file.write(lines[0])  # 写入第一行的注释行
        file.write(lines[1])  # 写入第二行的数量信息
        file.write("\n".join(modified_lines) + "\n")  # 写入修改后的数据

    print(f"修改后的文件已保存至: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Process a .tasks file and add two additional numbers.")
    parser.add_argument("input_file", help="Path to the input .tasks file")
    args = parser.parse_args()

    modify_tasks_file(args.input_file)


if __name__ == "__main__":
    main()
