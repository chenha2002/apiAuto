import pytest




@pytest.mark.parametrize("case")
@pytest.fixture(scope="function")
def prepare_headers(case):
    """统一处理请求头部的夹具"""
    # 初始化基础headers
    headers = case["request"].get("headers", {})
    return headers


