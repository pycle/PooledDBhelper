DBhelper
----------------------

This is a database tool class, do database link pool, support batch insert and query, based on PooledDB, code encapsulation, simplify the operation of development.

    # pool=PooledDBhelper({
    #     'host': '192.168.0.1',
    #     'user': 'username',
    #     'password': 'password',
    #     'port': 3306,
    #     'db': 'db_name'
    # })

    # data_list= [{"name":'a', 'info':'1'}, {"name":'b', 'info':'2'},{"name":'none', 'info':'3'}]
    # rows=pool.insert_many(data_list,"cy_self_test")
    # print(rows)

    # result_list=pool.task("select * from cy_self_test")
    # print(result_list)

    # query = "insert into `cy_self_test`({}) values {}".format("`name`,`info`", ("cy","world"))
    # pool.fetchone(query)

    # query="select  * from cy_self_test where id=1"
    # result=pool.fetchone(query)
    # print(result)