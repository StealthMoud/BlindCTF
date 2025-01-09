USE blind_ctf;

DROP TABLE IF EXISTS flags;
DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    status ENUM('available', 'not available')
);

INSERT INTO items (name, status) VALUES
('Item 1', 'available'),
('Item 2', 'not available'),
('Item 3', 'available');

CREATE TABLE flags (
    id INT PRIMARY KEY,
    flag TEXT NOT NULL
);

INSERT INTO flags (id, flag) VALUES
(1, 'FLAG{random_flag_item_1}'),
(3, 'FLAG{random_flag_item_3}');
