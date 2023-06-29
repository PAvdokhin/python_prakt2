class Tasks:
    def task1(self):
        print('Заменяемый task')

    def _task2(self):
        print('Полу-заменяемый task')

    def __task3(self):
        print('Незаменяемый task')



info = Tasks()

info.task1()
info._task2()
info.__task3()
