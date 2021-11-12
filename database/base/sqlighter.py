import sqlite3

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_userlist(self):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `users` ")

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))
    #
    def add_users(self,name,user_id):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('name', 'user_id') VALUES(?,?)", (name,user_id))



    def delete_users(self,user_id):
        """Добавляем нового подписчика"""
        with self.connection:
            result = self.cursor.execute('DELETE  FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return
    #
    # def update_subscription(self, user_id, status):
    #     """Обновляем статус подписки пользователя"""
    #     with self.connection:
    #         return self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()