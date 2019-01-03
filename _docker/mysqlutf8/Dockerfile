from mysql:5.6
COPY my.cnf /etc/mysql/conf.d/mysqlutf8.cnf
COPY ./grant_root_remote_visit.sql /docker-entrypoint-initdb.d
ENV MYSQL_ROOT_PASSWORD 123qwe 
CMD ["mysqld", "--character-set-server=utf8", "--collation-server=utf8_unicode_ci"]
