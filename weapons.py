from abc import ABC, abstractmethod
from aiogram.types import InputMediaPhoto


class Weapons(ABC):
    @abstractmethod
    def photo(self):
        pass

    @abstractmethod
    def inf(self):
        pass


class Classic(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt25bf56ede3e3c57c/5eb281c42278aa3e8d0ba7fa/classic.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/c/cc/Prime_Classic.png/revision/latest?cb=20210707141714')
        ]
        return photo

    def inf(self):
        inf = "За допомогою основного режиму стрільби можна стріляти з високою точністю, " \
              "а за допомогою альтернативного режиму випускати по кілька куль в бою на короткій дистанції."
        return inf


class Shorty(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt7b13117b3a4912a7/5eb281ca5e05b51483afd6bc/shorty.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/b/b7/Oni_Shorty.png/revision/latest?cb=20210708101734')

        ]
        return photo

    def inf(self):
        inf = "Швидкий короткоствольний дробовик смертоносний поблизу, але потребує перезаряджання " \
              "після двох пострілів. Добре поєднується із далекобійними видами зброї."
        return inf


class Frenzy(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt97e5c377459c2f3b/5eb281c43b09c042ddca13a1/frenzy.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/a/a4/Prime_2.0_Frenzy.png/revision/latest?cb=20210707191254')

        ]
        return photo

    def inf(self):
        inf = "Легкий автоматичний пістолет, найефективніший для стрільби на бігу. " \
              "Його високу скорострільність складно контролювати, тож" \
              " на середній дистанції краще стріляти короткими чергами."
        return inf


class Ghost(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltc4788d390015fb7c/5eb281c4105ab84c3815e164/ghost.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/9/94/Reaver%2C_EP_5_Ghost.png/revision/latest?cb=20220809131733')
        ]
        return photo

    def inf(self):
        inf = "Ghost стріляє точно і має магазин великої ємності на випадок промахів. " \
              "На далеку відстань краще стріляти з меншим темпом. Прицільтеся як слід і тисніть на курок."
        return inf


class Sheriff(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt3bbed29a5475c7d4/5eb281ca2278aa3e8d0ba7fe/sheriff.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/f/fd/Reaver_Sheriff.png/revision/latest?cb=20210708103455')
        ]
        return photo

    def inf(self):
        inf = "У цієї потужної гармати дуже сильна віддача - навчитися стріляти з неї не кожному під силу." \
              "Навчіться правильно використовувати Sheriff, і від ваших ворогів сліду не залишиться."
        return inf


class Stinger(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt55951cb43513b87d/5eb7c2209c5d3e37e05f27b6/stinger.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/8/88/Prelude_to_Chaos_Stinger.png/revision/latest?cb=20220622133021')
        ]
        return photo

    def inf(self):
        inf = "Магазин на 20 патронів та жахлива віддача не сприяють чудовому чпрею довгими чергами, " \
              "але прицільна стрільба та вмілий контроль вогню творять чудеса на середній дистанції."
        return inf


class Spectre(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8a6f9eb97f755412/5eb281cae11e6a13a6f613ed/spectre.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/0/02/Forsaken_Spectre.png/revision/latest?cb=20210708122041')
        ]
        return photo

    def inf(self):
        inf = "Універсальна зброя з гарним балансом між уроном, скорострільністю та" \
              " точністю як на коротких, так і на середніх дистанціях."
        return inf


class Bucky(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt2cd5308e8bdfcc8c/5eb281c334a9963e8f9599de/bucky.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/0/09/Ion_Bucky.png/revision/latest?cb=20201112142243')
        ]
        return photo

    def inf(self):
        inf = "Він важкий та точний, а основний режим стрілянини Bucky підходить для захисту кутів та ближнього бою. " \
              "Альтернативний режим дозволить вражати цілі на середній дистанції."
        return inf


class Judge(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt82404f7b88f8c612/5eb281c45050514d1a507146/judge.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/c/c6/Elderflame_Judge.png/revision/latest?cb=20210707203713')
        ]
        return photo

    def inf(self):
        inf = "Judge здатний стріляти точно, але стає непередбачуваним при веденні безперервного вогню. " \
              "Основний режим розносить цілі на ближній відстані, але далі за метр ви ні в що не попадете."
        return inf


class Bulldog(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltd4a396bf5a06e6b4/5eb281c4edfeb076e2050387/bulldog.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/0/0b/Oni_Bulldog.png/revision/latest?cb=20230307165619')
        ]
        return photo

    def inf(self):
        inf = "Ця зброя – справжній звір у руках умілого гравця. Альтернативний режим стрільби" \
              " дозволяє вам прицілюватися та стріляти точними короткими чергами на середні та далекі дистанції."
        return inf


class Guardian(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltd78ee0533f30e0a8/5eb281c4402b8b4d13a566dc/guardian.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/3/3f/Ruination_Guardian.png/revision/latest?cb=20210707184826')
        ]
        return photo

    def inf(self):
        inf = "Гвинтівка, створена за концепцією DMR. Тяжка і менш прийнятна порівняно з іншими гвинтівками," \
              " але точна і потужна. Хороша зброя для прицільної стрілянини на середні та дальні дистанції."
        return inf


class Phantom(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt04ac3b5158b8466a/5eb281caa44a154c3ef84a82/phantom.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/6/65/Oni_Phantom.png/revision/latest?cb=20200911011334')
        ]
        return photo

    def inf(self):
        inf = "Не бійтеся затискати спуск, стріляючи по супротивниках поблизу. Короткі черги з легкістю впораються" \
              " з ворогами на будь-якій дистанції. Точніше гвинтівка стріляє, поки агент не рухається."
        return inf


class Vandal(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt323df4a0d8210605/5eb281cb3b09c042ddca13a5/vandal.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/9/93/ChronoVoid_Vandal.png/revision/latest?cb=20220920131637')
        ]
        return photo

    def inf(self):
        inf = "Однак при стрільбі довгими чергами сильно втрачає стабільність. Vandal зберігає високу шкоду" \
              " на великих дистанціях і відмінно підходить для тих, хто може потрапляти одним пострілом у голову."
        return inf


class Marshal(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt545be89167b88e87/5eb281c4c7007e13a0530dd7/marshal.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/9/91/Sovereign_Marshal.png/revision/latest?cb=20210708101440')
        ]
        return photo

    def inf(self):
        inf = "Зручна снайперська важільна гвинтівка з одним режимом прицілювання, яка дозволяє" \
              " тримати занадто агресивних противників на відстані. Низька скорострільність означає," \
              " що ви або потрапляєте, або підставляєтесь під атаку супротивника."
        return inf


class Operator(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt3e6bf41bd01ca11e/5eb281ca24400043b65016ba/operator.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/e/ed/Elderflame_Operator.png/revision/latest?cb=20210707203739')
        ]
        return photo

    def inf(self):
        inf = "Руйнівна снайперська гвинтівка зі ковзним затвором та двома режимами наближення" \
              " прицілу. Марна при пересуванні, але завдає величезної шкоди кожним пострілом."
        return inf


class Ares(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt371bee690082f494/5eb281c3e11e6a13a6f613e9/ares.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/d/d5/Singularity_Ares.png/revision/latest?cb=20201010151740')
        ]
        return photo

    def inf(self):
        inf = "Завдяки місткому магазину Ares дозволяє вести вогонь на придушення і " \
              "завдавати серйозної шкоди групам супротивників."
        return inf


class Odin(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt0884ed7405d3646c/5eb281c38f7a7c3f6ec725e1/odin.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/1/13/BlastX_Odin.png/revision/latest?cb=20201210133413')
        ]
        return photo

    def inf(self):
        inf = "Здатний вести вогонь на придушення з високою шкодою та великою кунчністю." \
              " Поливайте ворогів свинцем поблизу або використовуйте додатковий режим стрілянини," \
              " щоб стати живою туреллю."
        return inf


class Knife(Weapons):
    def photo(self):
        photo = [InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt133c8372261f21a9/5eb281cbedfeb076e205038b/tactical-knife.png'),
                 InputMediaPhoto('https://static.wikia.nocookie.net/valorant/images/7/75/RGX_11z_Pro_Blade_Level_2.png/revision/latest?cb=20211005172431')
        ]
        return photo

    def inf(self):
        inf = "Якщо у вас виникли сумніви або закінчилися набої, то не бійтеся скористатися ножем. " \
              "Підвищує швидкість переміщення, швидко знищує об'єкти, а також вбиває супротивників з " \
              "одного удару зі спини при використанні альтернативного режиму атаки."
        return inf