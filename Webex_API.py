import requests

# Collect Webex Token
webex_token = input("Please Enter your Webex token: ")

while True:
    print("\nMain Menu:")
    print("0. Test Connection")
    print("1. Display User Information")
    print("2. List Rooms")
    print("3. Create a Room")
    print("4. Send Message to a Room")
    print("5. Exit")

    choice = input("Enter your choice (0-5): ")

    if choice == "0":
        # Option 0: Test Connection
        response = requests.get("https://api.ciscospark.com/v1/people/me", headers={"Authorization": f"Bearer {webex_token}"})
        
        if response.status_code == 200:
            print("Connection with Webex server is successful.")
        else:
            print("Connection test failed. Please check your Webex token.")

    elif choice == "1":
        # Option 1: Display User Information
        response = requests.get("https://api.ciscospark.com/v1/people/me", headers={"Authorization": f"Bearer {webex_token}"})
        
        if response.status_code == 200:
            user_data = response.json()
            print("\nUser Information:")
            print(f"Display Name: {user_data['displayName']}")
            print(f"Nickname: {user_data.get('nickName', 'N/A')}")
            print(f"Emails: {', '.join(user_data['emails'])}")
        else:
            print("Failed to retrieve user information. Please check your Webex token.")

    elif choice == "2":
        # Option 2: List Rooms
        response = requests.get("https://api.ciscospark.com/v1/rooms", headers={"Authorization": f"Bearer {webex_token}"})
        
        if response.status_code == 200:
            rooms = response.json()
            print("\nList of Rooms:")
            for room in rooms["items"][:5]:  # Display the first 5 rooms
                print(f"Room ID: {room['id']}")
                print(f"Room Title: {room['title']}")
                print(f"Date Created: {room['created']}")
                print(f"Last Activity: {room['lastActivity']}\n")
        else:
            print("Failed to retrieve room information. Please check your Webex token.")

    elif choice == "3":
        # Option 3: Create a Room
        room_title = input("Enter the title of the room: ")
        room_data = {"title": room_title}
        response = requests.post("https://api.ciscospark.com/v1/rooms", headers={"Authorization": f"Bearer {webex_token}"}, json=room_data)
        
        if response.status_code == 200:
            print(f"Room '{room_title}' created successfully.")
        else:
            print("Failed to create the room. Please check your Webex token.")

    elif choice == "4":
        # Option 4: Send Message to a Room
        response = requests.get("https://api.ciscospark.com/v1/rooms", headers={"Authorization": f"Bearer {webex_token}"})
        
        if response.status_code == 200:
            rooms = response.json()
            print("\nList of Rooms:")
            for i, room in enumerate(rooms["items"][:5], 1):
                print(f"{i}. Room Title: {room['title']}")
            
            room_choice = input("Enter the number of the room to send a message to: ")
            room_id = rooms["items"][int(room_choice) - 1]["id"]
            
            message = input("Enter the message to send: ")
            message_data = {"roomId": room_id, "text": message}
            
            response = requests.post("https://api.ciscospark.com/v1/messages", headers={"Authorization": f"Bearer {webex_token}"}, json=message_data)
            
            if response.status_code == 200:
                print("Message sent successfully.")
            else:
                print("Failed to send the message. Please check your Webex token.")
        else:
            print("Failed to retrieve room information. Please check your Webex token.")
    
    elif choice == "5":
        print("Exiting the application.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
