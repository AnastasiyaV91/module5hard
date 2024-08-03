class User:                                                             # Создаем класс User (пользователь)
    def __init__(self, nickname, password, age):
        self.nickname = nickname                                        # Определяем атрибуты класса
        self.password = hash(password)                                  # хэшируем пароль
        self.age = age                                                  #

    def __str__(self):
        return f"{self.nickname}"                                       # Возвращаем nickname строкой

class Video:                                                            # Создаем класс Video (видео)
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title                                              #
        self.duration = duration                                        # Определяем атрибуты класса
        self.time_now = time_now                                        #
        self.adult_mode = adult_mode                                    #

    def __str__(self):
        return f"{self.title} {self.duration}"                          # Возвращаем название видео и продолжительность
                                                                        # строкой

class UrTube:                                                           # Создаем класс UrTube
    def __init__(self):
        self.users = []                                                 #
        self.videos = []                                                # Определяем атрибуты класса
        self.current_user = None                                        #

    def log_in(self, nickname, password):                               # Проверяем есть ли пользователь в списке
        for user in self.users:                                         # пользователей
            if user.nickname == nickname and user.password == hash(password):   # Если пользователь в списке есть,
                self.current_user == user                                       # проверяем хэшированный пароль
                return

    def register(self, nickname, password, age):                        # Проверяем есть ли пользователь в списке
        for user in self.users:                                         # пользователей
            if user.nickname == nickname:                               # Если пользователь в списке есть, выводим в
                print(f"Пользователь {nickname} уже существует")        # консоль сообщение
                return
        new_user = User(nickname, password, age)                        #
        self.users.append(new_user)                                     # Добавляем нового пользователя в список
        self.current_user = new_user                                    # пользователей

    def log_out(self):                                                  # Сброс текущего пользователя
        self.current_user = None

    def add(self, *videos):                                             #
        for video in videos:                                            #
            if video.title not in [i.title for i in self.videos]:       # Добавление нового видео в список videos
                self.videos.append(video)                               #

    def get_videos(self, search_word):                                  # Проверка совпадений с поисковым словом
        found_videos = []                                               #
        for video in self.videos:                                       #
            if search_word.lower() in video.title.lower():              #
                found_videos.append(video.title)                        #
        return found_videos                                             # Возвращаем список названий всех видео,
                                                                        # содержащих поисковое слово (search_word)
    def watch_video(self, title):                                       # Просмотр видео
        if not self.current_user:                                       # Если пользователь не зарегистрирован, выводим
            print("Войдите в аккаунт, чтобы смотреть видео")            # в консоль сообщение
            return
        found_video = None                                              # Инициализация переменной для найденного видео 
        for video in self.videos:                                       # Если видео существует в списке и если есть
            if video.title == title:                                    # возврасное ограничение, проверяем возвраст
                found_video = video                                     # пользователя
                if self.current_user.age < 18 and video.adult_mode == True: # Если возвраст меньше 18, выводи в консоль
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")   # сообщение
                    break
                for video.time_now in range(1, found_video.duration +1):             #
                    print(video.time_now, end=" ")                                   #
                    import time                                         # Имитация воспроизведения видео с задержкой
                    time.sleep(0.5)                                     # 0.5 сек
                    if video.time_now == found_video.duration:                       #
                        print("Конец видео")                            # По окончании видео выводим в консоль сообщение
                break











ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
ur.add(v1, v2)

    # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
