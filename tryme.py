import openai
from config import key  

openai.api_key = key


response = openai.Image.create(
    prompt="cat stealing money",
    n=1, 
    size="1024x1024"  
)

# Extract the URL of the generated image
image_url = response['data'][0]['url']
print(image_url)
