import json

import allure
import pytest
from PID.utils.yaml_util import YamlUtil
from PID.utils.api_client import ApiClient
from PID.utils.shops_util import ShopsUtil

@allure.epic("商品下发")
class TestArticleIssued:

    @allure.story("修改发布类目和聚合号")
    @pytest.mark.parametrize("case,planned_products_data", [(YamlUtil().read_test_yaml("master_data_lock_case.yaml"),YamlUtil().read_test_yaml("release_planned_products_case.yaml"))])
    def test_master_data_lock(self, case,planned_products_data,prepare_headers):
        headers = prepare_headers
        type_values = ["category", "aggregation_number"]
        # 定义 type_value 和 new_value 的映射关系
        type_value_mapping = {
            "category": planned_products_data[0]["category"],
            "aggregation_number": planned_products_data[0]["aggregation_number"]
        }
        store_name = planned_products_data[0]["request"]["json"]["variables"]["launchStores"]
        store_name_str = store_name[0]


        for type_value in type_values:
            # 从映射关系中获取 new_value
            new_value = type_value_mapping.get(type_value)
            if new_value:
                # 调用 modify_store_categories 方法，动态传入 type_value
                data = ShopsUtil().modify_store_categories(store_name=store_name_str,type_value=type_value,new_value=new_value,article_no="JM5860",case=case)
                req = ApiClient().post(json=data, headers=headers)
                rep = req.json()
                print(rep)
                with allure.step("验证获取主数据列表结果"):
                    assert "error" not in rep
                    allure.attach(json.dumps(rep), name="master_data_list", attachment_type=allure.attachment_type.JSON)

    @allure.story("下放发布计划商品")
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("release_planned_products_case.yaml"))
    def test_release_planned_products(self, prepare_headers,case):
        headers = prepare_headers
        headers.update({"authorization": YamlUtil().read_yaml("token")})
        data = case["request"]["json"]
        req = ApiClient().post(json=data, headers=headers)
        rep = req.json()
        print(rep)
        with allure.step("验证下放发布计划商品结果"):
            assert "error" not in rep
            allure.attach(json.dumps(rep), name="release_planned_products", attachment_type=allure.attachment_type.JSON)





