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
