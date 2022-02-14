import sqlite3
conn = sqlite3.connect("stt_vnm.db")
c = conn.cursor()

# c.execute("PRAGMA foreign_keys = ON")

# ========== table users =======
# c.execute('''create table users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL,
#     password TEXT UNIQUE NOT NULL,
#     description TEXT
# ) ''')
# c.execute("insert into users(username, password, description) values('Nguyen Huyen Trang','trangshin','học viên')")
c.execute("select * from users")
print(c.fetchall())
# ========== table classes =======
# c.execute(''' create table classes(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     className TEXT UNIQUE NOT NULL,
#     description TEXT
# )
# ''')

# ========== table students =======
# c.execute('''create table students(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     studentCode TEXT UNIQUE NOT NULL,
#     studentName TEXT NOT NULL,
#     userId INT,
#     classId INT,
#     description TEXT,
#     FOREIGN KEY(userId) REFERENCES users(id),
#     FOREIGN KEY(classId) REFERENCES classes(id) 
# )''')

# ========== table teachers =======
# c.execute('''create table teachers(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      teacherCode TEXT UNIQUE NOT NULL,
#      teacherName TEXT NOT NULL,
#      userId INT,
#      classId INT,
#      description TEXT,
#      FOREIGN KEY(userId) REFERENCES users(id),
#      FOREIGN KEY(classId) REFERENCES classes(id)
# )''')

# ========== table studentTest_relationship =======
# c.execute(''' create table studentTest_rela(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      classTestRela_id INTEGER,
#      studentId INTEGER, 
#      mark REAL,
#      description TEXT,
#      FOREIGN KEY(classTestRela_id) REFERENCES classes(id),
#      FOREIGN KEY(studentId) REFERENCES students(id)
# )
# ''')

# ========== table questionLibrary =======
# c.execute(''' create table quetionsLib(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      content NOT NULL,
#      studentId INTEGER, 
#      level INTEGER NOT NULL,
#      teacherId INTEGER,
#      description TEXT,
#      FOREIGN KEY(studentId) REFERENCES students(id),
#      FOREIGN KEY(teacherId) REFERENCES teachers(id)
# )
# ''')

# ========== table testType =======
# c.execute(''' create table testType(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      typeName TEXT NOT NULL,
#      description TEXT
# )''')

# ========== table examination =======
# c.execute('''create table examination(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      testName TEXT NOT NULL,
#      testType_id INTEGER,
#      teacherId INTEGER,
#      description TEXT,
#      FOREIGN KEY(testType_id) REFERENCES testType(id),
#      FOREIGN KEY(teacherId) REFERENCES teachers(id)
# )''')

# ========== table questionsExamRelationship =======
# c.execute('''create table questionsExam_Rela(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     quesId INTEGER,
#     examId INTEGER,
#     description TEXT,
#     FOREIGN KEY(quesId) REFERENCES questionsLib(id),
#     FOREIGN KEY(examId) REFERENCES examinations(id)
# )''')

# ========== table category =======
# c.execute('''create table category(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      categoryName TEXT NOT NULL,
#      description TEXT
# )''')

# ========== table questions =======
# c.execute(''' create table quetions(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      content TEXT NOT NULL,
#      categoryId INTEGER,
#      level INTEGER NOT NULL,
#      description TEXT,
#      FOREIGN KEY(categoryId) REFERENCES category(id)
# )''')
 
conn.commit()
conn.close()