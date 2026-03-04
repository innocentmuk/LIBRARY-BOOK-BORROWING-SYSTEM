def member_details():
    add_member = "yes"
    while add_member == "yes":
      member_name = input("Enter Member Name: ")
      book_title = input("Enter Book Title: ")

      category = input("Enter Book Category(Regular/Reference/Magazine): ")
      category = category.lower()
      while category != "regular" and category != "reference" and category != "magazine":
          print("Error: Invalid category! Please enter Regular, Reference, or Magazine.")
          category = input("Enter Book Category(Regular/Reference/Magazine): ")



      days_borrowed = int(input("Enter Days Borrowed: "))
      days_late = int(input("Enter Days Late: "))
      add_member = input("Add another member?(yes/no): ")
      if add_member != "yes":
          break
    return member_name,book_title,category,days_borrowed,days_late,add_member

def calculate_borrowing_fee(category):
    fee = 0
    if category == "regular":
        fee = 1000
    elif category == "reference":
        fee = 2000
    elif category == "magazine":
        fee = 500

member_details()
