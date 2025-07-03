import json

import allure
import pytest

from Suhyang.utils.api_client import ApiClient
from Suhyang.utils.yaml_util import YamlUtil


@allure.epic("购物车")
class TestCart:


    @allure.story("加入购物车")
    @pytest.mark.account
    @pytest.mark.visitor
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("add_cart_case.yaml"))
    def test_cart_add(self,case,prepare_headers):
        headers = prepare_headers
        headers.update({"unex-user-token":YamlUtil().read_yaml('token')})
        query =case["request"]["query"]
        variables = case["request"]["variables"]

        req =ApiClient().execute_query(endpoint="cartAddGql",query=query,variables=variables,headers=headers)
        with allure.step("验证购物车添加结果"):
            assert "errors" not in req
            allure.attach(json.dumps(req), name="cartAddGql", attachment_type=allure.attachment_type.JSON)
            print(req)

    @allure.story("获取购物车列表")
    @pytest.mark.account
    @pytest.mark.visitor
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("get_cart_list_case.yaml"))
    def test_get_cart_list(self,case,prepare_headers):
        headers = prepare_headers
        headers.update({"unex-user-token":YamlUtil().read_yaml('token')})
        params = {
            "operationName": case["request"]["params"]["operationName"],
            "variables": json.dumps(case["request"]["params"]["variables"]),
            "extensions": json.dumps(case["request"]["params"]["extensions"])
        }

        req = ApiClient().get(endpoint="cartGql",params=params,headers=headers)
        rep = req.json()
        with allure.step("验证购物车列表结果"):
            assert "errors" not in rep
            allure.attach(body=json.dumps(rep), name="cartGql", attachment_type=allure.attachment_type.JSON)
            print(rep)
        if rep["data"]["cart"]["items"] not in (None, []):
            YamlUtil().write_yaml({"lineId": rep["data"]["cart"]["items"][0]["lineId"]})


    @allure.story("购物车更新商品")
    @pytest.mark.account
    @pytest.mark.visitor
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("update_cart_case.yaml"))
    def test_update_cart(self,prepare_headers,case):
        headers = prepare_headers
        headers.update({"unex-user-token":YamlUtil().read_yaml('token')})
        data = case["request"]["json"]
        data["variables"]["input"]["lineId"] = YamlUtil().read_yaml("lineId")

        req = ApiClient().post(endpoint="updateCartGql",json=data,headers=headers)
        rep = req.json()
        with allure.step("验证购物车更新商品结果"):
            assert "errors" not in rep
            allure.attach(body=json.dumps(rep), name="updateCartGql", attachment_type=allure.attachment_type.JSON)
            print(rep)


    @allure.story("购物车替换商品")
    @pytest.mark.account
    @pytest.mark.visitor
    @pytest.mark.skip(reason="暂时跳过")
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("replace_cart_case.yaml"))
    def test_cart_replace(self,prepare_headers,case):
        headers = prepare_headers
        headers.update({"unex-user-token":YamlUtil().read_yaml('token')})
        data = case["request"]["json"]
        data["variables"]["input"]["fromLineId"] = YamlUtil().read_yaml("lineId")

        req = ApiClient().post(endpoint="cartReplaceGql",json=data,headers=headers)
        rep = req.json()
        with allure.step("验证购物车替换商品结果"):
            assert "errors" not in rep
            allure.attach(body=json.dumps(rep), name="cartReplaceGql", attachment_type=allure.attachment_type.JSON)
            print(rep)


    @allure.story("购物车删除商品")
    @pytest.mark.account
    @pytest.mark.visitor
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("delete_cart_case.yaml"))
    def test_delete_cart(self,prepare_headers,case):
        headers = prepare_headers
        headers.update({"unex-user-token":YamlUtil().read_yaml('token')})
        data = case["request"]["json"]
        data["variables"]["input"]["lineIds"] = YamlUtil().read_yaml("lineId")
        # print(data)

        req = ApiClient().post(endpoint="deleteCartGql",json=data,headers=headers)
        rep = req.json()
        with allure.step("验证购物车删除商品结果"):
            assert "errors" not in rep
            allure.attach(body=json.dumps(rep), name="deleteCartGql", attachment_type=allure.attachment_type.JSON)
            print(rep)














