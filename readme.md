## App_id 

65f1d1e82d8e5b984f534734



CREATE TABLE User (
    serial_number INT AUTO_INCREMENT PRIMARY KEY,
    id VARCHAR(255) ,
    title VARCHAR(50),
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    gender VARCHAR(255),
    email VARCHAR(255),
    dateOfBirth DATE,
    registerDate VARCHAR(255),
    phone VARCHAR(20),
    picture VARCHAR(255),
    street VARCHAR(100),
    city VARCHAR(30),
    state VARCHAR(30),
    country VARCHAR(30),
    timezone VARCHAR(20)
);