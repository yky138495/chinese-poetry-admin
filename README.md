## requirements依赖安装
```
pip3 install -r requirements.txt
```

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

## Xadmin操作
```
python3 manage.py makemigrations xadmin    
python3  manage.py migrate xadmin
```

## 启动服务器
```
python3 manage.py runserver 0.0.0.0:8000

+ nohup 是linux命令，不挂断运行
nohup python manage.py runserver  0.0.0.0:8000
```

## 备注 JWT 和 Redis
可根据需求开启
```
JWT_AUTH = {
'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

CACHES = {
"default": {
"BACKEND": "django_redis.cache.RedisCache",
"LOCATION": "redis://127.0.0.1:6379",
"OPTIONS": {
"CLIENT_CLASS": "django_redis.client.DefaultClient",
}
}
}
```

## 目录结构

## 双数据库配置  settings.py
```
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db/tangshi.db'),
},
'database': {  # 配置第二个数据库节点名称
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db/songshi.db'),
},
}

DATABASE_APPS_MAPPING = {
'songshi': 'database',  # app名字: 数据库
'tangshi': 'default',  # app名字: 数据库
}
# 如果不设置 就是默认(default)的数据库

DATABASE_ROUTERS = ['poerty.database_router.DatabaseAppsRouter']
```

## API截图


## Xadmin后台截图


