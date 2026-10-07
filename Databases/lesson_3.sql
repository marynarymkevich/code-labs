PRAGMA foreign_keys = ON;

CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE instruments (
    instrument_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE teacher_instruments (
    teacher_id INTEGER REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    instrument_id INTEGER REFERENCES instruments(instrument_id) ON DELETE CASCADE,
    PRIMARY KEY (teacher_id, instrument_id)
);

CREATE TABLE lessons (
    lesson_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    room TEXT NOT NULL,
    teacher_id INTEGER REFERENCES teachers(teacher_id),
    student_id INTEGER REFERENCES students(student_id),
    instrument_id INTEGER REFERENCES instruments(instrument_id)
);