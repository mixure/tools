docker run -d -p 3307:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456 mysql:5.6
sleep 10  # 这个延时实在是...
docker exec -i mysql mysql -uroot -p123456<<EOF
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
flush privileges;
exit
EOF
