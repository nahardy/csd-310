/*
    Nick Hardy
    Module 12.3 Whatabook init script
    3/4/2023
*/

-- drop user if exist
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook user and grant them all privileges to the database
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password by 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop constraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop table if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

-- create tables
CREATE TABLE store (
    store_id    INT         NOT NULL        AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id    INT         NOT NULL        AUTO_INCREMENT,
    book_name      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id    INT         NOT NULL        AUTO_INCREMENT,
    first_name      VARCHAR(75)    NOT NULL,
    last_name       VARCHAR(75)    NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE wishlist (
    wishlist_id    INT         NOT NULL        AUTO_INCREMENT,
    user_id        INT    NOT NULL,
    book_id        INT    NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);
-- insert store record

INSERT INTO store(locale)
   VALUES ('2109 TOWNE Centre DR, Bellevue, NE 68123'); 


-- insert book records

INSERT INTO book(book_name, author, details)
   VALUES ('Of Mice and Men', 'John Steinbeck', 'High School Favorite');

INSERT INTO book(book_name, author, details)
   VALUES ('To Kill a Mockingbird', 'Harper Lee', 'Another High School Favorite');

INSERT INTO book(book_name, author, details)
   VALUES ('1984', 'George Orwell', 'Written in 1949');

INSERT INTO book(book_name, author, details)
   VALUES ('The Catcher in the Rye', 'J.D. Salinger','Funny and meaningful');

INSERT INTO book(book_name, author, details)
   VALUES ('Lord of the Flies', 'William Golding', 'Stranded on a deserted island');

INSERT INTO book(book_name, author, details)
   VALUES ('The Scarlet Letter', 'Nathaniel Hawthorne', 'Historical fiction');

INSERT INTO book(book_name, author, details)
   VALUES ('The Outsiders', 'S.E. Hinton', 'Greasers vs Socs');

INSERT INTO book(book_name, author, details)
   VALUES ('The Giver', 'Lois Lowry', 'Newbery Medal winner');

INSERT INTO book(book_name, author, details)
   VALUES ('Tuck Everlasting', 'Natalie Babbitt', 'Never grow old');


-- insert users

INSERT INTO user(first_name, last_name)
    VALUES('Mike', 'Tyson');

INSERT INTO user(first_name, last_name)
    VALUES('Bud', 'Crawford');

INSERT INTO user(first_name, last_name)
    VALUES('Evander', 'Holyfield');


-- insert wishlist books

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Mike'),
        (SELECT book_id FROM book WHERE book_name = '1984')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Bud'),
        (SELECT book_id FROM book WHERE book_name = 'The Outsiders')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Evander'),
        (SELECT book_id FROM book WHERE book_name = 'The Giver')
    );
