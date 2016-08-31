# -*- coding: utf-8 -*-
import os
import yaml
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_names():
    file_path = os.path.join(BASE_DIR, 'names.txt')
    with open(file_path, 'rb') as f:
        names = [name.decode('utf-8').strip() for name in f]
    return names

def read_private_comment_from_tutor(name):
    if name == '':
        return ''
    file_path = os.path.join(BASE_DIR, 'knowledge.sqlite3')
    conn = sqlite3.connect(file_path)
    c = conn.cursor()
    
    comment = ''
    c.execute("""SELECT id FROM student WHERE name LIKE ?;""",(name+'%',))
    student_id = c.fetchone()
    if student_id == None:
        c.close()
        conn.close()
        return comment
    c.execute("""SELECT comment FROM tutor_comment WHERE id = ? AND is_listened = 0;""",student_id)
    comment = c.fetchone()[0]
    if comment == None:
        comment = ''
    c.close()
    conn.close()
    return comment

def read_class_comment_from_teacher(name):
    if name == '':
        return ''
    file_path = os.path.join(BASE_DIR, 'knowledge.sqlite3')
    conn = sqlite3.connect(file_path)
    c = conn.cursor()

    c.execute("""SELECT id FROM student WHERE name LIKE ?;""",(name+'%',))
    student_id = c.fetchone()[0]

    c.execute("""SELECT fk_class FROM student_belong_to_class WHERE fk_student = ?;""",(student_id,))
    class_ids = [i[0] for i in c.fetchall() if i != None]

    comments = []
    for class_id in class_ids:
        print(class_id)
        c.execute("""SELECT fk_teacher FROM class WHERE id = ?;""",(class_id,))
        teacher_id = c.fetchone()[0]
        c.execute("""SELECT name FROM teacher WHERE id = ?;""",(teacher_id,))
        teacher = c.fetchone()[0]
        c.execute("""SELECT comment FROM class_comment WHERE fk_class = ? AND is_listened = 0 ORDER BY created_at DESC;""",(class_id,))
        comment = c.fetchone()
        if comment != None:
            comments.append((teacher,comment[0])) 
    c.close()
    conn.close()
    return comments
