import os

import yaml


def generate_custom_yaml(file_name, custom_name):
    # 构建YAML内容
    yaml_data = [
        {
            'name': custom_name,  # 使用用户输入的自定义值
            "request": {
                "headers":{"content-type":"application/json"},
                "json": {"operationName":"deleteCartGql","variables":{"input":{"lineIds":["1885912227529523209"]}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"3e33c187b5e91418c141cf677b88f693e5a6e39d7179df61e1fad88042917b53"}}}

            }
        }
    ]

    # 将YAML内容写入文件
    try:
        utils_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(utils_dir)
        test_data_path = os.path.join(parent_dir, "test_data")
        os.makedirs(test_data_path, exist_ok=True)
        file_path = os.path.join(test_data_path, file_name)

        with open(file_path, mode="w", encoding="utf-8") as f:
            yaml.dump(yaml_data, f, allow_unicode=True)
    except Exception as e:
        print(f"写入 YAML 文件时发生错误: {e}")


file_name_input = input("请输入YAML文件的名称（不带扩展名）: ")
name_value_input = input("请输入YAML文件中'name'字段的值: ")
generate_custom_yaml(f"{file_name_input}.yaml", name_value_input)
print(f"YAML文件 '{file_name_input}.yaml' 已成功生成！")