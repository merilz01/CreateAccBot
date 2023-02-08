import dotenv
import os

dotenv.load_dotenv()

words = "abcdefghijklmnopqrstuvwxyz"
wordshigh = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "!@#$%^&*(){}?№%"

TG_TOKEN = os.getenv("TG_TOKEN")
RESULT_PHRASE = words + wordshigh + numbers + special
WELCOME_MESSAGE = "Use /help to get help."
