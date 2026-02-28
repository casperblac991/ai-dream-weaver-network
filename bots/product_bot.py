import os
import requests
import openai

# 1. إعداد مفاتيح API من الأسرار (Secrets)
openai.api_key = os.environ.get('OPENAI_API_KEY')
gumroad_token = os.environ.get('GUMROAD_ACCESS_TOKEN')

def generate_product_idea():
    # كود لتوليد فكرة المنتج باستخدام OpenAI
    # (بافتراض وجود هذا الجزء سابقاً)
    return {"name": "Product Name", "price": 10, "description": "Description"}

def create_gumroad_product(token, name, price, description):
    # 2. إرسال الطلب إلى API الخاص بـ Gumroad
    url = "https://api.gumroad.com/v2/products"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": name,
        "price": price,
        "description": description,
        "currency": "usd"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

# 3. تنفيذ العملية
product = generate_product_idea()
result = create_gumroad_product(gumroad_token, product['name'], product['price'], product['description'])
print(result)
