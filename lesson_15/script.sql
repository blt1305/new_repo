CREATE DATABASE shop;

CREATE TABLE customers(
  id   INT              NOT NULL AUTO_INCREMENT,
  name VARCHAR (20)     NOT NULL,
  age  INT              NOT NULL,
  address  CHAR (25) ,
  PRIMARY KEY (id)
);

CREATE TABLE orders (
  id int NOT NULL AUTO_INCREMENT,
  order_number int NOT NULL,
  customer_id int,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

ALTER TABLE orders DROP FOREIGN KEY customer_id;

insert into customers (name, age, address) values ('Semen', 33, 'Minsk, Street 1, 44');
insert into customers (name, age, address) values ('Ilya', 19, 'Minsk, Street 2, 46');
insert into customers (name, age, address) values ('Olga', 54, 'Minsk, Street 1, 48');
insert into customers (name, age, address) values ('Dana', 24, 'Minsk, Street 9, 22');
insert into customers (name, age, address) values ('Sergey', 34, 'Minsk, Street 9, 54');


insert into orders (order_number, customer_id, price) values (1234, 1, 23.3);
insert into orders (order_number, customer_id, price) values (1235, 2, 13);
insert into orders (order_number, customer_id, price) values (1236, 3, 555);
insert into orders (order_number, customer_id, price) values (1237, 5, 650);
insert into orders (order_number, customer_id, price) values (1238, 1, 34);
insert into orders (order_number, customer_id, price) values (1239, 2, 9.8);
insert into orders (order_number, customer_id, price) values (1241, 3, 7.5);
insert into orders (order_number, customer_id, price) values (1242, 5, 3.2);
insert into orders (order_number, customer_id, price) values (1243, 5, 5.6);
insert into orders (order_number, customer_id, price) values (1244, 5, 17.5);
insert into orders (order_number, customer_id, price) values (1245, 3, 90);
insert into orders (order_number, customer_id, price) values (1246, 5, 56);
insert into orders (order_number, customer_id, price) values (1247, 5, 63);
insert into orders (order_number, customer_id, price) values (1248, 1, 500);


SELECT * FROM customers JOIN orders ON customers.id = orders.customer_id;
SELECT * FROM customers LEFT JOIN orders ON customers.id = orders.customer_id;
SELECT c.id, c.name, o.price FROM customers as c LEFT JOIN orders as o ON c.id = o.customer_id;


SELECT c.id, c.name, o.price FROM customers as c LEFT JOIN orders as o ON c.id = o.customer_id WHERE o.price > 200;

SELECT c.id, c.name, SUM(o.price) FROM customers as c LEFT JOIN orders as o ON c.id = o.customer_id
GROUP BY c.id HAVING SUM(o.price) > 200;


select AVG(o.price), c.name from orders as o join customers as c on c.id = o.customer_id
group by c.id;


select avg(price) from orders;










