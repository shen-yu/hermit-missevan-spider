# hermit-missevan-spider

> 爬取猫耳FM的音频到数据库，配合 `wp_hermit` 插件自用

## Usage

```python
pip install -r requirements.txt
```

在根目录新建一个 `config.py` 文件，在里面填写数据库信息

```python
host = "#"
port = 3306
user = "#"
password = "#"
database = "#"
```

然后运行

```python
python main.py musicId
```