#! /bin/bash

echo
echo "=============== Dropping databases ==============="
mysql -uroot -e "drop database test_main"
mysql -uroot -e "drop database test_accounts"
mysql -uroot -e "drop database test_shard1"
mysql -uroot -e "drop database test_shard2"

echo
echo "=============== Creating databases ==============="
mysql -uroot -e "create database test_main"
mysql -uroot -e "create database test_accounts"
mysql -uroot -e "create database test_shard1"
mysql -uroot -e "create database test_shard2"

echo
echo "=============== syncing default ==============="
python manage.py syncdb --noinput

echo
echo "=============== syncing accounts ==============="
python manage.py syncdb --noinput --database=accounts

echo
echo "=============== syncing shard1 ==============="
python manage.py syncdb --noinput --database=shard1

echo
echo "=============== syncing shard2 ==============="
python manage.py syncdb --noinput --database=shard2

echo
echo "Creating superuser"
python manage.py createsuperuser --username=admin --email=admin@example.com

echo "Finish"
