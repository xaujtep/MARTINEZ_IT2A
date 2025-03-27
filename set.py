def record_keeping_app():
    data_store = set()  # Set to store unique key-value pairs as tuples
    
    while True:
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")
        choice = input("Enter your choice (a/b/c): ").lower()
        
        if choice == 'a':
            # Add Data
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            data_store.add((key, value))
            print("\nData Added Successfully!")
            print("Current Data:")
            for item in data_store:
                print(item)
        
        elif choice == 'b':
            # Delete Data
            key_to_delete = input("Enter Key to Delete: ")
            found = False
            for item in list(data_store):  # Convert to list to allow removal
                if item[0] == key_to_delete:
                    data_store.remove(item)
                    found = True
            if found:
                print("\nData Deleted Successfully!")
            else:
                print("\nKey not found!")
            print("Current Data:")
            for item in data_store:
                print(item)
        
        elif choice == 'c':
            # End
            print("\nTHANK YOU")
            break
        
        else:
            print("\nInvalid choice! Please choose a, b, or c.")

# Run the application
record_keeping_app()
