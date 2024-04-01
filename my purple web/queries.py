create = '''
CREATE TABLE IF NOT EXISTS users(
    first_name VARCHAR,
    last_name VARCHAR,
    years INTEGER,
    town VARCHAR,
    img VARCHAR,
    login VARCHAR,
    password VARCHAR
)
'''

insert = '''
INSERT INTO users (first_name, last_name, years, town, img, login, password)
VALUES
("Ekaterina", "Ivanova", 25, "Moscow", "https://img.razrisyika.ru/kart/122/1200/486715-samye-milye-36.jpg", "katya", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Pavel", "Petrov", 38, "Omsk", "https://proprikol.ru/wp-content/uploads/2022/10/kartinki-na-avatarku-dlya-parnej-i-muzhchin-68.jpg", "pav", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Anastasia", "Larionova", 28, "Kazan", "https://papik.pro/uploads/posts/2023-03/1677779928_papik-pro-p-krasivaya-kartinka-devushki-risunok-so-spi-40.jpg", "ana", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Vasilisa", "Shrek", 35, "Arkhangelsk", "https://gas-kvas.com/grafic/uploads/posts/2023-09/1695837147_gas-kvas-com-p-kartinki-shrek-2.jpg", "shrek", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Habar", "Babayka", 97, "Selo Vasyukovka", "https://coolsen.ru/wp-content/uploads/2021/11/24-20211122_174649.jpg", "habar", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Rodion", "Raskolnikov", 24, "St. Peterburg", "https://yt3.googleusercontent.com/a3RVwuDqDc9yX3YmAekF8fjlh9zFaVEv9eOZQdHDFmT3GaXvCoRHjwqub0Lwp9sdunkd4zXnwg=s900-c-k-c0x00ffffff-no-rj", "rodik", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Muravey", "AA", 100, "Moscow", "https://media.baamboozle.com/uploads/images/406717/1626364117_351951.jpeg", "muravey", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
("Krutoy", "Ahmed", 56, "Sochi", "https://kartinki.pics/uploads/posts/2022-12/1670634254_2-kartinkin-net-p-kartinki-kompyutera-dlya-detei-vkontakte-2.jpg", "ahmed", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b")
'''

drop = '''DROP TABLE IF EXISTS users'''