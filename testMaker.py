import glob
import shutil
import os
from py_sub_class.AngStdPreis import LaTeXAng_Stdpr
import sqlite3
import pymysql.cursors

main_path = os.path.abspath(".")
# print(main_path)
out_dir = os.path.join(main_path, "testfolder")


# print(out_dir)


def test1():
    output_folder_name = 'testfolder'
    source_folder_name = 'sourcefolder'
    output_path_abs = os.path.join(os.path.abspath("."), output_folder_name)
    source_folder_abs = os.path.join(os.path.abspath("."), source_folder_name)
    if not os.path.exists(output_path_abs):
        """create the output file if its not existed"""
        os.makedirs(output_path_abs)
        print("{} is created".format(output_path_abs))
    else:
        print("{} is existed".format(output_path_abs))

    for file in glob.glob(os.path.join(source_folder_abs, "*")):
        shutil.copy2(file, output_path_abs)
        print("copy {} >>>>>>> {}".format(file, output_path_abs))


def test2():
    print("{} {} 123".format("1", "2"))


def test3():
    print(os.path.join(main_path, "sourcefolder/Angebot"))
    print(os.path.join(main_path, "sourcefolder/Angebot/RFFE_Angebot.tex"))


def test4():
    kdInfo = {
        'VN': "MuVN",
        'NN': "MusterNN",
        'Geschl': 'F',
        'FaA': "MusterFirmaname",
        'FaNErg': "MusterfirmanameErgänzung",
        'PLZ': '11001',
        'Anschr': "Musterstr.11",
        'St': "Musterstdt"
    }

    AngInfo = {
        'Bez': "TestAngBezeichnung",
        'Nr': "20210701",
        'Dat': "01.01.2077",
        'StdPr': "222,77",
        'GesStd': "888",
        'AblDat': "02.03.2088",
    }

    Absender = 'Absender'
    A = LaTeXAng_Stdpr(main_path, out_dir, AngInfo=AngInfo, kdInfo=kdInfo, Absender=Absender)
    A.compile_PDF()
    print(A)


def test5(dir):
    print(os.path.isfile(dir))


def test6():
    username = "contact_addresses"
    password = "Ht9gV@3Ff2*5-Q"
    con = sqlite3.connect("sqlite:////192.168.0.203:3306", uri=True)
    cur = con.cursor()
    statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():  # An empty result evaluates to False.
        print("Login failed")
    else:
        print("Welcome")


def test7():
    connection = pymysql.connect(host='192.168.0.203',
                                 user="contact_addresses",
                                 password="H+9gV@3Ff2*s-Q",
                                 database='contao',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 local_infile=True)
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM rffe_contact_addresses ORDER BY FirstName"
        cursor.execute(sql)
        # result = cursor.fetchone()
        result = cursor.fetchall()
        # for row in result:
        # print(row)
        print(result[0])
        print(result[0]["LastName"])


def test8():
    source_dir = "sourcefolder/Angebot"
    out_dir = "testfolder"
    for file in glob.glob(os.path.join(source_dir, "*")):
        shutil.copy2(file, out_dir)
        print("copy {} >>>>>>> {}".format(file, out_dir))


def test9():
    for file in glob.glob(os.path.join(source_dir, "*")):
        print(file)


def test10():
    source_dir = "sourcefolder/Angebot"
    path = os.path.abspath(os.path.join(os.path.dirname(source_dir), ".."))
    print(path)


test7()
