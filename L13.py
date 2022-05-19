from peewee import *

db = MySQLDatabase("lesson", user="root", password="A123BC%xyRW", host="localhost")
#print(db)

# SELECT example1.Cat, example1.Part, example2.Cat_name,
# example2.Price FROM example1 INNER JOIN example2 ON
# example1.Cat = example2.Cat_id;
#вот сам запрос


class BaseModel(Model):
    class Meta:
        database = db


class Example2(BaseModel):
    Cat_id = IntegerField()
    Cat_name = CharField(20)
    Price = FloatField()


class Example1(BaseModel):
    Part_id = IntegerField(PrimaryKeyField)
    Part = CharField()
    Cat = IntegerField()


data = [
    (10, "Стройматериалы", 105.00),
    (505, "Недвижимость", 210.00),
    (205, "Транспорт", 160.00),
    (30, "Мебель", 77.0),
    (45, "Техника", 65.00)
]
data_2 = [

    (1, "Квартиры", 505),
    (2, "Автомашины", 205),
    (3, "Доски", 10),
    (4, "Шкафы", 30),
    (5, "Книги", 160)
 ]


# Example2.create_table()
# Example2.insert_many(data, fields=[Example2.Cat_id, Example2.Cat_name, Example2.Price]).execute()
# print('Done')
# Example1.create_table()
# Example1.insert_many(data_2, fields=[Example1.Part_id, Example1.Part, Example1.Cat])


def connect(name_db, user_name, user_password, user_host):
    try:
        db = MySQLDatabase(database=name_db, user=user_name, password=user_password, host=user_host)
        database = db
        query = (Example1.select().join(Example2, on=(Example1.Cat == Example2.Cat_id)))
        for Example in query:
            print(Example.Cat, Example.Part)
    except ConnectionError as ex:
        print(ex)
        print('Something went wrong.')


connect(name_db='lesson', user_name='root', user_password='A123BC%xyRW', user_host='localhost')

#Example2.drop_table()
#Example1.drop_table()
# from peewee import *
# db = MySQLDatabase("lesson", user="root", password="A123BC%xyRW", host="localhost")
#
#
# class BaseModel(Model):
#     class Meta:
#         db = Database
#
#

#
#
# Example1.create_table()
# Example1_1 = Example1(1, "Мебель", 330)
# Example1_1.save()
#
# data1 = [
#
#     (1, "Квартиры", 505),
#     (2, "Автомашины", 205),
#     (3, "Доски", 10),
#     (4, "Шкафы", 30),
#     (5, "Книги", 160)
# ]
# # Table1_1 = Table1(1, "Мебель", 330)
#
# #Table1.create_table()
#Table1.insert_many(data1, fields=[Table1.Part_id, Table1.Part, Table1.Cat]).execute()

# EX1 = Example1(Part_id=1, Part='мебель', Cat=400)
# Example1.create_table()
# EX1.save()
# Example1.drop_table()
# ex2 = Example2(Cat_numb=10, Cat="Стройматериалы", Price=105.00)
# ex2.save()