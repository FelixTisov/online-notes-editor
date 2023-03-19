from app import app
import pymysql


class Database:
    def __init__(self):
        self.__host = app.config['DB_HOST']
        self.__username = app.config['DB_USER']
        self.__password = app.config['DB_PASSWORD']
        self.__dbname = app.config['DB_NAME']
        self.__charset = 'utf8mb4'
        self.__autocommit = True
        self.__conn = None
        self.__open_connection()

    def __del__(self):
        self.close_connection()

    def __open_connection(self):
        """Подключение к БД"""
        try:
            if self.__conn is None:
                self.__conn = pymysql.connect(
                    host=self.__host,
                    user=self.__username,
                    password=self.__password,
                    database=self.__dbname,
                    charset=self.__charset,
                    autocommit=self.__autocommit
                )
        except pymysql.MySQLError as sqlerror:
            raise pymysql.MySQLError(f'Failed to connect to the database due to: {sqlerror}')
        except Exception as error:
            raise Exception(f'An exception occured due to: {error}')

    @property
    def db_connection_status(self):
        """Статус подключения"""
        return True if self.__conn is not None else False

    def close_connection(self):
        """Отключиться от БД"""
        try:
            if self.__conn is not None:
                self.__conn.close()
                self.__conn = None
        except Exception as e:
            raise Exception(f'Failed to close the database connection due to: {e}')

    def run_query(self, query):
        """Выполнить sql запрос"""
        try:
            if not query or not isinstance(query, str):
                raise Exception()

            if not self.__conn:
                self.__open_connection()

            with self.__conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()

                return result
        except pymysql.MySQLError as sqlerror:
            raise pymysql.MySQLError(f'Failed to execute query due to: {sqlerror}')
        except Exception as error:
            raise Exception(f'An exception occured due to: {error}')
