rm -rf src
tar -xzvf src.tar.gz
cd src
docker-compose down
docker-compose build
docker-compose up