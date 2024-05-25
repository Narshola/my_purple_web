create_users = '''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    years INTEGER,
    town VARCHAR,
    img VARCHAR,
    login VARCHAR,
    password VARCHAR
)
'''

create_chat = '''
CREATE TABLE chat (
    user_id            INTEGER  REFERENCES users (id),
    msg_user           TEXT,
    msg_user_time      DATETIME,
    to_user_id         INTEGER  REFERENCES users (id),
    msg_from_user      TEXT,
    msg_from_user_time DATETIME,
    msg_has_seen       BOOLEAN  DEFAULT (FALSE) 
);

'''

insert_users = '''
INSERT INTO users (first_name, last_name, years, town, img, login, password)
VALUES
("Василиса", "Шрек", 65, "Архангельск", "https://gas-kvas.com/grafic/uploads/posts/2023-09/1695837147_gas-kvas-com-p-kartinki-shrek-2.jpg", "shrek", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Хабар", "Бабайка", 97, "Село Васюковка", "https://coolsen.ru/wp-content/uploads/2021/11/24-20211122_174649.jpg", "habar", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Родион", "Раскольников", 24, "Санкт-Петербург", "https://yt3.googleusercontent.com/a3RVwuDqDc9yX3YmAekF8fjlh9zFaVEv9eOZQdHDFmT3GaXvCoRHjwqub0Lwp9sdunkd4zXnwg=s900-c-k-c0x00ffffff-no-rj", "rodik", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Муравей", "А А", 100, "Москва", "https://media.baamboozle.com/uploads/images/406717/1626364117_351951.jpeg", "muravey", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Крутой", "Ахмед", 56, "Сочи", "https://kartinki.pics/uploads/posts/2022-12/1670634254_2-kartinkin-net-p-kartinki-kompyutera-dlya-detei-vkontakte-2.jpg", "ahmed", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Штука", "Непонятная", 87, "Ыб", "https://cdn.culture.ru/images/af9de8fe-3393-5281-8915-81d3420e322e", "shtuka", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b")
'''

new_insert = '''INSERT INTO users (first_name, last_name, years, town, img, login, password) VALUES (?, ?, ?, ?, ?, ?, ?)'''

msg_data = '''SELECT * FROM chat WHERE user_id = ? AND to_user_id = ?'''
chat_insert = '''INSERT INTO chat (user_id, to_user_id, msg_user, msg_user_time, msg_has_seen) VALUES (?, ?, ?, ?, TRUE)'''
to_chat_insert = '''INSERT INTO chat (user_id, to_user_id, msg_from_user, msg_from_user_time) VALUES (?, ?, ?, ?)'''
get_new_msg = '''SELECT * FROM chat WHERE user_id=? AND msg_has_seen=FALSE'''


login_data = '''SELECT * FROM users WHERE login = ?'''
id_data = '''SELECT * FROM users WHERE id = ?'''

drop_users = '''DROP TABLE IF EXISTS users'''
drop_chat = '''DROP TABLE IF EXISTS chat'''