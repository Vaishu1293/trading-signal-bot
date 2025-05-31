import requests

def send_telegram_message(token: str, chat_id: str, message: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    
    # Debug output
    print("🔁 Telegram API Response:")
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    return response.ok

def send_telegram_image(token: str, chat_id: str, image_path: str, caption: str = ""):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    with open(image_path, "rb") as image_file:
        files = {"photo": image_file}
        data = {
            "chat_id": chat_id,
            "caption": caption,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, data=data, files=files)
        print("🖼️ Image Upload Response:", response.status_code, response.text)
        return response.ok
