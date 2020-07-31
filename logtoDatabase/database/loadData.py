import pymysql

"""
从数据库里拿取数据进行分析
"""
con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678',
    db='test',
    charset='utf8',
)


# 把选择数据展示的功能在这里实现，version_id确定你要选择一次的测试
# 返回的是一个二维矩阵
def load_data_from_database(version_id):
    cue = con.cursor()
    sql = "select * from records where version_id=" + str(version_id)
    try:
        cue.execute(sql)
        results = cue.fetchall()
        return results
    except Exception as e:
        print('Insert error:', e)
        con.rollback()
    else:
        con.commit()


# load_data_from_database(1)
