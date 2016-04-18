#encoding:utf8
import pymysql
import traceback

class Models:
    def __init__(self,host='vol55vif.zzcdb.dnstoo.com',username='exq7oo5s_f',password='exq7oo5s',database='exq7oo5s',port=5506,charset='utf8'):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        try:
            self.conn = pymysql.connect(host,username,password,database,port,charset)
            if len(self.query('SHOW TABLES LIKE "PY_Post"')) < 1 :
                self.creattable()
            elif len(self.query('SHOW TABLES LIKE "PY_Users"')) < 1 :
                self.creattable()
            elif len(self.query('SHOW TABLES LIKE "PY_Catalogue"')) < 1 :
                self.creattable()
            elif len(self.query('SHOW TABLES LIKE "PY_Comments"')) < 1 :  
                self.creattable()
        except:
            traceback.print_exc()

    def __del__(self):
        try:
            self.conn.close()
        except:
            traceback.print_exc()

    def query(self,sql):
        try:
          cur = self.conn.cursor()
          cur.execute('SET NAMES UTF8')
          cur.execute(sql)
          data = cur.fetchall()
          cur.close()
          return data         #返回结果集
        except:
          traceback.print_exc()

    def exe(self,sql):
        try:
          cur = self.conn.cursor()
          cur.execute('SET NAMES UTF8')
          cul= cur.execute(sql)
          self.conn.commit()
          cur.close()
          return cul          #返回受影响的行数
        except:
          traceback.print_exc()

    def creattable(self):
        try:
            sql1 = 'DROP TABLE IF EXISTS `PY_Comments`;\
            DROP TABLE IF EXISTS `PY_Post`;\
            DROP TABLE IF EXISTS `PY_Users`;\
            DROP TABLE IF EXISTS `PY_Catalogue`;'
            sql2 = 'create table `PY_Users` (\
            `UId` varchar(50) NOT NULL,\
            `UPassword` varchar(50) NOT NULL,\
            PRIMARY KEY(`UId`)\
            )DEFAULT CHARSET = utf8;'
            sql3 = 'create table `PY_Catalogue` (\
            `CaId` int(4) NOT NULL AUTO_INCREMENT,\
            `CaName` varchar(50) NOT NULL,\
            PRIMARY KEY(`CaId`)\
            )DEFAULT CHARSET = utf8;'
            sql4 = 'create table `PY_Post` (\
            `PId` int(4) NOT NULL AUTO_INCREMENT,\
            `PTitle` varchar(255),\
            `Date` datetime NOT NULL,\
            `PContent` text NOT NULL,\
            `CaId` int(4) NOT NULL,\
            PRIMARY KEY(`PId`),\
            FOREIGN KEY(`CaId`) REFERENCES PY_Catalogue(`CaId`)\
            )DEFAULT CHARSET = utf8;'
            sql5 = 'create table `PY_Comments` (\
            `CoId` int(4) NOT NULL AUTO_INCREMENT,\
            `PId` int(4) NOT NULL,\
            `UId` varchar(50) NOT NULL,\
            `Date` datetime NOT NULL,\
            `CoContent` text NOT NULL,\
            PRIMARY KEY(`CoId`),\
            FOREIGN KEY(`PId`) REFERENCES PY_Post(`PId`),\
            FOREIGN KEY(`UId`) REFERENCES PY_Users(`UId`)\
            )DEFAULT CHARSET = utf8;'
            self.exe(sql1) #删除表
            print('删除表')
            self.exe(sql2) #创建表
            print('create PY_Users')
            self.exe(sql3) #创建表
            print('create PY_Catalogue')
            self.exe(sql4) #创建表
            print('create PY_Post')
            self.exe(sql5) #创建表
            print('create PY_Comments')
        except:
            traceback.print_exc()

    #根据PId查所有信息(文章，评论,文章列表)
    def selectAll(self,Id,IdName,TABLE):
        sql ='select * from ' + TABLE + ' where ' +  IdName + ' = ' + str(Id) + ' order by date Desc'
        return self.query(sql)

    #根据CaId查文章的ID和相应的title
    def selectPT(self,Id):
        sql ='select `PId`,`PTitle` from  PY_Post  where  CaId = ' + str(Id)   
        return self.query(sql)

    #查询所有目录,评论,文章
    def selectA(self,TABLE):
        sql = 'select * from '+ TABLE
        return self.query(sql)


if __name__ == '__main__':
    mode = Models()
    print('success')
    print(mode.selectAll('1','PId','PY_Post'))
    print(mode.selectAll('1','PId','PY_Comments'))
    print(mode.selectAll('1','CaId','PY_Post'))
    print(mode.selectCa())
    print(mode.selectPT('1'))