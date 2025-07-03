import pytest
import requests

from PID.utils.yaml_util import YamlUtil
from PID.utils.api_client import ApiClient




@pytest.mark.parametrize("case")
@pytest.fixture(scope="function")
def prepare_headers(case):
    """统一处理请求头部的夹具"""
    # 初始化基础headers
    if isinstance(case, (list, dict)):  # 统一处理 list 和 dict 类型
        request_data = case[0]["request"] if isinstance(case, list) else case["request"]
        headers = request_data.get("headers", {})
        headers.update({"authorization": YamlUtil().read_yaml("token")})
        return headers
    return {}  # 如果 case 不是 list 或 dict，返回空字典




