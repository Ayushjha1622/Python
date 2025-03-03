import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
        
def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}.")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    
def update_video(videos):
    pass

def  delete_video(videos):
    pass

videos = load_data()

def main():

    while True:
        print("\n Youtube manager |choose an option")
        print("1. list of all videos")
        print("2. Add video")
        print("3. update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("enter your choice: ")
        print(videos)
        
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")
                
            
        
if __name__ == "__main__":
    main()