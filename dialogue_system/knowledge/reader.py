# -*- coding: utf-8 -*-
import os
import yaml
import re
import sqlite3
import MeCab

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

def read_condition(text):
    def analyze(pos, words, point, score, number):
        for i in pos:
            cnt = 0
            for j in words:
                if i == j:
                    score += float(point[cnt])
                    number += 1
                cnt += 1
        return score, number
    nounswords, verbswords, adjswords, advswords = [], [], []    , []
    nounspoint, verbspoint, adjspoint, advspoint = [], [], []    , []
    count = {'名詞':[],'動詞':[],'形容詞':[],'副詞':[]}

    with open(os.path.join(BASE_DIR, 'pn_ja.dic.txt'))as f:
        for line in f:
            line = line.rstrip()
            x = line.split(':')
            if abs(float(x[3]))>0:
                if x[2] == '名詞':
                    nounswords.append(x[0])
                    nounspoint.append(x[3])
                if x[2] == '動詞':
                    verbswords.append(x[0])
                    verbspoint.append(x[3])
                if x[2] == '形容詞':
                    adjswords.append(x[0])
                    adjspoint.append(x[3])
                if x[2] == '副詞':
                    advswords.append(x[0])
                    advspoint.append(x[3])
    tagger = MeCab.Tagger()
    p = r'[\t,]'
    tmp = [re.split(p,x) for x in tagger.parse(text).split('\    n')]
    tokens = [tuple([y for i, y in enumerate(x) if i in [1,7]    ]) for x in tmp if len(x)>3]
    pos_dic = {'名詞':[],'動詞':[],'形容詞':[],'副詞':[]}
    for (pos, surface) in tokens:
        if pos in pos_dic.keys():
            pos_dic[pos].append(surface)
    score = number = 0
    score,number = analyze(pos_dic['名詞'],nounswords,nounspoint,score, number)
    score,number = analyze(pos_dic['動詞'],verbswords,verbspoint,score, number)
    score,number = analyze(pos_dic['形容詞'],adjswords,adjspoint,score, number)
    score,number = analyze(pos_dic['副詞'],advswords,advspoint,score, number)
    if number > 0:
        avg_score = score / number
        if avg_score < -0.3:
            return 'LOW'
        elif -0.3 <= avg_score <= 0.3:
            return 'NEUTRAL'
        elif avg_score > 0.3:
            return 'HIGH'
        else:
            return ''
    else:
        return ''

    return 

