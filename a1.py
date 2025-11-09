# 1. Import necessary libraries
import requests
from config import HF_API_KEY
# 2. Define constants
MODEL_ID = "nlpconnect/vit-gpt2-image-captioning"
API_URL = "https://api-inference.huggingface.co/models/" + MODEL_ID

# 3. Define authorization headers
headers = {
    "Authorization": "Bearer " +HF_API_KEY
}

# 4. Function to caption a single image
def caption_single_image():
    # 4.1. Specify image file path
    image_source = "test.jpg"

    # 4.2. Try to read image as binary
    try:
        with open(image_source, "rb") as file:
            image_bytes = file.read()
    except Exception as error:
        print("Error opening image:", error)
        return        
    
    # 4.3. Make POST request to Hugging Face API
    response = requests.post(API_URL, headers=headers, data=image_bytes)

    # 4.4. Parse JSON response
    result = response.json()

    # 4.5. Handle potential API error
    if isinstance(result, dict) and "error" in result:
        print("API Error:", result["error"])
        return
    
    # 4.6. Extract caption
    caption = result[0].get("generated_text", "No caption found.")

    # 4.7. Display results
    print(f"Image: {image_source}")
    print(f"Caption: {caption}")

# 5. Main entry point
def main():
    caption_single_image()

# 6. Execute script
if __name__ == "__main__":
    main()    


    
    