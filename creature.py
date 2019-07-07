from SkillSet import SkillSet
from dice import d10

class Creature:
    def __init__(self, name = "", ob = 0, db = 0, level = 1):
        self.name = name
        self.ob = ob
        self.db = db
        self.hits = 0
        self.level = level
        self.hits = self.level * d10()
        self.skill_set = SkillSet("./skillset.json")
        
    def print_obj(self):
        print('Name: ' + self.name)
        print('OB: ' + str(self.ob))
        print('DB: ' + str(self.db))
        print('Hits: ' + str(self.hits))
        print('level: ' + str(self.level))
        print('Skill Set: ')
        self.skill_set.print_obj()
        
if __name__ == "__main__":
    character = Creature("Derp", ob = 5, db = 0)
    character.print_obj()