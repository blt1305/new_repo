create table users (
    id int not null AUTO_INCREMENT,
    username varchar(18) NOT NULL UNIQUE,
    password varchar(16) NOT NULL,
    PRIMARY KEY (id)
);

create table messages (
    id int not null AUTO_INCREMENT,
    text TEXT,
    created_at DATETIME,
    PRIMARY KEY (id)
);

create table user_messages (
    id int not null AUTO_INCREMENT,
    from_user INT NOT NULL,
    to_user INT NOT NULL,
    message_id INT NOT NULL,
	FOREIGN KEY (from_user) REFERENCES users(id),
    FOREIGN KEY (to_user) REFERENCES users(id),
    FOREIGN KEY (message_id) REFERENCES messages(id),
    PRIMARY KEY (id)
);


create table followers (
    id int not null AUTO_INCREMENT,
    user_id INT NOT NULL,
    follower_id INT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (follower_id) REFERENCES users(id),
    PRIMARY KEY (id)
);

insert into users (username, password) values ('Sergey', '12345');
insert into users (username, password) values ('Alesya', '12345');
insert into users (username, password) values ('Katya', '12345');

insert into messages (text, created_at) values ('Привет, как дела?', NOW());

insert into user_messages (from_user, to_user, message_id) values (1, 2, 1);
insert into user_messages (from_user, to_user, message_id) values (1, 3, 1);

SELECT *
FROM users u
JOIN user_messages um ON u.id = um.from_user
JOIN messages m ON um.message_id = m.id



