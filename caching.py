import time


def lry_size(maxsize):
    def lry_cache(func):
        # связать cache and timeQueue. Двусвязный  список? Или просто по индексам?
        # cache - key= время запроса(cur_time). value = file(в байтах)
        # timeQueue - список, содержащий время запросов
        cache = dict()
        timeQueue = list()
        def wrapper(file):
            cur_time = time.time()
            data = func(file)
            # data ничего не возвращает, с чем работать(на примере upload_data_in_repository)
            # Если значение уже было в кэше вернем его
            if data in cache.values():
                # Сначала обновим время последнего запроса к data
                cur_time = time.time()
                timeQueue.append(cur_time)
                return cache[cur_time]
            # Иначе добавим в кэш результат
            cache[cur_time] = data
            # Если в кэше больше maxsize элементов, то удалим самый старый
            if len(cache) > maxsize:
                old_time_key = min(timeQueue)
                cache.pop(old_time_key)
                timeQueue.pop(old_time_key)
            # Добавим в кэш и в временную очерердь
            cache[file] = data
            timeQueue[file] = cur_time
            return data
        return wrapper
    return lry_cache
