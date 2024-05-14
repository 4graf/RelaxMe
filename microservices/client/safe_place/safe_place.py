class SafePlaceDecider:
    @classmethod
    def get_safe_place(cls, quest_result):
        safe_place = {'environment': cls._environment(quest_result),
                      'weather': cls._weather(quest_result),
                      'people': cls._people(quest_result),
                      'animals': cls._animals(quest_result)}

        return safe_place

    @classmethod
    def _environment(cls, quest_result):
        house_keys = ((0, 0),
                      (0, 1),
                      (2, 6),
                      (3, 0),
                      (7, 0),
                      (8, 1),
                      (9, 0))
        house = cls._score(quest_result, house_keys)

        forest_keys = ((0, 3),
                       (2, 1),
                       (2, 3),
                       (3, 0),
                       (7, 3),
                       (8, 5),
                       (9, 2))
        forest = cls._score(quest_result, forest_keys)

        sea_keys = ((0, 4),
                    (2, 4),
                    (3, 0),
                    (7, 4),
                    (8, 0),
                    (9, 1))
        sea = cls._score(quest_result, sea_keys)

        city_keys = ((0, 2),
                     (2, 5),
                     (3, 0),
                     (7, 1),
                     (8, 3),
                     (9, 4))
        city = cls._score(quest_result, city_keys)

        fantasy_keys = ((3, 1),
                        (4, 4),
                        (5, 4),
                        (7, 2),
                        (8, 4),
                        (9, 3))
        fantasy = cls._score(quest_result, fantasy_keys)

        all_categories = {'house': house,
                          'forest': forest,
                          'sea': sea,
                          'city': city,
                          'fantasy': fantasy}

        result = max(all_categories, key=all_categories.get)

        return result

    @classmethod
    def _weather(cls, quest_result):
        sun_keys = ((1, 1),
                    (6, 1),
                    (6, 2))
        sun = cls._score(quest_result, sun_keys)

        rain_keys = ((1, 0),
                     (6, 1),
                     (6, 3))
        rain = cls._score(quest_result, rain_keys)

        snow_keys = ((1, 0),
                     (6, 0))
        snow = cls._score(quest_result, rain_keys)

        all_categories = {'sun': sun,
                          'rain': rain,
                          'snow': snow}

        result = max(all_categories, key=all_categories.get)

        return result

    @classmethod
    def _people(cls, quest_result):
        people_keys = ((0, 1),
                       (0, 2),
                       (2, 5),
                       (7, 0),
                       (7, 1))
        people = cls._score(quest_result, people_keys)

        return 'people' if people == 3 else 'not people'

    @classmethod
    def _animals(cls, quest_result):
        dog_keys = ((4, 0, 2),
                    (5, 0, 3))
        dog = cls._score(quest_result, dog_keys)

        cat_keys = ((2, 6, 1),
                    (4, 1, 2),
                    (5, 1, 3))
        cat = cls._score(quest_result, cat_keys)

        bird_keys = ((2, 0, 1),
                     (4, 2, 2),
                     (5, 2, 3))
        bird = cls._score(quest_result, bird_keys)

        fish_keys = ((4, 3, 2),
                     (5, 3, 3))
        fish = cls._score(quest_result, fish_keys)

        fantasy_animal_keys = ((4, 4, 2),
                               (5, 4, 3))
        fantasy_animal = cls._score(quest_result, fantasy_animal_keys)

        all_categories = {'dog': dog,
                          'cat': cat,
                          'bird': bird,
                          'fish': fish,
                          'fantasy_animal': fantasy_animal}

        result = max(all_categories, key=all_categories.get)

        return result, all_categories[result]

    @classmethod
    def _score(cls, quest_result, keys, score_multiple=False):
        result = 0

        if score_multiple:
            for quest, answer, value in keys:
                if quest_result[quest] == answer:
                    result += value
            return result
        else:
            for quest, answer in keys:
                if quest_result[quest] == answer:
                    result += 1
            return result
