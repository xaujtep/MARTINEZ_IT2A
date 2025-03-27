<<<<<<< HEAD
print("\n\tOutput")
print("\n\t--------------")
grocery = ("apple","chicken","lemon","veggies","")
=======
# print("\n\tOutput")
# print("\n\t--------------")
# grocery = ["apple","chicken","lemon","veggies"]
# print(grocery)

dict =	{
  "name": "Stephanie",
  "course": "BSIT",
  "age": 19
}

# dict['course'] = "BSIT";
# dict['school'] = "DLL";

# del dict['name'];
# dict.clear()
# del dict;

# print("My name is", dict ['name'], "I am", dict ['age'], "years old and I am actually currently a", dict ['course'], "student in", dict['school'])
def translate_to_bisaya(word, dictionary):
    return dictionary.get(word, "Translation not found")

def add_translation(dictionary):
    tagalog_word = input("Enter the Tagalog word to add: ").lower()
    bisaya_translation = input("Enter the Bisaya translation: ").lower()
    if tagalog_word in dictionary:
        print("\nThis word already exists. Updating its translation...")
    dictionary[tagalog_word] = bisaya_translation
    print("\nNew translation added successfully!")

def record_keeping_app():
    tagalog_to_bisaya = {  # Dictionary to store Tagalog-to-Bisaya translations
        "kamusta": "kumusta",
        "salamat": "daghang salamat",
        "paalam": "padayon"
    }
    
    while True:
        print("\nChoose an option:")
        print("a. Translate to Bisaya")
        print("b. Add New Translation")
        print("c. View All Translations")
        print("d. End")
        choice = input("Enter your choice (a/b/c/d): ").lower()
        
        if choice == 'a':
            # Translate word to Bisaya
            print("Choose here(available word to translate): ")
            print("kamusta")
            print("salamat")
            print("paalam")

            tagalog_word = input("Enter the Tagalog word to translate: ").lower()
            translation = translate_to_bisaya(tagalog_word, tagalog_to_bisaya)
            print(f"The Bisaya translation for '{tagalog_word}' is: {translation}")
            
            # Ask if user wants to add a new translation
            add_new = input("Do you want to add a new translation? (yes/no): ").lower()
            if add_new == 'yes':
                add_translation(tagalog_to_bisaya)
        
        elif choice == 'b':
            # Add new translation
            add_translation(tagalog_to_bisaya)
        
        elif choice == 'c':
            # View all translations
            print("\nCurrent Tagalog-to-Bisaya Translations:")
            for tagalog_word, bisaya_translation in tagalog_to_bisaya.items():
                print(f"{tagalog_word} : {bisaya_translation}")
        
        elif choice == 'd':
            # End
            print("\nTHANK YOU")
            break
        
        else:
            print("\nInvalid choice! Please choose a, b, c, or d.")

# Run the application
record_keeping_app()
>>>>>>> afb4775 (Initial commit)
