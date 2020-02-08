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

## 因Git有文件50M限制

唐诗和宋诗两个DB文件方百度云盘中共享(下载后迁移到对应目录)

tangshi.db 
链接: https://pan.baidu.com/s/19v37ylRPDg_hRLsLreghAg 提取码: n8bc

songshi.db 
链接: https://pan.baidu.com/s/1JpPEMAcZwSY_oMuwomkLoA 提取码: dkm9 

### 宋诗数据库地址
```
/chinese-poetry-admin/db/songshi.db 
```

### 唐诗数据库地址
```
/chinese-poetry-admin/db/tangshi.db 
```


PS：sqllite数据库查看工具
```
https://github.com/sqlitebrowser
```




## PyCharm CE版debug配置
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/9.png?raw=true)


## 目录结构
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/10.png?raw=true)

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

### API截图
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/1.png?raw=true)
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/2.png?raw=true)
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/3.png?raw=true)
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/4.png?raw=true)

### HTTP POST截图
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/5.png?raw=true)

## Xadmin后台截图
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/6.png?raw=true)
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/7.png?raw=true)
![](https://github.com/yky138495/chinese-poetry-admin/blob/master/img/8.png?raw=true)


