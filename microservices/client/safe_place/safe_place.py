class SafePlaceDecider:
    all_places = {
        (
            ('environment', 'forest'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'bird_1')
        ): (
            'https://www.youtube.com/watch?v=6g3QiE4IB-4',
            'https://www.youtube.com/watch?v=_QB9BVkXnFE',
            'https://www.youtube.com/watch?v=ipf7ifVSeDU'
        ),

        (
            ('environment', 'forest'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=oSmUI3m2kLk'
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=jEnd8JIMii4'
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'yes'),
            ('animals', 'dog_3')
        ): (
            'https://www.youtube.com/watch?v=NfbKa8CQpuE',
            'https://www.youtube.com/watch?v=XmG0rfaIK5s',
            'https://www.youtube.com/watch?v=-ZqsNggRBLY'
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'dog_3')
        ): (
            'https://www.youtube.com/watch?v=7CGXsLkbdv4',
            'https://www.youtube.com/watch?v=GTIPiD1g624',
            'https://www.youtube.com/watch?v=irjUXgvMBR4'
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'dog_2')
        ): (
            'https://www.youtube.com/watch?v=m6L4nG0kaSE',
        ),

        (
            ('environment', 'forest'),
            ('weather', 'snow'),
            ('people', 'no'),
            ('animals', 'dog_3')
        ): (
            'https://www.youtube.com/watch?v=JpBJcOq_0e8',

        ),

        (
            ('environment', 'city'),
            ('weather', 'snow'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=Pms5ZBzZBAM',

        ),

        (
            ('environment', 'home'),
            ('weather', 'snow'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=DKaZTjgYldE',

        ),

        (
            ('environment', 'city'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=0L38Z9hIi5s',
            'https://www.youtube.com/watch?v=LFOx-vmYrts'
        ),

        (
            ('environment', 'city'),
            ('weather', 'sun'),
            ('people', 'yes'),
            ('animals', 'dog_3')
        ): (
            'https://www.youtube.com/watch?v=fa3Slv2i0Uw'
        ),

        (
            ('environment', 'forest'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=c9pQYOGIWM8',
            'https://www.youtube.com/watch?v=ynLpZGegiJE'
        ),

        (
            ('environment', 'forest'),
            ('weather', 'rain'),
            ('people', 'yes'),
            ('animals', 'dog_2')
        ): (
            'https://www.youtube.com/watch?v=ObOAXStZPjs',
        ),

        (
            ('environment', 'forest'),
            ('weather', 'sun'),
            ('people', 'yes'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=5mn437fw27c',
        ),

        (
            ('environment', 'forest'),
            ('weather', 'rain'),
            ('people', 'yes'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=YLeJ9QRaM7I',
        ),

        (
            ('environment', 'forest'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'cat_3')
        ): (
            'https://www.youtube.com/watch?v=Z_JU4NE90gI',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'bird_2')
        ): (
            'https://www.youtube.com/watch?v=Ge4fag9A9kA',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'fantasy_animal_2')
        ): (
            'https://www.youtube.com/watch?v=SE7dzWYWz1w',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'fantasy_animal_2')
        ): (
            'https://www.youtube.com/watch?v=ajPlBlh8sDU',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'rain'),
            ('people', 'yes'),
            ('animals', 'fantasy_animal_2')
        ): (
            'https://www.youtube.com/watch?v=keyhWKkVIHw',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'rain'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=hmzPJmVX9D4',
        ),

        (
            ('environment', 'fantasy'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'no')
        ): (
            'https://www.youtube.com/watch?v=Ii9fO5Y7SVo',
        ),

        (
            ('environment', 'home'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'cat_3')
        ): (
            'https://www.youtube.com/watch?v=xSeVzZsdQlg',
        ),

        (
            ('environment', 'sea'),
            ('weather', 'sun'),
            ('people', 'no'),
            ('animals', 'cat_3')
        ): (
            'https://www.youtube.com/watch?v=VHQLPyGOwWc',
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
