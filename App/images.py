from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    #url_endpoint=os.getenv("IMAGEKIT_URL")
    )

   # public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"), # Changed from public_key_endpoint
   # url_endpoint=os.getenv("IMAGEKIT_URL"),       # Changed from imgkit_url
