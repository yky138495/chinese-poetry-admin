
## Admin操作
创建超级账户：
```
python3 manage.py createsuperuser
yang001 ymg112233
```

## 反向生成Model
已有数据库生成models
```
manage.py inspectdb
python mysite/manage.py inspectdb > mysite/myapp/models.py
```

## settings.py
```
python3 manage.py migrate   # 创建表结构
python3 manage.py makemigrations tangshi  # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate TestModel   # 创建表结构
```

## 启动服务器
```
python3 manage.py runserver 0.0.0.0:8000
```
