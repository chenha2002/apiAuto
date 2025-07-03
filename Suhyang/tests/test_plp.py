import json

import allure
import pytest
import requests

from Suhyang.utils.api_client import ApiClient
from Suhyang.utils.yaml_util import YamlUtil


@allure.feature("PLP")
class TestPLP:

    @allure.story("搜索商品")
    @pytest.mark.account
    @pytest.mark.visitor
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("plp_search_products_case.yaml"))
    def test_search_products(self,case,prepare_headers):
        headers = prepare_headers
        #print(headers)
        params = {
            "operationName": case["request"]["params"]["operationName"],
            "variables": json.dumps(case["request"]["params"]["variables"]),  # 使用序列化的变量
            "extensions": json.dumps(case["request"]["params"]["extensions"])
        }

        # print(params)
        req = ApiClient().get(endpoint="searchProductsGql",params=params,headers=headers)
        rep = req.json()
        with allure.step("搜索商品"):
           assert "errors" not in rep
           allure.attach(json.dumps(rep), name="searchProductsGql", attachment_type=allure.attachment_type.JSON)
           print(rep)

    @allure.story("预估到手价")
    @pytest.mark.account
    @pytest.mark.visitor
    @pytest.mark.parametrize("case",YamlUtil().read_test_yaml("plp_estimate_price_case.yaml"))
    def test_estimate_price_by_sku(self,case,prepare_headers):
        headrs = prepare_headers
        #print(headers)
        params = {
            "operationName": case["request"]["params"]["operationName"],
            "variables": json.dumps(case["request"]["params"]["variables"]),
            "extensions": json.dumps(case["request"]["params"]["extensions"])

        }
        # print(params)
        req = ApiClient().get(endpoint="estimatePriceBySkuGql",params=params,headers=headrs)
        rep = req.json()
        with allure.step("验证登录结果"):
            assert "errors" not in rep
            allure.attach(json.dumps(rep), name="estimatePriceBySkuGql", attachment_type=allure.attachment_type.JSON)
            print(rep)









