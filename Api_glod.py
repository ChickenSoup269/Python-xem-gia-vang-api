import requests
import json
from tabulate import tabulate

# URL của API
url = "http://api.btmc.vn/api/BTMCAPI/getpricebtmc?key=3kd8ub1llcg9t45hnoh8hmn7t5kc2v"

# Gọi API để lấy dữ liệu
response = requests.get(url)
response_json = response.json()

# Kiểm tra dữ liệu JSON
# print("Dữ liệu JSON trả về từ API:")
# print(json.dumps(response_json, indent=4))

# Chuyển đổi dữ liệu JSON thành bảng
data = []
for item in response_json.get('DataList', {}).get('Data', []):
    row_number = item.get('@row')
    row_data = {
        'Name': item.get(f'@n_{row_number}'),
        'Karats': item.get(f'@k_{row_number}'),
        'Purity': item.get(f'@h_{row_number}'),
        'Giá mua (VND)': int(item.get(f'@pb_{row_number}', 0)),
        'Giá bán (VND)': int(item.get(f'@ps_{row_number}', 0)),
        'Timestamp': item.get(f'@d_{row_number}')
    }
    data.append(row_data)

# Tạo bảng từ danh sách dữ liệu
table = tabulate(data, headers="keys", tablefmt="fancy_grid")

# Xuất bảng
print("\nBảng giá vàng:")
print(table)
