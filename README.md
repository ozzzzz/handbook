# handbook

## Установка elastic search

```
mkdir elasticdata
docker pull docker.elastic.co/elasticsearch/elasticsearch:6.4.0
docker run -dit --name elastic -p 9200:9200 -p 9300:9300 -v <path_to_elasticdata>:/usr/share/elasticsearch/data -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.4.0
```

## Заливка

В скрипте `uploader.py` указываем:
  * путь до файла со списком объектов;
  * путь и тип