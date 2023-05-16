CREATE TABLE persons (
    person_id int  NOT NULL AUTO_INCREMENT,
    last_name varchar(255),
    first_name varchar(255) NOT NULL,
    age int default 18,
    sex varchar(5),
    address varchar(255),
    city varchar(255),
    PRIMARY KEY (person_id)
);

ALTER TABLE persons ADD created_at datetime;


INSERT INTO persons (first_name,last_name,created_at) VALUES ('Egor','Melnik', NOW());
INSERT INTO persons (first_name,last_name,created_at,address) VALUES ('Igor','Bubenchik', NOW(), 'Minsk');
INSERT INTO persons (first_name,last_name,created_at,address, age) VALUES ('Alex','Novak', NOW(), 'Paris', 31);
INSERT INTO persons (first_name,last_name,created_at,address, age) VALUES ('Kirill','Petrov', NOW(), 'Warsaw', 35);
INSERT INTO persons (first_name,last_name,created_at,address, age) VALUES ('Maria','Petrova', NOW(), 'Warsaw', 34);
INSERT INTO persons (first_name,last_name,created_at,address, age) VALUES ('Irina','Petrova', NOW(), 'Warsaw', 4);


