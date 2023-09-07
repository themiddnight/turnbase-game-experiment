import random

class Human:
    def __init__(self, ch_name):
        self.ch_type = "Human"
        self.ch_name = ch_name
        self.__ch_rel = {}

    def move(self, direction):
        print(f"{self.ch_name} moved {direction}.")

    def speak(self, words="Hi!", target=None):
        if target:
            print(f'{self.ch_name} talks to {target.ch_name}: "{words}"')
            self.increase_rel(target.ch_name)
            target.increase_rel(self.ch_name)
        else:
            print(f'{self.ch_name} said "{words}"')

    def increase_rel(self, name):
        if name not in self.__ch_rel:
            self.__ch_rel[name] = 0
        self.__ch_rel[name] += 1

    def get_relationship(self):
        return self.__ch_rel


class Monster:
    def __init__(self, ch_name):
        self.ch_type = "Monster"
        self.ch_name = ch_name

    def move(self, direction):
        print(f"{self.ch_name} moved {direction}.")

    def speak(self, words=None):
        print(f'{self.ch_name} said "WAAHHHHHGHHHH!!!"')


class Warrior:
    def __init__(self, ch_hp, ch_mp, ch_atk, ch_def, ch_acc, ch_luk):
        # r for remaining.
        self.ch_hp = ch_hp
        self.ch_hp_r = self.ch_hp
        self.ch_mp = ch_mp
        self.ch_mp_r = self.ch_mp
        # i for initial. it will be extra added in each class.
        self.ch_atk_i = ch_atk
        self.ch_def_i = ch_def
        self.ch_acc_i = ch_acc
        self.ch_luk_i = ch_luk
        self.ch_atk = self.ch_atk_i
        self.ch_def = self.ch_def_i
        self.ch_acc = self.ch_acc_i
        self.ch_luk = self.ch_luk_i
        # if 100%, critical chance = 1/5
        self.__critical_factor = self.ch_luk / 5

    def __generate_bar(self, max_value, value):
        bar = round((value * 20) / max_value)
        space = round(20 - bar)
        bar_str = "|" + "◼" * bar + "·" * space + "|"
        return bar_str

    def show_init_status(self):
        print(f"{f' {self.ch_name} : {self.ch_class} ':=^25}")
        print("HP:  ", round(self.ch_hp, 2))
        print("MP:  ", round(self.ch_mp, 2))
        print("ATK: ", round(self.ch_atk, 2))
        print("DEF: ", round(self.ch_def, 2))
        print("ACC: ", round(self.ch_acc * 100), "%")
        print("LUK: ", round(self.ch_luk * 100), "%")
        print()

    def show_hp_bar(self):
        bar_str = self.__generate_bar(self.ch_hp, self.ch_hp_r)
        if self.ch_hp_r > 0:
            print(f"HP: {bar_str} {self.ch_hp_r}/{self.ch_hp}")
        else:
            print(f"{self.ch_name} is dead ❌")

    def show_mp_bar(self):
        bar_str = self.__generate_bar(self.ch_mp, self.ch_mp_r)
        if self.ch_hp_r > 0:
            print(f"MP: {bar_str} {self.ch_mp_r}/{self.ch_mp}")
        else:
            print(f"{self.ch_name} is dead ❌")

    def attack(self, target):
        if self.ch_hp_r > 0:
            if target.ch_hp_r > 0:
                critical = random.random() < self.__critical_factor
                acc_factor = random.uniform(self.ch_acc, 1)
                attack = self.ch_atk / (target.ch_def * 0.5)
                if acc_factor > 0.4:
                    attack = round(attack * acc_factor, 2)
                    if critical:
                        attack = round(attack * 1.5, 2)
                else:
                    attack = 0
                target.ch_hp_r = round(target.ch_hp_r - attack, 2)
                if target.ch_hp_r < 0:
                    target.ch_hp_r = 0
                # print action
                if attack:
                    if critical:
                        self.speak("Bring it on!!")
                        print(
                            (
                                f"- {self.ch_name} attacks "
                                f"{target.ch_name} 💥{attack} !"
                            )
                        )
                    else:
                        print(
                            (f"- {self.ch_name} attacks " f"{target.ch_name} 🔪{attack}")
                        )
                else:
                    print(f"- {self.ch_name} missed 💨")
                    self.speak("Crap!!")
                return True
            else:
                print((f"- {target.ch_name} is dead ❌ " f"{self.ch_name} do nothing."))
                return False
        else:
            self.ch_hp_r = 0
            print(f"- {self.ch_name} can't do anything ❌")
            return True