import pywhatkit as kit
import time

# Function to send message at a specific time
def send_whatsapp_message(phone_number, message, hour, minute, image_path=None):
    try:
        if image_path:
            # Send image along with a message
            kit.sendwhats_image(phone_number, image_path, message, time_hour=hour, time_minute=minute)
            print(f"Image and message sent to {phone_number} at {hour}:{minute}")
        else:
            # Send only text message
            kit.sendwhatmsg(phone_number, message, hour, minute)
            print(f"Message sent to {phone_number} at {hour}:{minute}")
    except Exception as e:
        print(f"Error: {e}")

# Ask user for details
phone_number = input("Enter the phone number (with country code, e.g., +1234567890): ")
message = input("Enter the message you want to send (you can use '\\n' for new lines): ")
hour = int(input("Enter the hour (24-hour format, e.g., 14 for 2:00 PM): "))
minute = int(input("Enter the minute (e.g., 30 for 2:30): "))

# Ask if user wants to send an image
image_choice = input("Do you want to send an image? (yes/no): ").lower()

image_path = None
if image_choice == "yes":
    image_path = input("Enter the image path (e.g., 'path/to/image.jpg'): ")

# Send the message or image with the provided details
send_whatsapp_message(phone_number, message, hour, minute, image_path)

# Wait for the message to be sent (this should be enough time for pywhatkit)
time.sleep(10)
