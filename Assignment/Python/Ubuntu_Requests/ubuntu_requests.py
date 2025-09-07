import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    url = input("https://images.pexels.com/photos/33240142/pexels-photo-33240142.jpeg: ").strip()

    # Create directory if it doesn't exist
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Try to extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename or '.' not in filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"image_{timestamp}.jpg"

        # Save image in binary mode
        filepath = os.path.join(folder_name, filename)
        with open(filepath, 'wb') as file:
            file.write(response.content)

        print(f"✅ Image saved as '{filename}' in '{folder_name}'")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet or the URL.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except requests.exceptions.RequestException as err:
        print(f"❌ An error occurred: {err}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    fetch_image()
