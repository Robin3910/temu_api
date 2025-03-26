import hashlib
import json
import time
import requests
from temu_api import TemuAPI

def main():
    # 使用示例
    temu = TemuAPI()
    
    try:
        order_list = [] 
        for page_number in range(1, 10):
            order_list.extend(temu.get_order_list(page_size=100, page_number=page_number)['result']['pageItems'])

        customized_products_order_list = []

        for order in order_list:
            for item in order['orderList']:
                for order_label in item['orderLabel']:
                    if order_label['name'] == 'customized_products' and order_label['value'] != 0:
                        customized_products_order_list.append(order['parentOrderMap']['parentOrderSn'])

        print(customized_products_order_list)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
