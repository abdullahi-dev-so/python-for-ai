class APIConfig:
    def __init__(self,api_key,model ="gpt-3.5-turbo",max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"
# create different configuration
#using positional for required arg ,name  for optional
dev_config = APIConfig("sky_dev_key",max_tokens=200) 

# using all named arguments (clearest)
prod_config = APIConfig(api_key="sky_prod_key",model="gpt-4",max_tokens=500)

# access for configuration
print(f"Dev Config: {dev_config.model}")
print(f"Prod Config: {prod_config.model}")
print(f"Prod Config Max Tokens: {prod_config.max_tokens}")