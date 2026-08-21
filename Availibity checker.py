books = ["matilda", "harry potter", "wonder", "the jungle book", "charlie"]
copy_counts = [4, 0, 6, 3, 2]

library = {book: count for book, count in zip(books, copy_counts)}
print("Full Library Stock:", library)

available_books = [book for book in books if library[book] > 0]
print("Books Available:", available_books)

chosen_book = input("Which book do you want to borrow? ")

if chosen_book not in library or library[chosen_book] == 0:
    print(chosen_book, "is not available! Stopping the checker.")
    exit()

late_fees = [5, 8, 4, 6, 7]
extra_fee = int(input("Enter the extra library fee to add to every book: "))

updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
print("Updated Late Fees:", updated_fees)

book_index = books.index(chosen_book)
chosen_fee = updated_fees[book_index]
print("Late fee for", chosen_book, "after update:", chosen_fee)

library[chosen_book] = library[chosen_book] - 1
print(chosen_book, "borrowed! Remaining copies:", library[chosen_book])

print("")
print("===== LIBRARY BOOK AVAILABILITY CHECKER =====")
print("Book Borrowed:", chosen_book)
print("Late Fee:", chosen_fee)
print("Updated Library Stock:", library)
print("=============================================")