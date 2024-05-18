player = {
    'name': '',
    'armor': 0.95,
    'hp': 100,
    'attack': 5,
    'luck': 10,
    'money': 10000,
    'inventory': []
}

enemies = [
    {
        'name': 'Волк', 
        'hp': 10,
        'attack': 10,
        'script': 'Зачем ты здесь? Ты не сможешь меня победить. Принцесса больше не твоя, а чья - не твоя забота. Уходи, пока можешь.',
        'win': 'Ты - достойный противник, но до принцессы тебе всё равно никогда не добраться.',
        'loss': 'Ха! Я же говорил - тебе меня не одолеть. Уходи и не возвращайся.'
    },
    {
        'name': 'Змей Горыныч',
        'hp': 20,
        'attack': 25,
        'script': 'Не ожидал меня встретить? Я, если честно, тоже не думал, что здесь окажусь. После богатырей остаётся только фрилансить, в этот раз сказали защищать долину на пути к замку. В любом случае, ААААААрхрхрархгрх!! Ты не пройдёшь!',
        'win': 'На самом деле, я даже рад, что ты меня победил. Мой босс - дуралей, принцессу не заслужил. Иди дальше. Не зубадь там замолвить за меня словечко. Скажи, что я сражался как лев. Нет.. Как дракон!!',
        'loss': 'Могли бы просто побеседовать. Ты же и сам знал, что у тебя не получится меня убить.. Возвращайся как-нибудь, здесь довольно одиноко.'
    },

    {
        'name': 'Доминик Торетто',
        'hp': 200,
        'attack': 50,
        'script': 'Как ты смог добраться до сюда?! Как ты вообще посмел думать, что можешь со мной сражаться? Ты слаб! Принцесса будет моей, а ты уйдёшь ни с чем. Да будет битва! Самое важное - семья.',
        'win': 'Ты меня убил, но я точно появлюсь в следующей части',
        'loss': 'Прощай..'
    }
]

shop = [
    {
        "name" : "Меч",
        "attack" : 10,
        "single_time_use" : False,
        "price" : 6000
    },
    {
        "name" : "Зелье здоровья",
        "attack": -3,
        "hp": 20,
        "single_time_use": True,
        "price" : 500
    },
    {
        "name" : "Рыцырский шлем",
        "armor": 0.07,
        "single_time_use": False,
        "price": 3000
    },
]