# LIBRARY-BOOK-BORROWING-SYSTEM
Library Book Borrowing System** – A command‑line Python program that simulates a library's book borrowing process. Librarians can enter member details, calculate borrowing fees and late fines, and view a summary of all transactions. Ideal for learning functions, loops, conditionals, and input validation.
Below is a **detailed README.md** for your **Library Book Borrowing System** project, followed by a **short description** suitable for the GitHub repository’s “About” section.

---

## README.md

```markdown
# 📚 Library Book Borrowing System

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![CLI](https://img.shields.io/badge/platform-CLI-lightgrey)

A **command‑line program** that simulates a library’s book borrowing process.  
Librarians can enter member details, calculate borrowing fees and late fines, and view a summary of all transactions. Perfect for learning basic Python concepts like functions, loops, conditionals, and input validation.

---

## 📖 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation & Usage](#installation--usage)
- [Example Run](#example-run)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## ✨ Features

- **Add multiple members** – Enter as many members as needed.
- **Validate book categories** – Only `Regular`, `Reference`, or `Magazine` are accepted.
- **Calculate borrowing fees** – Based on category:
  - Regular → 1000 UGX
  - Reference → 2000 UGX
  - Magazine → 500 UGX
- **Compute late fines** – Tiered penalty system:
  - 0 days late → No fine
  - 1–5 days late → 500 UGX per day
  - More than 5 days late → First 5 days at 500 UGX/day, additional days at 1000 UGX/day
- **Print a detailed receipt** for each member showing:
  - Member name, book title, category
  - Borrowing fee, late fine, total due
- **Display summary statistics** after all entries:
  - Total members served
  - Total revenue collected
  - Average payment per member
- **Robust input handling** – Prevents crashes from invalid inputs.

---

## 🖥 Requirements

- **Python 3.x** (no external libraries needed)

---

## 🚀 Installation & Usage

1. **Clone the repository** (or download the `library_system.py` file directly):
   ```bash
   git clone https://github.com/your-username/library-book-borrowing-system.git
   cd library-book-borrowing-system
   ```

2. **Run the program**:
   ```bash
   python library_system.py
   ```

3. Follow the interactive prompts to enter member data.

---

## 🧪 Example Run

```
===== LIBRARY BOOK BORROWING SYSTEM =====
Enter Member Name: Innocent
Enter Book Title: Python Basics
Enter Book Category (Regular/Reference/Magazine): Regular
Enter Days Borrowed: 7
Enter Days Late: 3

----- RECEIPT -----
Member: Innocent
Book: Python Basics
Category: Regular
Borrowing Fee: 1000 UGX
Late Fine: 1500 UGX
Total Due: 2500 UGX
-------------------

Add another member? (yes/no): yes

Enter Member Name: Sarah
Enter Book Title: Data Science 101
Enter Book Category (Regular/Reference/Magazine): Reference
Enter Days Borrowed: 10
Enter Days Late: 0

----- RECEIPT -----
Member: Sarah
Book: Data Science 101
Category: Reference
Borrowing Fee: 2000 UGX
Late Fine: 0 UGX
Total Due: 2000 UGX
-------------------

Add another member? (yes/no): no

===== SUMMARY =====
Total Members Served: 2
Total Revenue Collected: 4500 UGX
Average Payment Per Member: 2250 UGX
```

---

## ⚙️ How It Works

The program is structured into several functions, each with a single responsibility:

- **`calculate_borrowing_fee(category)`** – Returns the flat borrowing fee based on the book category.
- **`calculate_late_fine(days_late)`** – Implements the tiered fine calculation.
- **`display_receipt(...)`** – Prints a formatted receipt for a member.
- **`main()`** – Orchestrates the entire flow:
  - Loops until the librarian stops.
  - Collects and validates input.
  - Computes fees and fines.
  - Displays the receipt.
  - Updates summary statistics.
  - Finally prints the summary.

Input validation ensures that:
- The book category must be one of the three allowed values.
- Days borrowed and days late must be integers (basic error handling prevents crashes).



## 🤝 Contributing

Contributions are welcome! If you’d like to improve this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please ensure your code follows the existing style and includes appropriate comments.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---


## 🙏 Acknowledgements

- This project was created as part of a programming assignment to demonstrate structured programming in Python.
- Inspired by real‑world library management systems.
```
