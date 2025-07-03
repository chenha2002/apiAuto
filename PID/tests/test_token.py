import allure
import pytest
import json

import requests

from PID.utils.yaml_util import YamlUtil
from PID.utils.api_client import ApiClient

class TestToken:

    @allure.story("获取token")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("case", YamlUtil().read_test_yaml("get_token_case.yaml"))
    def test_login_success(self, case):
        url = case["request"]['url']
        data = case["request"]['data']
        headers = case["request"]['headers']
        req = requests.post(url=url,data=data,headers=headers)
        rep = req.json()
        print(rep)
        with allure.step("验证获取token结果"):
            assert "errors" not in rep
            allure.attach(json.dumps(rep), name="token", attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_yaml({"token": "Bearer "+rep['access_token']})
