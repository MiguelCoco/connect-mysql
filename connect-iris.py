import pymysql.cursors
#连接数据库iris
connection = pymysql.connect(host='localhost',
							user='root',
							password='***************',
							db='iris',
							charset='utf8mb4',
							cursorclass=pymysql.cursors.DictCursor,)
try:

	with connection.cursor() as cursor:
		sql = 'select `*` from `iris` where `id` in (%s,%s)'
		cursor.execute(sql,('100','99'))
		result=cursor.fetchall()
		#遍历列表提取sepal_length值
		for i in range(2):	
			sepal_length = result[i]['sepal_length']
			print(sepal_length)
finally:
	connection.close()
