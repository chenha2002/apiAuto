import requests
from requests.exceptions import RequestException
from urllib.parse import urljoin


class ApiClient:
    # 类变量定义环境配置
    ENV = "uat"  # 默认环境，可通过 GraphQLClient.ENV = "uat" 动态修改
    DEFAULT_TIMEOUT = 10

    def __init__(self):
        # 初始化会话并设置默认请求头
        self.session = requests.session()


    @classmethod
    def base_url(cls) -> str:
        """获取当前环境的基础URL"""
        env_map = {
            "dev": "https://suhyang-dev.baozun.com/api/graphql/",
            "uat": "https://suhyang-uat.baozun.com/api/graphql/",
        }
        return env_map[cls.ENV]

    @classmethod
    def build_url(cls, endpoint: str) -> str:
        """安全构建完整URL"""
        return urljoin(cls.base_url(), endpoint.lstrip('/'))

    def send_request(
            self,
            method: str,
            endpoint: str = "",
            query: str = None,
            variables: dict = None,
            json: dict = None,
            data: dict = None,
            params: dict = None,
            headers: dict = None,
            timeout: int = DEFAULT_TIMEOUT
    ) -> requests.Response:

        url = self.build_url(endpoint)

        # 合并请求头
        # merged_headers = {**self.session.headers, **(headers or {})}

        # 构建请求载荷
        payload = {}
        if query:
            payload.update({"query": query})
        if variables:
            payload.update({"variables": variables})

        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                json=json or payload or None,
                params=params or None,
                data=data,
                headers=headers,
                timeout=timeout

            )
            response.raise_for_status()
            return response
        except RequestException as e:
            print(f"请求失败: {str(e)}")
            if hasattr(e, 'response') and e.response:
                print(f"响应内容: {e.response.text[:200]}...")  # 截断长内容
            raise

    # 快捷方法
    def execute_query(self,endpoint:str, query: str, variables: dict = None, **kwargs) -> dict:
        """执行GraphQL查询（POST专用快捷方法）"""
        resp = self.send_request("POST", endpoint=endpoint, query=query, variables=variables, **kwargs)
        return resp.json()

    def get(self, endpoint: str, params: dict = None, **kwargs) -> requests.Response:
        return self.send_request("GET", endpoint=endpoint, params=params, **kwargs)

    def post(self, endpoint: str = "", **kwargs) -> requests.Response:
        return self.send_request("POST", endpoint=endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self.send_request("PUT", endpoint=endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.send_request("DELETE", endpoint=endpoint, **kwargs)