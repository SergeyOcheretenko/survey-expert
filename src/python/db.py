from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password='8237',
        database='order_food'
    ) as connection:
        create_db_query = "CREATE DATABASE IF NOT EXISTS order_food"
            
        # show_db_query = "SHOW DATABASES"

        create_clients_table_query = """
        CREATE TABLE IF NOT EXISTS clients (
        client_id INT PRIMARY KEY AUTO_INCREMENT,
        lastname VARCHAR(30),
        firstname VARCHAR(30),
        middlename VARCHAR(30),
        adress VARCHAR(80),
        phone_number CHAR(13)
        );
        """

        insert_clients_query = """
            INSERT INTO clients(lastname, firstname, middlename, adress, phone_number)
            VALUES
            ('Городенко',
            'Олексій',
            'Віталійович',
            'м.Київ, вул.Академіка Янгеля 5, кв.30',
            '+380943236853'),
            ('Михайлов',
            'Іван',
            'Сергійович',
            'м.Київ, прсп.Перемоги 18, кв.4',
            '+380657384759'),
            ('Іванов',
            'Степан',
            'Володимирович',
            'м.Київ, вул.Хрещатик 21, кв.26',
            '+380953769305'),
            ('Жмих',
            'Ірина',
            'Вікторівна',
            'м.Харків, вул.Шевченка 51, кв.42',
            '+380542345683'),
            ('Водограй',
            'Михайло',
            'Петрович',
            'м.Київ, вул.Гагаріна 17, кв.54',
            '+380945739602'),
            ('Травченко',
            'Кирило',
            'Степанович',
            'м.Київ, вул.Лесі Українки 1, кв.4',
            '+380674539284');
        """
        
        select_clients_query = "SELECT * FROM clients;"

        select_phone_query = """
        SELECT *
        FROM clients
        WHERE LEFT(phone_number,6) IN ('+38067', '+38095', '+38097');
        """
        
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            # cursor.execute(show_db_query)
            # for db in cursor:
            #     print(db)
            cursor.execute(create_clients_table_query)
            cursor.execute(insert_clients_query)

            cursor.execute(select_clients_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

            print('-' * 70)
            
            cursor.execute(select_phone_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
            
            connection.commit()
except Error as error:
    print(error)
