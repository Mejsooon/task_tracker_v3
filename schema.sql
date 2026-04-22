CREATE TABLE users (
    id          VARCHAR(10)  PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    username    VARCHAR(50)  NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL
);

CREATE TABLE tasks (
    id                VARCHAR(10)  PRIMARY KEY,
    user_id           VARCHAR(10)  NOT NULL,
    difficulty        SMALLINT     NOT NULL CHECK (difficulty BETWEEN 1 AND 10),
    description       TEXT         NOT NULL,
    additional_notes  TEXT,
    status            VARCHAR(20)  NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'completed')),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO users (id, name, username, password)
VALUES ('U001', 'Jan Kowalski', 'user1', '$2b$12$loGljvDW3fQR8fSpjRJ3wuECETjbQZEiF7uDPq0pO2F6wZtKltkw6');