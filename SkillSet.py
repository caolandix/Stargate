import json

class Skill:
    def __init__(self, name = "", slots = 0, bonuses = 0, extra_bonuses = 0):
        self.name = name
        self.slots = slots
        self.extra_bonuses = bonuses
        self.bonus = slots * 5 + extra_bonuses

class SkillSet:
    def __init__(self, json_file = "", skill_list = []):
        self.skill_list = {}
        if len(json_file) > 0:
            skill_list = self.json_to_skills(json_file)
        for skill in skill_list:
            self.skill_list[skill] = Skill(skill)
    
    def json_to_skills(self, json_filename):
        skill_list = []
        with open(json_filename) as json_file:
            json_data = json.load(json_file)
            for skill in json_data['skill']:
                skill_list.append(skill['name'])
        return skill_list

    def print_obj(self):
        
        # print key and values
        for key in self.skill_list.items():
            print(key[0]),
            print(', Slots: ' + str(key[1].slots)),
            print(', Bonus: ' + str(key[1].bonus)),
            print(', Extra Bonus: ' + str(key[1].extra_bonuses))
