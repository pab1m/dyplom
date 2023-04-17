from abc import ABC, abstractmethod
from aiogram.types import InputMediaPhoto


class Maps(ABC):
    @abstractmethod
    def photos(self):
        pass

    @abstractmethod
    def inf(self):
        pass


class Lotus(Maps):
    def photos(self):
        photo = [
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt0bb2058c88892462/63b8a805ade3a64c67746408/Lotus_Screenshot_1.jpg?auto=webp&width=915'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt4c4df42a35c18f69/63b784c889d0f0116272223f/Phase_3_Minimap_LOTUS.jpg?auto=webp&width=515'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt4f595d14ee2ee972/63b8a8047f7baa7b8ce598a8/Lotus_Screenshot_2.jpg?auto=webp&width=915'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt3f7683427640a207/63b8a805cb9ce5175b0f310d/Lotus_Screenshot_3.jpg?auto=webp&width=915'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt296ca5112fed17f4/63b8a8058a5edf5b50386141/Lotus_Screenshot_4.jpg?auto=webp&width=915'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltdb487ae5810363a7/63b8a8056e04e50b40ff66fe/Lotus_Screenshot_5.jpg?auto=webp&width=915'),
        ]
        return photo

    def inf(self):
        inf = "Таємнича споруда, в якій знаходиться астральний канал, випромінює древню силу. " \
              "Великі кам'яні двері забезпечують різноманітні можливості пересування і відкривають шляхи до трьох таємничих місць."
        return inf


class Pearl(Maps):
    def photos(self):
        photo = [
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt0c118364c6320f60/62a289d3891af05acaff06b1/Pearl_Gallery_01.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltd91a0e43577787d7/6328a5ce8a5a2b30fbe2a57f/Pearl_Map_Website_Asset_v2.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltcf2c066dc0337049/62a28a30f4da744f1d8c60c9/Pearl_Gallery_02.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt771890dd49e137a3/62a28a398f6a4950536cea50/Pearl_Gallery_03.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltfe248e709f94f6a5/62a28a54a18b205191cf7409/Pearl_Gallery_06.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt687d1a1bc8fe0cf0/62a28a6a682a22504d4e3734/Pearl_Gallery_08.jpg?auto=webp&width=464'),
        ]
        return photo

    def inf(self):
        inf = "Ця карта з двома точками, де захисники чекають на атакувальників внизу, розташована в мальовничому підводному місті. " \
              "На Pearl немає незвичайних механік - тільки цікавий ландшафт. Боріться на невеликому міді або в довгих бічних проходах на нашій першій карті на Землі 'Омега'."
        return inf


class Fracture(Maps):
    def photos(self):
        photo = [
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf4485163c8c5873c/6131b23e9db95e7ff74b6393/Valorant_FRACTURE_Minimap_Alpha_web.png'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltbd14247152e640c9/63336bcdde1e8c340e57b061/Fracture_Map_Website_Asset-507.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt371ab49354f8002f/6131bedf07866d6a2d823d2c/Fracture_Screenshot-1.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt077539ab4901aaf7/6131bf103ff46b267bdfaf8a/Fracture_Screenshot-2.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt82553061d7056a29/6131bf1c85514a6ee3fac85b/Fracture_Screenshot-3.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6632690fbfaae9a1/6131bf3a504fe365615e53c9/Fracture_Screenshot-6.jpg?auto=webp&width=464'),
        ]
        return photo

    def inf(self):
        inf = "Секретний дослідницький центр, розділений надвоє через невдалий експеримент із радіанітом. Ця незвичайна карта відкриває різні можливості для захисників: " \
              "застаньте атакувальників зненацька на їхньому боці або задраюйте люки, щоб пережити штурм. Вибір за вами!"
        return inf


class Breeze(Maps):
    def photos(self):
        photo = [
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltb03d2e4867f2e324/607f995892f0063e5c0711bd/breeze-featured_v1.png'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt1aa82531c6b3a04b/607fa05b33cf413db790d632/breeze_1a.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltde7c2fc29aa0d3a0/607f9e3ce650b13fbe2129d2/breeze_2.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt174b8512c8e4d6a5/607f9e3c03ce953dac7563e4/breeze_3.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltc1e8e8a2228fef3a/607f9e3e92f0063e5c0711cb/breeze_6.jpg?auto=webp&width=464'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blta0463cfd3f61287d/607f9e4f1cac355a10f6bf96/breeze_12.jpg?auto=webp&width=464'),
        ]
        return photo

    def inf(self):
        inf = "Ласкаво просимо в тропічний рай. Милуйтеся стародавніми руїнами, досліджуйте морські печери і приводьте з собою друзів. " \
              "Тут на вас чекають відкрита місцевість і перестрілки на далеких дистанціях, тож допомога зайвою точно не буде. Головне - вчасно прикрити фланги."
        return inf


class Icebox(Maps):
    def photos(self):
        photo = [
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltde02911a015d7ef9/5f80d2851f5f6d4173b4e49d/Icebox_transparentbg_for_Web.png'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt99dbdb8199ef057e/626c2e245d936230ca8ea9d6/04-2022-Icebox-Minimap-2.jpg?auto=webp&width=473'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blta5558199bebb5107/5f80debfa50ed742e7fca4b9/icebox_3.jpg?auto=webp&width=473'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt5e97ee30cae1b6b6/5f80dec04671ee30c689ca24/icebox_5.jpg?auto=webp&width=473'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt3073fafdd0e84ca8/5f80dec03f52332642075f9b/icebox_7.jpg?auto=webp&width=473'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt5afffe335e51db97/626c2e23d2794936634f95ce/04-2022-Icebox-9.jpg?auto=webp&width=473'),
        ]
        return photo

    def inf(self):
        inf = "Вам доведеться битися на покинутій секретній арктичній базі Kingdom. Точки для встановлення бомби захищені снігом і металом. Тут вам знадобляться хитрість і спритність. " \
              "Скористайтеся тросами, щоб залишитися непоміченими або застати ворога зненацька."
        return inf


class Bind(Maps):
    def photos(self):
        photo = [
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8538036a309525ae/5ebc470bfd85ad7411ce6b50/bind-featured.png'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltad4274632c983531/5ecd64d04d187c101f3f2486/bind-minimap-2.png?auto=webp&width=537'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt4d395d5eb0c5aeec/5eabe92d97c0a55d71b7fce5/bind2.jpg?auto=webp&width=714'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt275a73b80ff9eb5a/5eabe92db8a6356e4ddc0c92/bind3.jpg?auto=webp&width=714'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt81c2ff999b2e5887/5eabe92d08d37e6d82ef715a/bind4.jpg?auto=webp&width=714'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blta6be60823002f711/5eabe92d4398082ffe23fdb5/bind5.jpg?auto=webp&width=714'),
        ]
        return photo

    def inf(self):
        inf = "Дві точки. Ніякого міду. Куди ж іти, направо чи наліво? Що б ви не обрали, на кожному напрямку є прямий маршрут " \
              "для нападу й односторонній телепорт для виходу за спини супротивників."
        return inf


class Haven(Maps):
    def photos(self):
        photo = [
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8afb5b8145f5e9b2/5ebc46f7b8c49976b71c0bc5/haven-featured.png'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltedb5d57941e4f3f5/5ecd64c14d187c101f3f2484/haven-minimap-2.png?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt65a4029cdfaf77b4/5eabe9861b51e36d7c1b67ab/haven2.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt7df0b99a582cc5aa/5eabe987b8a6356e4ddc0ca4/haven1.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt2bd976c100216469/5eabe98608d37e6d82ef7160/haven3.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt768f194cd2c52f84/5eabe9862b79652f27c326ca/haven4.jpg?auto=webp&width=538'),
        ]
        return photo

    def inf(self):
        inf = "Стіни забутого монастиря стрясає шум бою агентів, які борються за контроль над трьома точками. " \
              "Території для захоплення більше, але захисникам набагато легше агресивно пушити противника."
        return inf


class Split(Maps):
    def photos(self):
        photo = [
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltd188c023f88f7d91/5ebc46db20f7727335261fcd/split-featured.png'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blteb20e9c083614412/63b8a95cbf8ad51208626d6e/Phase_3_Minimap_SPLIT.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt643d33e2defb855c/5eabe9fe248a28605479c547/split1.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8114d8ae57703cf8/5ed81946bf4ae52c761ec8e8/split2-2.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltdfd43bd79d9b3410/5eabe9fea20afe612d82f833/split3.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf7a4f75409f2dbc1/5ed81936047b8c2b9c25fe74/split4-2.jpg?auto=webp&width=538'),
        ]
        return photo

    def inf(self):
        inf = "На цій карті велике значення має зайняття висот. Дві точки відокремлює одна від одної центр з високими позиціями, на які можна швидко піднятися по мотузках. " \
              "Контроль над кожною точкою допоможуть утримати вежі, що підносяться над ними. Не забувайте поглядати вгору."
        return inf


class Ascent(Maps):
    def photos(self):
        photo = [
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blta9b912e1a1b59aa4/5ebc471cfa550001f72bcb13/ascent-featured.png'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt47bef6aa9e43d8ec/5ecd64df96a8996de38bbf8f/ascent-minimap-2.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt930666d9ab927326/5eabe9c45751b2150e57a42c/ascent1.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt9e24fe356d0faf81/5eabe9c497c0a55d71b7fceb/ascent2.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt77e465b8079103af/5eabe9c4af7e315106b479a1/ascent3.jpg?auto=webp&width=538'),
            InputMediaPhoto('https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blta7375f4e704347dc/5eabe9c4b8a6356e4ddc0caa/ascent4.jpg?auto=webp&width=538'),
        ]
        return photo

    def inf(self):
        inf = "Дві точки Ascent відокремлені одна від одної відкритим майданчиком для дрібних позиційних сутичок і відстрілу супротивників. " \
              "Кожна точка може бути посилена герметичними дверима; після їх активації вам знадобиться або знищити їх, або знайти інший шлях на точку. Ні кроку назад!"
        return inf