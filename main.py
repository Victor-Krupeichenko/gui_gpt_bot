# pip install -U g4f[all]
# pip install -U nodriver

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from gpt_gui import Ui_MainWindow
from g4f.client import Client
from g4f.errors import RetryProviderError
import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
import time


class Worker(QThread):
    """
    Класс потока, который выполняет длительную операцию
    """
    finished = pyqtSignal(str)

    def __init__(self, my_gpt):
        super().__init__()
        self.my_gpt = my_gpt
        self.question = None

    def run(self):
        """
        Выполнение длительной операции здесь
        """
        self.my_gpt.ui.label_2_output_text.append(f'Виктор: {self.question}\n')
        while True:
            response = self.my_gpt.request_to_gpt(self.question)  # Это может быть длительная операция
            if response.startswith('sorry') or response.startswith('GPT_error'):
                error = f'GPT_chat: Произошла неизвестная внутренняя ошибка\nGPT_chat: Повторяю вопрос: {self.question}'
                self.my_gpt.ui.label_2_output_text.append(f'{error}')
                self.my_gpt.ui.label_2_output_text.append(f'\n{"*" * 106}\n')
                time.sleep(5)
                continue
            break
        self.finished.emit(response)

    def set_question(self, question):
        """
        Устанавливаем какой вопрос был задан к методу request_to_gpt(question)
        :param question: вопрос к gpt
        """
        self.question = question


class MyGpt(QMainWindow):
    """Класс основного окна приложения"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.client = Client()
        self.model = 'gpt-3.5-turbo'
        # self.model = 'gpt-4o'
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.minimize_window_button.setCursor(Qt.PointingHandCursor)
        self.ui.close_window_button.setCursor(Qt.PointingHandCursor)
        self.ui.speaker_button.setCursor(Qt.PointingHandCursor)
        self.ui.keyboard_button.setCursor(Qt.PointingHandCursor)
        self.ui.question_button.setCursor(Qt.PointingHandCursor)

        # выход из программы
        self.ui.close_window_button.clicked.connect(self.close)
        # минимизация окна
        self.ui.minimize_window_button.clicked.connect(self.showMinimized)
        # Получение текста из поля запроса
        self.ui.question_button.clicked.connect(self.get_text)
        # перемещение окна
        self.old_pos = None

        self.question = None
        # экземпляр класса другого потока
        self.worker = Worker(self)
        self.worker.finished.connect(self.response_output)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def request_to_gpt(self, question):
        """
        Запрос к gpt (Задает вопрос gpt)
        :param question:
        :return: строку с ответом от gpt или ошибкой
        """
        asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{'role': 'user', 'content': f'{question} (пиши на русском)'}],
            )
            return response.choices[0].message.content.replace('\n\n', '\n')
        except (RetryProviderError, Exception) as e:
            return f'GPT_error: Ошибка запроса к GPT: {e}'

    def get_text(self):
        """
        Получение текста из поля вопроса, а также передает в новый поток вопрос который мы только что получили
        """
        self.question = self.ui.lineEdit_question.text()
        self.ui.lineEdit_question.clear()

        # Создание новый поток
        self.worker.set_question(self.question)  # передаем вопрос который мы получили выше
        self.worker.start()  # запускаем новый поток

    def response_output(self, response):
        """Вывод ответа"""
        self.ui.label_2_output_text.append(f'GPT_chat: {response}')
        self.ui.label_2_output_text.append(f'\n{"*" * 106}\n')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_prog = MyGpt()
    main_prog.show()
    sys.exit(app.exec_())
