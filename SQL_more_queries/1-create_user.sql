-- creates the user user_0d_1 with all privileges
CREATE USER
    IF NOT EXISTS 'user''@localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVLIGES
    ON *.*
    TO 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVLIGES