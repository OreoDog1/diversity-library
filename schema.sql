CREATE TABLE users (
    id INTEGER
    email TEXT
    username TEXT
    password_hash TEXT
    PRIMARY KEY(id)
);


CREATE TABLE books (
    id INTEGER
    title TEXT
    author TEXT
    description TEXT
    -- store path to cover image
    cover TEXT
    PRIMARY KEY(id)
);


CREATE TABLE tags (
    book_id INTEGER
    tag TEXT
    FOREIGN KEY(book_id) REFERENCES books(id)
);


CREATE TABLE requests (
    user_id INTEGER
    book_id INTEGER
    status TEXT
    FOREIGN KEY(user_id) REFERENCES users(id)
    FOREIGN KEY(book_id) REFERENCES books(id)
)