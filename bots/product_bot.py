import os
import requests
from openai import OpenAI

# 1. إعداد العميل لـ OpenAI
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
gumroad_token = os.environ.get('GUMROAD_ACCESS_TOKEN')

def generate_product_idea():
    """توليد فكرة منتج رقمي باستخدام OpenAI"""
    prompt = "Generate a creative and profitable digital product idea for a developer or creator. Provide a name, a price in USD (between 5 and 50), and a short compelling description."
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative product strategist."},
            {"role": "user", "content": prompt}
        ],
        response_format={ "type": "json_object" }
    )
    
    # توقع استجابة JSON تحتوي على name, price, description
    import json
    idea = json.loads(response.choices[0].message.content)
    return idea

def create_gumroad_product(token, name, price, description):
    """إنشاء منتج على Gumroad"""
    if not token:
        print("Error: GUMROAD_ACCESS_TOKEN is not set.")
        return None
        
    url = "https://api.gumroad.com/v2/products"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": name,
        "price": int(price) * 100,  # Gumroad uses cents
        "description": description,
        "currency": "usd"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

if __name__ == "__main__":
    print("Generating product idea...")
    try:
        product = generate_product_idea()
        print(f"Product Idea: {product}")
        
        print("Creating product on Gumroad...")
        result = create_gumroad_product(gumroad_token, product.get('name'), product.get('price'), product.get('description'))
        print(f"Gumroad Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
