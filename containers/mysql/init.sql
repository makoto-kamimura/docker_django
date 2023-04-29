-- MYSQL_USERに権限を付与
-- 今回はdjangoというユーザを指定
GRANT ALL PRIVILEGES ON *.* TO 'django'@'%';
FLUSH PRIVILEGES;