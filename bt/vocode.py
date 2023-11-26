import os

from dotenv import load_dotenv
from vocode.client import Vocode

load_dotenv()


VOCODE_API_KEY = os.getenv("VOCODE_API_KEY")

vocode_client = Vocode(
  token=VOCODE_API_KEY
)
