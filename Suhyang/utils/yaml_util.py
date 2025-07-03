import os
import yaml

class YamlUtil:
    # 读取yaml文件
    def read_yaml(self, key):
        try:
            utils_dir = os.path.dirname(os.path.abspath(__file__))
            # 定位到上级目录（与utils同级）
            parent_dir = os.path.dirname(utils_dir)
            test_data_path = os.path.join(parent_dir, "test_data")
            file_path = os.path.join(test_data_path, "extract.yml")

            with open(file_path, mode="r", encoding="utf-8") as f:
                values = yaml.safe_load(f)
                return values[key]

        except FileNotFoundError:
            print(f"文件未找到: {file_path} 请检查文件路径")
        except KeyError:
            print(f"键 {key} 未在 YAML 文件中找到")
        except yaml.YAMLError as e:
            print(f"YAML 格式解析错误: {e}")
        except Exception as e:
            print(f"读取 YAML 文件时发生未知错误: {e}")

    # 写入yaml文件
    def write_yaml(self, data):
        try:
            utils_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(utils_dir)
            test_data_path = os.path.join(parent_dir, "test_data")
            os.makedirs(test_data_path, exist_ok=True)
            file_path = os.path.join(test_data_path, "extract.yml")

            existing_data = {}
            if os.path.exists(file_path):
                with open(file_path, mode="r", encoding="utf-8") as f:
                    existing_data = yaml.safe_load(f) or {}
            existing_data.update(data)

            # 写回文件
            with open(file_path, mode="w", encoding="utf-8") as f:
                yaml.safe_dump(existing_data, f, allow_unicode=True, default_flow_style=False)

        except Exception as e:
            print(f"写入 YAML 文件时发生错误: {e}")

    # 读取测试用例的yml文件
    def read_test_yaml(self, yaml_file):
        # 定位 test_data 目录
        test_data_dir = os.path.join(os.path.dirname(__file__), "..", "test_data")
        if not os.path.isdir(test_data_dir):
            print(f"错误：测试数据目录未找到 - {test_data_dir}")
            return None

        file_path = os.path.join(test_data_dir, yaml_file)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"错误：YAML 文件未找到 - {file_path}")
        except yaml.YAMLError as e:
            print(f"YAML 解析错误: {e}")
        except Exception as e:
            print(f"读取 YAML 文件时发生未知错误: {e}")
        return None

# 清除yaml文件
#     def clear_yaml(self):
#         try:
#             utils_dir = os.path.dirname(os.path.abspath(__file__))
#             parent_dir = os.path.dirname(utils_dir)
#             test_data_path = os.path.join(parent_dir, "test_data")
#             os.makedirs(test_data_path, exist_ok=True)
#             file_path = os.path.join(test_data_path, "extract.yml")
#             with open(file_path, mode="a", encoding="utf-8") as f:
#                 f.truncate()
#         except Exception as e:
#             print(f"清除 YAML 文件时发生错误: {e}")


