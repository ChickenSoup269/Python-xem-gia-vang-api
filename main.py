import requests
import json
from tabulate import tabulate
from colorama import Fore, Style, init

# Khởi tạo colorama
init(autoreset=True)

class GoldPriceFetcher:
    def __init__(self, url):
        self.url = url
        self.data = []
    
    def fetch_data(self):
        """Lấy dữ liệu từ API"""
        response = requests.get(self.url)
        response_json = response.json()
        self.data = [
            [
                item.get(f'@n_{item.get("@row")}'),
                item.get(f'@k_{item.get("@row")}'),
                item.get(f'@h_{item.get("@row")}'),
                int(item.get(f'@pb_{item.get("@row")}', 0)),
                int(item.get(f'@ps_{item.get("@row")}', 0)),
                item.get(f'@d_{item.get("@row")}')
            ]
            for item in response_json.get('DataList', {}).get('Data', [])
        ]

class TableFormatter:
    def __init__(self, data):
        self.data = data
    
    def format_table(self):
        """Định dạng bảng với tiêu đề màu sắc"""
        headers = [
            f"{Fore.RED}Name{Style.RESET_ALL}",
            f"{Fore.BLUE}Karats{Style.RESET_ALL}",
            f"{Fore.YELLOW}Purity{Style.RESET_ALL}",
            f"{Fore.GREEN}Giá mua (VND){Style.RESET_ALL}",
            f"{Fore.GREEN}Giá bán (VND){Style.RESET_ALL}",
            f"{Fore.CYAN}Timestamp{Style.RESET_ALL}"
        ]
        
        # Tạo bảng từ danh sách dữ liệu
        table = tabulate(self.data, headers=headers, tablefmt="rounded_outline")
        return table

class GoldPriceApp:
    def __init__(self, api_url):
        self.fetcher = GoldPriceFetcher(api_url)
        self.formatter = None
    
    def run(self):
        # Lấy dữ liệu từ API
        self.fetcher.fetch_data()
        
        # Định dạng bảng
        self.formatter = TableFormatter(self.fetcher.data)
        table = self.formatter.format_table()
        
        # Xuất bảng
        print("\nBảng giá vàng:")
        print(table)

# URL của API
api_url = "http://api.btmc.vn/api/BTMCAPI/getpricebtmc?key=3kd8ub1llcg9t45hnoh8hmn7t5kc2v"

# Khởi chạy ứng dụng
app = GoldPriceApp(api_url)
app.run()
