class books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_rented = False 

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"\nSuccess: '{self.title}' rented out.")
        else:
            print(f"\nError: '{self.title}' is already rented.")

    def return_books(self):
        if self.is_rented:
            self.is_rented = False
            print(f"\nSuccess: '{self.title}' returned.")
        else:
            print(f"\nError: '{self.title}' is not currently rented.")

Books = [
    books("Backrooms", "Kane Parsons"),
    books("Obsession", "Curry Barker"),
    books("Inception", "Christopher Nolan")
]

while True:
    # 1. Display current inventory and status
    print("\n================ BOOKS INVENTORY ================")
    for index, b in enumerate(Books, start=1):
        status = "Rented" if b.is_rented else "Available"
        print(f"[{index}] {b.title:12} | author: {b.author:10} | Status: {status}")
    print("[0] Exit System")
    print("================================================")

    
    choice = input("Select a book number (or 0 to exit): ").strip()
    
    if choice == "0":
        print("Goodbye!")
        break
        
    if not choice.isdigit() or not (1 <= int(choice) <= len(Books)):
        print("Invalid selection. Please try again.")
        continue

    
    selected_books = Books[int(choice) - 1]
    print(f"\nYou selected: {selected_books.title}")

    action = input("Do you want to (R)ent, (T)urn in/Return, or (C)ancel? ").strip().upper()

    if action == "R":
        selected_books.rent()
    elif action == "T":
        selected_books.return_books()
    elif action == "C":
        print("Action cancelled.")
    else:
        print("Invalid action selected.")