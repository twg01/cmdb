# Python3
import pymysql

class MySQLHelper:
    def __init__(self, host, user, password, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.timeout = 10
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password,
                                        charset=self.charset,connect_timeout=self.timeout)
            self.cursor = self.conn.cursor()
        except pymysql.Error as e:
            print('MySql Error : %d %s' % (e.args[0], e.args[1]))

    def setDB(self, db):
        try:
            self.conn.select_db(db)
        except pymysql.Error as e:
            print('MySql Error : %d %s' % (e.args[0], e.args[1]))

    def query(self, sql):
        try:
            rows = self.cursor.execute(sql)
            return rows
        except pymysql.Error as e:
            print('MySql Error: %s SQL: %s' % (e, sql))

    def queryRow(self, sql):
        try:
            self.query(sql)
            result = self.cursor.fetchone()
            desc = self.cursor.description
            row = {}
            for i in range(0, len(result)):
                row[desc[i][0]] = result[i]
            return row
        except pymysql.Error as e:
            print('MySql Error: %s SQL: %s' % (e, sql))

    def queryAll(self, sql):
        try:
            self.query(sql)
            result = self.cursor.fetchall()
            desc = self.cursor.description
            rows = []
            for cloumn in result:
                row = {}
                for i in range(0, len(cloumn)):
                    row[desc[i][0]] = cloumn[i]
                rows.append(row)
            return rows
        except pymysql.Error as e:
            print('MySql Error: %s SQL: %s' % (e, sql))

    def insert(self, tableName, pData):
        try:
            newData = {}
            for key in pData:
                newData[key] = "'" + pData[key] + "'"
            key = ','.join(newData.keys())
            value = ','.join(newData.values())
            sql = "insert into " + tableName + "(" + key + ") values(" + value + ")"
            self.query("set names 'utf8'")
            self.query(sql)
            self.commit()
        except pymysql.Error as e:
            self.conn.rollback()
            print('MySql Error: %s %s' % (e.args[0], e.args[1]))
        finally:
            self.close()

    def update(self, tableName, pData, whereData):
        try:
            newData = []
            keys = pData.keys()
            for i in keys:
                item = "%s=%s" % (i, "'" + pData[i] + "'")
                newData.append(item)
            items = ','.join(newData)
            newData2 = []
            keys = whereData.keys()
            for i in keys:
                item = "%s=%s" % (i, "'" + whereData[i] + "'")
                newData2.append(item)
            whereItems = " AND ".join(newData2)
            sql = "update " + tableName + " set " + items + " where " + whereItems
            self.query("set names 'utf8'")
            self.query(sql)
            self.commit()
        except pymysql.Error as e:
            self.conn.rollback()
            print('MySql Error: %s %s' % (e.args[0], e.args[1]))
        finally:
            self.close()

    def getLastInsertRowId(self):
        return self.cursor.lastrowid

    def getRowCount(self):
        return self.cursor.rowcount

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    conn = MySQLHelper("192.168.3.130","root","root")
    conn.setDB("test")
    result = conn.queryAll("select * from emp;")
    for item in result:
        print(item)