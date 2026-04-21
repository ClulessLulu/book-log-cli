# 📚 Book Log CLI

A command-line book rating system built in Python. Log books you've read, rate them with 🌶️ chili peppers, search your collection, and view stats.

Built as Week 1 of my AI Engineer learning roadmap.

## Features

- **Add a book** — title, author, and a 1–5 🌶️ rating
- **Remove a book** — select by number from your list
- **Search by title** — case-insensitive, with an option to add the book if not found
- **Display all books** — formatted list with visual chili pepper ratings
- **Show stats** — total books logged, average rating, and highest-rated book

## How to run

```bash
python book_log.py
```

Requires Python 3.6+. No external libraries needed.

## Example
Book Rating System

Add a book
Remove a book
Search for books
Display all books
Show statistics
Exit

Enter your choice: 1
Enter the book title: dune
Enter the book author: frank herbert
Enter your rating for the book (1-5): 5
Book 'Dune' by Frank Herbert added with rating 5.

## What I struggled with and solved

What I struggle with was accidentally creating a readme file when creating a repo which caused a merged conflicted. This was resolved by just a pit pull then allow unrelated histories. I was also having a hard time trying to figure out how to ask adding a book when an error happened but was resolved with a while true loop.

## Tech

- Python 3
- No external dependencies