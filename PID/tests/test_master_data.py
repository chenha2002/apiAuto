import json

import allure
import pytest

from PID.utils.yaml_util import YamlUtil
from PID.utils.api_client import ApiClient

@allure.epic("主数据")
class TestMasterData:

    @allure.story("获取店铺列表")
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("get_shops_case.yaml"))
    def test_get_shops(self,case,prepare_headers):
        headers = prepare_headers
        headers.update({"authorization": YamlUtil().read_yaml('token')})
        data =case["request"]["json"]

        req = ApiClient().post(json=data,headers=headers)
        rep = req.json()
        print(rep)
        with allure.step("验证获取店铺列表结果"):
            assert "error" not in rep
            allure.attach(json.dumps(rep), name="shops", attachment_type=allure.attachment_type.JSON)

    @allure.story("获取字段定义")
    @pytest.mark.parametrize("case",YamlUtil().read_test_yaml("get_field_definitions_case.yaml"))
    def test_get_field_definitions(self,prepare_headers,case):
        headers = prepare_headers
        headers.update({"authorization": YamlUtil().read_yaml('token')})
        data = case["request"]["json"]

        req = ApiClient().post(json=data,headers=headers)
        rep = req.json()
        print(rep)
        with allure.step("验证获取字段定义结果"):
            assert "error" not in rep
            allure.attach(json.dumps(rep), name="field_definitions", attachment_type=allure.attachment_type.JSON)

    @allure.story("获取主数据列表")
    @pytest.mark.parametrize("case",YamlUtil().read_test_yaml("get_master_data_list_case.yaml"))
    def test_get_master_data_list(self,prepare_headers,case):
        headers = prepare_headers
        headers.update({"authorization": YamlUtil().read_yaml('token')})
        data = case["request"]["json"]

        req = ApiClient().post(json=data,headers=headers)
        rep = req.json()
        print(rep)
        with allure.step("验证获取主数据列表结果"):
            assert "error" not in rep
            allure.attach(json.dumps(rep), name="master_data_list", attachment_type=allure.attachment_type.JSON)

    @allure.story("筛选主数据")
    @pytest.mark.parametrize("case",YamlUtil().read_test_yaml("filter_mater_data_case.yaml"))
    def test_filter_master_data(self,prepare_headers,case):
        headers = prepare_headers
        headers.update({"authorization": YamlUtil().read_yaml('token')})
        data = case["request"]["json"]

        req = ApiClient().post(json=data,headers=headers)
        rep = req.json()
        print(rep)
        with allure.step("验证筛选主数据结果"):
            assert "error" not in rep
            allure.attach(json.dumps(rep), name="filter_master_data", attachment_type=allure.attachment_type.JSON)
















