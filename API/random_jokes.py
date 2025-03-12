import requests

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        category = user_data["categories"]["content"]
        id = user_data["categories"]["id"]
        return category, id
    else:
        raise Exception("Failed to fetch user data")
    
    
    
def main():
    try:
        category, id = fetch_random_jokes()
        print(f"category: {category} \nid: {id}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
    