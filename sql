pymysql.connect('vol55vif.zzcdb.dnstoo.com','exq7oo5s_f','exq7oo5s','exq7oo5s',5506,'utf8')

DROP TABLE IF EXISTS PY_Comments;
DROP TABLE IF EXISTS PY_Post;
DROP TABLE IF EXISTS PY_Users;
DROP TABLE IF EXISTS PY_Catalogue;

create table `PY_Users` (
`UId` varchar(50) NOT NULL,
`UName` varchar(50) NOT NULL,
`UPassword` varchar(50) NOT NULL,
PRIMARY KEY(`UId`)
)DEFAULT CHARSET = utf8;

create table `PY_Catalogue` (
`CaId` int(4) NOT NULL AUTO_INCREMENT,
`CaName` varchar(50) NOT NULL,
PRIMARY KEY(`CaId`)
)DEFAULT CHARSET = utf8;

create table `PY_Post` (
`PId` int(4) NOT NULL AUTO_INCREMENT,
`PTitle` varchar(255),
`PDate` datetime NOT NULL,
`PContent` text NOT NULL,
`CaId` int(4) NOT NULL,
PRIMARY KEY(`PId`),
FOREIGN KEY(`CaId`) REFERENCES PY_Catalogue(`CaId`)
)DEFAULT CHARSET = utf8;

create table `PY_Comments` (
`CoId` int(4) NOT NULL AUTO_INCREMENT,
`PId` int(4) NOT NULL,
`UId` varchar(50) NOT NULL,
`CoDate` datetime NOT NULL,
`CoContent` text NOT NULL,
PRIMARY KEY(`CoId`),
FOREIGN KEY(`PId`) REFERENCES PY_Post(`PId`),
FOREIGN KEY(`UId`) REFERENCES PY_Users(`UId`)
)DEFAULT CHARSET = utf8;


py_catalogue
insert into py_catalogue(CaName) values('测试');
insert into py_catalogue(CaName) values('测试');
insert into py_catalogue(CaName) values('测试');
insert into py_catalogue(CaName) values('测试');

py_post
insert into py_post(PTitle,PDate,PContent,CaId) values('测试','2015-12-13 24:00:00','nihaoslkdflalad<h1>你好</h1>','1');
insert into py_post(PTitle,PDate,PContent,CaId) values('测试','2015-12-13 24:00:00','nihaoslkdflalad<h1>你好</h1>','1');

py_users
insert into py_users(UId,UName,UPassword) values('1173507862@qq.com','测试','wangkaijin');

py_comments
insert into py_comments(PId,UId,CoDate,CoContent) values('4','1173507862@qq.com','2015-12-13 4:20:00','这是测试的评论<h1>你好</h1>');
insert into py_comments(PId,UId,CoDate,CoContent) values('4','1173507862@qq.com','2015-12-13 4:20:00','这是测试的评论<h1>你好</h1>');
insert into py_comments(PId,UId,CoDate,CoContent) values('4','1173507862@qq.com','2015-12-13 4:20:00','这是测试的评论<h1>你好</h1>');