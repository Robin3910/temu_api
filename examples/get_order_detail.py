import hashlib
import json
import time
import requests
from temu_api import TemuAPI

def main():
    # 使用示例
    temu = TemuAPI()
    
    try:
        order_detail = temu.get_order_detail("PO-211-04294571750951171")

        print(order_detail)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
