'''
 -*- coding: utf-8 -*-
 @Time : 18-11-13 下午5:18
 @Author : SamSa
 @Site : 
 @File : insert_city.py
 @Software: PyCharm
 @Statement:初始化将字母和城市插入数据库
'''
import json
import pymysql
'''
将城市信息爬取并插入数据库
'''


'''将城市首字母插入'''
def insert_letter():
    con = pymysql.connect(host='localhost',user='root',password='124816',port=3306,charset='utf8',database='Tpp')
    print(con)
    cur = con.cursor()
    '''打开json文件解析'''
    with open('cities.json') as fp:
        info = json.load(fp).get('returnValue')
    letters = info.keys()
    '''插入语句'''
    try:
        for letter in letters:
            sql = 'insert into letter (letter) values ("{}")'.format(letter)
            cur.execute(sql)
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        con.close()


def insert_cities():
    con = pymysql.connect(host='127.0.0.1',password='124816',database='Tpp',port=3306,charset='utf8',user='root')
    cur = con.cursor()
    with open('cities.json') as fp:
        info = json.load(fp).get('returnValue')
        try:
            for letter in info:
                citiesList = info.get(letter)
                for temp in citiesList:
                    id = temp.get('id')
                    parentId = temp.get('parentId')
                    regionName = temp.get('regionName')
                    cityCode = temp.get('cityCode')
                    pinYin = temp.get('pinYin')
                    print('{}\t{}\t{}\t{}\t{}'.format(id,parentId,regionName,cityCode,pinYin))
                    '''查询外键'''
                    sql1 = 'select * from letter where letter="{}"'.format(letter)
                    cur.execute(sql1)
                    letter_id = cur.fetchone()[0]
                    print(letter_id,type(letter_id))
                    '''插入至cities表'''
                    sql2 = 'insert into cities (id,parentId,regionName,cityCode,pinYin,letter_id) values ("{}","{}","{}","{}","{}","{}")'.format(id,parentId,regionName,cityCode,pinYin,letter_id)
                    cur.execute(sql2)
                    con.commit()
                    print(letter_id)
        except Exception as e:
            print(e)
            con.rollback()
        finally:
            con.close()

if __name__ == '__main__':
    # pass
    # insert_letter()
    insert_cities()