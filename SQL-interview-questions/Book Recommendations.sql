SELECT
  b1.genre,
  b1.book_title AS current_book,
  b2.book_title AS suggested_book
FROM goodreads AS b1
INNER JOIN goodreads AS b2
  ON b1.genre = b2.genre
WHERE b1.book_id != b2.book_id
ORDER BY b1.book_title;

/*** TAKING BOOK RECOMMENDATIONS TO ANOTHER NEXT LEVEL */
SELECT
  b1.genre,
  b1.book_title AS current_book,
  b2.book_title AS suggested_book_1,
  b3.book_title AS suggested_book_2
FROM goodreads AS b1
INNER JOIN goodreads AS b2 
  ON b1.genre = b2.genre
INNER JOIN goodreads as b3 
  ON b1.genre = b3.genre
WHERE b1.book_id != b2.book_id
  AND b1.book_id != b3.book_id
  AND b2.book_id != b3.book_id
ORDER BY b1.book_title,
LIMIT 50; 
