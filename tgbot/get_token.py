# Understanding the Single Responsibility Principle (SRP) of SOLID
import os 
from dotenv import load_dotenv

load_dotenv()

def GetToken():
    MY_TOKEN = os.getenv("TGBOTTOKEN", None)
    if MY_TOKEN: return MY_TOKEN.strip()
    else: raise Exception("Token tapılmadı!")

