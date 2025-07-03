import json

import pytest
from PID.utils.yaml_util import YamlUtil
from PID.constant.shops_constant import ShopsConstant

class ShopsUtil:

    ShopsConstant = ShopsConstant()

    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("master_data_lock_case.yaml"))
    def modify_store_categories(self, store_name, type_value, new_value, article_no, case):
        # 提取请求数据
        data = case[0]["request"]["json"]

        # 更新数据
        data["variables"]["input"]["id"] = article_no
        data["variables"]["input"]["fieldValues"]["newValue"] = new_value
        # 定义店铺和类型的映射关系
        store_field_mapping = {
            "REDFS": {
                "category": ShopsConstant.REDFS_PUBLISHING_CATEGORY,
                "aggregation_number": ShopsConstant.REDFS_AGGREGATION_NUMBER,
            },
            "JD": {
                "category": ShopsConstant.JDFS_PUBLISHING_CATEGORY,
                "aggregation_number": ShopsConstant.JDFS_AGGREGATION_NUMBER,
            }
        }

        # 根据店铺名称和类型值设置字段
        print(store_name)
        print(store_field_mapping)
        print(store_field_mapping[store_name])
        if store_name in store_field_mapping and type_value in store_field_mapping[store_name]:
            data["variables"]["input"]["fieldValues"]["field"] = store_field_mapping[store_name][type_value]
        return data

    def ensure_dict(self,case):
        if isinstance(case, list):
            # 如果列表中的元素是键值对，直接转换为字典
            case_converted = dict(case)
            print(case_converted)
            return dict(case)
        elif isinstance(case, dict):
            return case
        else:
            raise ValueError(f"Unsupported case type: {type(case)}. Expected list or dict.")

