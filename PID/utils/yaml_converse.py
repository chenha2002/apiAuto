import os
import yaml

def generate_custom_yaml(file_name, custom_name):
    # 尝试读取现有的 YAML 文件（如果存在）
    existing_data = []
    file_path = os.path.join(get_test_data_path(), file_name)
    if os.path.exists(file_path):
        with open(file_path, mode="r", encoding="utf-8") as f:
            try:
                existing_data = yaml.safe_load(f) or []  # safe_load 返回 None 时使用空列表
            except yaml.YAMLError as exc:
                print(f"错误：无法解析现有的 YAML 文件 {file_path}. 错误信息: {exc}")
                return

    # 构建新的 YAML 内容
    new_entry = {
        'name': custom_name,
        "request": {
            "headers": {"content-type": "application/json"},
            "json": {"operationName":"launchArticlesToStoresTaskCreate","variables":{"launchPlanIds":["66f42329588be40008401d7e"],"launchStores":["REDFS"]},"query":"mutation launchArticlesToStoresTaskCreate($launchPlanIds: [String!]!, $launchStores: [AdidasStore!]) {\n  launchArticlesToStoresTaskCreate(launchPlanIds: $launchPlanIds, launchStores: $launchStores) {\n    id\n    __typename\n  }\n}\n"}

        }
    }

    # 将新内容追加到现有数据中
    updated_data = existing_data + [new_entry]

    # 将更新后的 YAML 内容写入文件
    try:
        with open(file_path, mode="w", encoding="utf-8") as f:
            yaml.dump(updated_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    except Exception as e:
        print(f"写入 YAML 文件时发生错误: {e}")

def get_test_data_path():
    utils_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(utils_dir)
    test_data_path = os.path.join(parent_dir, "test_data")
    os.makedirs(test_data_path, exist_ok=True)
    return test_data_path

# 用户输入文件名（不带扩展名）
file_name_input = input("请输入YAML文件的名称（不带扩展名）: ")

# 用户输入'name'字段的值
name_value_input = input("请输入YAML文件中'name'字段的值: ")

# 生成YAML文件
generate_custom_yaml(f"{file_name_input}.yaml", name_value_input)

print(f"YAML文件 '{file_name_input}.yaml' 已成功生成或追加！")