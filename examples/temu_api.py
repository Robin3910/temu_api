import hashlib
import json
import time
import requests
from typing import Dict, Any, Optional

class TemuAPI:
    def __init__(self, app_key: str = None, app_secret: str = None, access_token: str = None):
        # API凭证
        self.app_key = app_key or "4ebbc9190ae410443d65b4c2faca981f"
        self.app_secret = app_secret or "4782d2d827276688bf4758bed55dbdd4bbe79a79"
        self.access_token = access_token or "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7"
        self.base_url = "https://openapi-b-us.temu.com/openapi/router"

    def generate_signature(self, params: Dict) -> str:
        sorted_keys = sorted(params.keys())
        base_string = self.app_secret
        for key in sorted_keys:
            value = params[key]
            if isinstance(value, (dict, list)):
                base_string += f"{key}{json.dumps(value)}"
            else:
                base_string += f"{key}{value}"
        base_string += self.app_secret
        return hashlib.md5(base_string.encode('utf-8')).hexdigest().upper()

    def make_request(self, method_params: Dict) -> Dict:
        params = {
            "timestamp": str(int(time.time())),
            "app_key": self.app_key,
            "data_type": "JSON",
            "access_token": self.access_token,
            **method_params
        }
        
        sign = self.generate_signature(params)
        params["sign"] = sign
        
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(
            self.base_url,
            json=params,
            headers=headers
        )
        
        return response.json()

    def get_order_list(self, page_size: int = 100, page_number: int = 1, 
                       parent_order_status: int = 0) -> Dict:
        """获取订单列表"""
        method_params = {
            "type": "bg.order.list.v2.get",
            "pageSize": page_size,
            "pageNumber": page_number,
            "parentOrderStatus": parent_order_status
        }
        return self.make_request(method_params)

    def get_order_detail(self, order_id: str) -> Dict:
        """获取订单详情"""
        method_params = {
            "type": "bg.order.detail.get",
            "orderId": order_id
        }
        return self.make_request(method_params)

    def get_logistics_info(self, order_id: str) -> Dict:
        """获取物流信息"""
        method_params = {
            "type": "bg.logistics.get",
            "orderId": order_id
        }
        return self.make_request(method_params)

# # 使用示例
# if __name__ == "__main__":
#     # 创建API实例
#     temu = TemuAPI()
    
#     try:
#         # 获取订单列表
#         order_list = temu.get_order_list(page_size=50, page_number=1)
#         print("订单列表:", json.dumps(order_list, indent=2, ensure_ascii=False))
        
#         # 如果有订单，获取第一个订单的详情
#         if order_list.get("data", {}).get("list"):
#             first_order_id = order_list["data"]["list"][0]["orderId"]
            
#             # 获取订单详情
#             order_detail = temu.get_order_detail(first_order_id)
#             print("\n订单详情:", json.dumps(order_detail, indent=2, ensure_ascii=False))
            
#             # 获取物流信息
#             logistics_info = temu.get_logistics_info(first_order_id)
#             print("\n物流信息:", json.dumps(logistics_info, indent=2, ensure_ascii=False))
            
#     except Exception as e:
#         print(f"发生错误: {e}") 