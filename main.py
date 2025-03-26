import hashlib
import json
import time
import requests
from temu_api import TemuAPI

def main():
    # 使用示例
    temu = TemuAPI()
    
    try:
        order_list = temu.get_order_list(page_size=50, page_number=1)

        print(order_list)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
