from google import genai

# Apni AQ wali API key daal yahan
client = genai.Client(api_key="")

print("Checking available models...")
try:
    for model in client.models.list():
        print(model.name)
except Exception as e:
    print(f"Error checking models: {e}")