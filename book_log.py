'''A simple book rating system that allows users to add, remove, search, and display books with their ratings.
The book list is stored as a list of dictionaries, where each dictionary contains the title, author, and rating of a book. 
The program provides a menu for users to interact with the system and perform various operations on the book list.
The rating is represented visually using chili pepper emojis, where each chili pepper corresponds to one rating point (e.g., a rating of 3 would be displayed as 🌶️🌶️🌶️). 
The program also includes input validation to ensure that users enter valid data when adding books and removing them.'''

book_list = []

def add_book():
    '''Adds a book to the book list with title, author, and rating.'''
    while True:
        title = input("Enter the book title: ").strip().title()
        if title:
            break
        print("Title cannot be empty. Please try again.")
    while True:
        author = input("Enter the book author: ").strip().title()
        if author:
            break
        print("Author cannot be empty. Please try again.")
    while True:
        try:
            rating = int(input("Enter your rating for the book (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Rating must be between 1 and 5. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    book = { 
        'title': title,
        'author': author,
        'rating': rating
    }
    book_list.append(book)
    print(f"Book '{title}' by {author} added with rating {rating}.")
    
def remove_book():
    '''Removes a book from the book list based on user input.'''
    if not book_list:
        print("No books to remove.")
        return
    display_books()
    try:
        index = int(input("Enter the number of the book to remove: ")) - 1
        if 0 <= index < len(book_list):
            removed_book = book_list.pop(index)
            print(f"Removed book: {removed_book['title']} by {removed_book['author']}.")
        else:
            print("Invalid number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
        
  
def search_books():
    '''Searches for books by title.'''
    query = input("Enter the title to search for: ").strip().lower()
    found_books = [book for book in book_list if query in book['title'].lower()]
    if found_books:
        print("Search results:")
        for book in found_books:
            rating_chili = '🌶️' * book['rating']
            print(f"Title: {book['title']}, Author: {book['author']}, Rating: {rating_chili} ({book['rating']}/5)")
    else:
        print("No books found matching your search.")   
        add_new = input("Would you like to add this book? (y/n): ").strip().lower()
        if add_new == 'y':
            add_book()
             
def display_books():
    '''Displays all books in the book list.'''
    if not book_list:
        print("No books to display.")
        return
    for i, book in enumerate(book_list, start=1):
        rating_chili = '🌶️' * book['rating']
        print(f"{i}. Title: {book['title']}, Author: {book['author']}, Rating: {rating_chili} ({book['rating']}/5)") 
     
def show_stats():
    '''Displays total books, average rating, and highest-rated book.'''
    if not book_list:
        print("No books logged yet.")
        return
    total = len(book_list)
    avg = sum(book['rating'] for book in book_list) / total
    best = max(book_list, key=lambda b: b['rating'])
    print(f"\n📚 Total books logged: {total}")
    print(f"⭐ Average rating: {avg:.1f}/5")
    print(f"🌶️  Highest rated: {best['title']} by {best['author']} ({'🌶️' * best['rating']})")
   
def main():
    '''Main function to run the book rating system.'''
    while True:
        print("\nBook Rating System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for books")
        print("4. Display all books")
        print("5. Show statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_books()
        elif choice == '4':
            display_books()
        elif choice == '5':
            show_stats()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()