import psycopg2
import requests as rq
from requests.exceptions import Timeout, ConnectionError
import schedule
import datetime


def api():
    url = 'http://c2-178-216-98-50.elastic.cloud.croc.ru:9721/ptzrestapi/states'

    try:
        response = rq.get(url=url)
        result = response.json()
        s=1
        lst_1 = []
        for n in result:
            demo_lst = []
            demo_lst.append(s)
            demo_lst.append(n.get('BType'))
            demo_lst.append(n.get('Counter1'))
            demo_lst.append(n.get('Counter2'))
            demo_lst.append(n.get('Counter3'))
            lst_1.append(demo_lst)
            s += 1
        return lst_1
    except Timeout:
        print('Ошибка таймаута')
    except  ConnectionError:
        print('Ошибка соединения')
        
lst2 = api()


def check():
    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    global lst2
    if lst2 == api():
        print(f'Все окей, обновлений нет')
    else:
        lst3 = lst2
        lst2 = api()
        try:
            connection = psycopg2.connect(
                            dbname="PTZ_db",
                            user="superuser",
                            password="Qwerty123!",
                            host="127.0.0.1",
                            port="5432",)
            cursor = connection.cursor()

            for n in lst2:
                update_query = f"""Update backend_buttons set ("Btype", "Counter1", "Counter2", "Counter3"
                        ) = ({n[1]}, {n[2]}, {n[3]}, {n[4]}) where id = {n[0]}"""
                cursor.execute(update_query)
                connection.commit()

            cursor.execute("""SELECT * from backend_buttons""")
            result = cursor.fetchall()
            print(result)
            print("Все обновлено")

            s = 0

            for n in result:
                if n[1] == 3:
                    if lst3[s][1] != n[1]:
                        if n[0] == 1:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№1', null, '{now}', null, null);
                                            INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№15', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                        
                        elif n[0] == 2:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№2', null, '{now}', null, null);
                                            INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№3', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1  
                            
                        elif n[0] == 3:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№16', null, '{now}', null, null);
                                            INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№17', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1 
                            
                        elif n[0] == 4:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№4', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1 
                            
                        elif n[0] == 5:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№18', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1 
                            
                        elif n[0] == 6:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№5', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1 
                            
                        elif n[0] == 7:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№19', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1 
                            
                        elif n[0] == 8:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№6', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1 
                            
                        elif n[0] == 9:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№20', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1 
                            
                        elif n[0] == 10:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№7', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1 
                            
                        elif n[0] == 11:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id")) VALUES ('№21', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1 
                            
                        elif n[0] == 12:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№8', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                            
                        elif n[0] == 13:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№22', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                            
                        elif n[0] == 14:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№9', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                            
                        elif n[0] == 15:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№23', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                            
                        elif n[0] == 16:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№10', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                            
                        elif n[0] == 17:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№24', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                            
                        elif n[0] == 18:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№11', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                            
                        elif n[0] == 19:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№25', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                            
                        elif n[0] == 20:
                            print(f'Внимание! Произошел инцидент!!!')
                            query = f"""INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№12', null, '{now}', null, null);
                                            INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№13', null, '{now}', null, null);
                                            INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№14', null, '{now}', null, null);
                                            INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№26', null, '{now}', null, null);
                                            INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№27', null, '{now}', null, null);
                                            INSERT INTO backend_accidents ("Post", "Description", "FixTime", "EndTime", "Type_id") VALUES ('№28', null, '{now}', null, null)"""
                            cursor.execute(query)
                            connection.commit()
                            print(n[1])
                            s += 1
                            
                    else:
                        s += 1
                else:
                    s += 1
            

            cursor.execute("""SELECT * from backend_accidents""")
            connection.commit()
            cursor.close()
            connection.close()
            print('Соединение с бд закрыто')
        except:
            print('Не удалось подключиться')


schedule.every(1).seconds.do(check) 

while __name__ == '__main__':
    schedule.run_pending()
