import json

import allure
import pytest

from Suhyang.utils.api_client import ApiClient
from Suhyang.utils.yaml_util import YamlUtil


@allure.feature("登录")
class TestLogin:


    @allure.story("会员密码登录")
    @pytest.mark.run(order=1)
    @pytest.mark.account
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("account_login_case.yaml"))
    def test_login_success(self, case):
        req = ApiClient().post(endpoint="accountLoginGql", json=case["request"]["json"])
        rep = req.json()
        with allure.step("验证登录结果"):
           assert "errors" not in rep
           allure.attach(json.dumps(rep), name="accountLoginGql", attachment_type=allure.attachment_type.JSON)
           print(rep)
           if "token" in rep['data']['accountLogin']:
               YamlUtil().write_yaml({"token": rep['data']['accountLogin']['token']})



    @allure.story("游客登录")
    @pytest.mark.run(order=1)
    @pytest.mark.visitor
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("visitor_login_case.yaml"))
    def test_login_guest(self, case):
        req = ApiClient().post(endpoint="visitorLoginGql", json=case["request"]["json"])
        rep = req.json()
        print(rep)
        with allure.step("验证登录结果"):
            assert "errors" not in rep
            allure.attach(json.dumps(rep), name="visitorLoginGql", attachment_type=allure.attachment_type.JSON)

        