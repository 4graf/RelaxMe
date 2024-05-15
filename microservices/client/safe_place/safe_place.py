class SafePlaceDecider:
    all_places = {
        (
            ('environment', 'forest'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'bird_1')
        ): (
            '6g3QiE4IB-4',
            '_QB9BVkXnFE',
            'ipf7ifVSeDU'
        ),

        (
            ('environment', 'forest'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'oSmUI3m2kLk'
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'jEnd8JIMii4'
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'yes'),
            ('animals', 'dog_3')
        ): (
            'NfbKa8CQpuE',
            'XmG0rfaIK5s',
            '-ZqsNggRBLY'
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'dog_3')
        ): (
            '7CGXsLkbdv4',
            'GTIPiD1g624',
            'irjUXgvMBR4'
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'dog_2')
        ): (
            'm6L4nG0kaSE',
        ),

        (
            ('environment', 'forest'),
            ('weather', 'snow'),
            ('people', 'no'),
            ('animals', 'dog_3')
        ): (
            'JpBJcOq_0e8',

        ),

        (
            ('environment', 'city'),
            ('weather', 'snow'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'Pms5ZBzZBAM',

        ),

        (
            ('environment', 'home'),
            ('weather', 'snow'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'DKaZTjgYldE',

        ),

        (
            ('environment', 'city'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            '0L38Z9hIi5s',
            'LFOx-vmYrts'
        ),

        (
            ('environment', 'city'),
            ('weather', 'sun'),
            ('people', 'yes'),
            ('animals', 'dog_3')
        ): (
            'fa3Slv2i0Uw'
        ),

        (
            ('environment', 'forest'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'c9pQYOGIWM8',
            'ynLpZGegiJE'
        ),

        (
            ('environment', 'forest'),
            ('weather', 'rain'),
            ('people', 'yes'),
            ('animals', 'dog_2')
        ): (
            'ObOAXStZPjs',
        ),

        (
            ('environment', 'forest'),
            ('weather', 'sun'),
            ('people', 'yes'),
            ('animals', 'no')
        ): (
            '5mn437fw27c',
        ),

        (
            ('environment', 'forest'),
            ('weather', 'rain'),
            ('people', 'yes'),
            ('animals', 'no')
        ): (
            'YLeJ9QRaM7I',
        ),

        (
            ('environment', 'forest'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'cat_3')
        ): (
            'Z_JU4NE90gI',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'bird_2')
        ): (
            'Ge4fag9A9kA',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'fantasy_animal_2')
        ): (
            'SE7dzWYWz1w',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'fantasy_animal_2')
        ): (
            'ajPlBlh8sDU',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'rain'),
            ('people', 'yes'),
            ('animals', 'fantasy_animal_2')
        ): (
            'keyhWKkVIHw',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'hmzPJmVX9D4',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'Ii9fO5Y7SVo',
        ),

        (
            ('environment', 'home'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'cat_3')
        ): (
            'xSeVzZsdQlg',
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'cat_3')
        ): (
            'VHQLPyGOwWc',
        ),
    }

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

        return 'yes' if people == 3 else 'no'

    @classmethod
    def _animals(cls, quest_result):
        dog_keys = ((4, 0, 2),
                    (5, 0, 3))
        dog = cls._score(quest_result, dog_keys, score_multiple=True)

        cat_keys = ((2, 6, 1),
                    (4, 1, 2),
                    (5, 1, 3))
        cat = cls._score(quest_result, cat_keys, score_multiple=True)

        bird_keys = ((2, 0, 1),
                     (4, 2, 2),
                     (5, 2, 3))
        bird = cls._score(quest_result, bird_keys, score_multiple=True)

        fish_keys = ((4, 3, 2),
                     (5, 3, 3))
        fish = cls._score(quest_result, fish_keys, score_multiple=True)

        fantasy_animal_keys = ((4, 4, 2),
                               (5, 4, 3))
        fantasy_animal = cls._score(quest_result, fantasy_animal_keys, score_multiple=True)

        all_categories = {'dog': dog,
                          'cat': cat,
                          'bird': bird,
                          'fish': fish,
                          'fantasy_animal': fantasy_animal}

        result = max(all_categories, key=all_categories.get)
        score = all_categories[result]
        score = 3 if score > 3 else score
        result = 'no' if score == 0 else f'{result}_{score}'

        return result

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
