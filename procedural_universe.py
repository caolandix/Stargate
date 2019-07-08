import json
import os
import argparse
import dice

class Universe:
    def __init__(self, num_star_systems = 10):
        self.star_systems = []
    
    def generate(self):
        for i in range(0, num_star_systems):
            star_system = StarSystem()
            star_system.generate()
            self.star_systems.append(star_system)
    
class StarSystem:
    def __init__(self):
        self.stars = []
        
    def generate(self):
        roll = dice.d6(2)
        num_stars = 1
        if roll == 10:
            num_stars = 2
        elif roll == 11:
            num_stars = 3
        else:
            num_stars = 4
        for i in range(num_stars):
            star = (Star()).generate()
            self.stars.append(star)
    
class Star:
    """
    structure:
    
    (oribital_object_data[star_class])[star_type] = < Stellar Mass = idx0, Biozone range = idx1, Inner Limit = idx2, Stellar Radius = idx3, Planets On = idx4, Num Orbits = idx5, Life Roll Modifier = idx6 >)
    """
    orbital_object_data = {
        "O" : {
                "Ia" : [ 70.0, (790.0, 1190.0), 16.0, 0.2, 0, [], -12 ],
                "Ib" : [ 60.0, (630.0, 950.0),  13.0, 0.1, 0, [], -12 ],
                "V"  : [ 50.0, (500.0, 750.0),  10.0, 0.0, 0, [], -9 ],
               },
        "B" : {
                "Ia" : [ 50.0, (500.0, 750.0), 10.0, 0.2, 0, [], -10 ],
                "Ib" : [ 40.0, (320.0, 480.0),  6.3, 0.1, 0, [], -12 ],
                "II" : [ 35.0, (250.0, 375.0),  5.0, 0.1, 3, [ 3, 1 ], -9 ],
                "III" : [ 30.0, (200.0, 300.0), 4.0, 0.0, 3, [ 3, 1 ], -9 ],
                "IV" : [ 20.0, (180.0, 270.0),  3.8, 0.0, 3, [ 3, 1 ], -9 ],
                "V" : [ 10.0, (30.0, 45.0),     0.6, 0.0, 4, [ 3, 1 ], -9 ],
               },
        "A" : {
                "Ia" : [ 30.0, (200.0, 300.0), 4.0, 0.6, 3, [ 3, 3 ], -10 ],
                "Ib" : [ 16.0, (50.0, 75.0),  1.0, 0.2, 3, [ 3, 2 ], -10 ],
                "II" : [ 10.0, (20.0, 30.0),  0.4, 0.0, 3, [ 3, 2 ], -10 ],
                "III" : [ 6.0, (5.0, 7.5), 0.0, 0.0, 3, [ 3, 1 ], -10 ],
                "IV" : [ 4.0, (4.0, 6.0),  0.0, 0.0, 4, [ 3, 0 ], -10 ],
                "V" : [ 3.0, (3.1, 4.7),  0.0, 0.0, 5, [ 3, -1 ], -9 ],
            },
        "F" : {
                "Ia" : [ 15.0, (200.0, 300.0), 4.0, 0.8, 4, [ 3, 3 ], -10 ],
                "Ib" : [ 13.0, (50.0, 75.0), 1.0, 0.2, 4, [ 3, 2 ], -10 ],
                "II" : [ 8.0, (13.0, 19.0), 0.3, 0.0, 4, [ 3, 1 ], -9 ],
                "III" : [ 2.5, (2.5, 3.7), 0.1, 0.0, 4, [ 3, 0 ], -9 ],
                "IV" : [ 2.2, (2.0, 3.0), 0.0, 0.0, 6, [ 3, 0 ], -9 ],
                "V" : [ 1.9, (1.6, 2.4),  0.0, 0.0, 13, [ 3, -1 ], -8 ],
            },
        "G" : {
                "Ia" : [ 12.0, (160.0, 240.0), 3.1, 1.4, 6, [ 3, 3 ], -10 ],
                "Ib" : [ 10.0, (50.0, 75.0), 1.0, 0.4, 6, [ 3, 2 ], -10 ],
                "II" : [ 6.0, (13.0, 19.0), 0.3, 0.1, 6, [ 3, 1 ], -9 ],
                "III" : [ 2.7, (3.1, 4.7), 0.1, 0.0, 6, [ 3, 0 ], -8 ],
                "IV" : [ 1.8, (1.0, 1.5), 0.0, 0.0, 7, [ 3, -1 ], -6 ],
                "V" : [ 1.1, (0.5, 0.6), 0.0, 0.0, 16, [ 3, -2 ], 0 ],
                "VI" : [ 0.8, (0.2, 0.3), 0.0, 0.0, 16, [ 2, 1 ], 1 ],
            },
        "K" : {
                "Ia" : [ 15.0, (125.0, 190.0), 2.5, 3.0, 10, [ 3, 2 ], -10 ],
                "Ib" : [ 12.0, (50.0, 75.0), 1.0, 1.0, 16, [ 3, 2 ], -10 ],
                "II" : [ 6.0, (13.0, 19.0), 0.3, 0.2, 16, [ 3, 1 ], -9 ],
                "III" : [ 3.0, (4.0, 5.9), 0.1, 0.0, 16, [ 3, 0 ], -7 ],
                "IV" : [ 2.3, (1.0, 1.5), 0.0, 0.0, 16, [ 3, -1 ], -5 ],
                "V" : [ 0.9, (0.5, 0.6), 0.0, 0.0, 16, [ 3, -2 ], 0 ],
                "VI" : [ 0.5, (0.2, 0.3), 0.0, 0.0, 16, [ 2, 1 ], 1 ],
            },
        "M" : {
                "Ia" : [ 20.0, (100.0, 150.0), 2.0, 7.0, 16, [ 3, 0 ], -10 ],
                "Ib" : [ 16.0, (50.0, 76.0), 1.0, 4.2, 16, [ 3, 0 ], -10 ],
                "II" : [ 8.0, (16.0, 24.0), 0.3, 1.1, 16, [ 3, 0 ], -9 ],
                "III" : [ 4.0, (5.0, 7.5), 0.1, 0.3, 16, [ 3, 0 ], -6 ],
                "V" : [ 0.3, (0.1, 0.2), 0.0, 0.0, 16, [ 3, -2 ], 1 ],
                "VI" : [ 0.2, (0.1, 0.1), 0.0, 0.0, 16, [ 2, 2 ], 2 ],
            },
        "D" : {
                "dwarf" : [ 0.8, (0.03, 0.03), 0.0, 0.0, -1, [ -1, 0 ], -10 ],
            },
    }
    
    
    def __init__(self):
        self.planets = []
        self.star_class = ""
        self.star_type = ""
        self.stellar_mass = 0
        self.biozone = []
        self.inner_limit = 0
        self.stellar_radius = 0.0
        self.planets_on = 0
        self.num_orbits = 0
        self.life_roll_mod = 0
        
    def determine_star_class(self):
        roll = dice.d6(3)
        if roll >= 3 and roll <= 5:
            self.star_class = "D"
        elif roll == 6:
            self.star_class = "VI"
        elif roll == 18:
            roll = dice.d6(3)
            if roll == 3:
                roll = dice.d100()
                if roll <= 33:
                   self.star_class = "Ia"
                else:
                   self.star_class = "Ib"
            elif roll == 4:
                self.star_class = "II"
            elif roll >= 5 and roll <= 12:
                self.star_class = "III"
            else:
                self.star_class = "IV"
        else:
            self.star_class = "V"
            
    def determine_mainseq_type(self):
        roll = dice.d6(3)
        if roll >= 9 and roll <= 18:
            self.star_type = "M"
        else:
            if roll == 3:
                self.star_type = "O"
            elif roll == 4:
                self.star_type = "B"
            elif roll == 5:
                self.star_type = "A"
            elif roll == 6:
                self.star_type = "F"
            elif roll == 7:
                self.star_type = "G"
            else:
                self.star_type = "K"
                
    def determine_giant_type(self):
        done = False
        while not done:
            roll = dice.d6(2)
            if roll == 2:
                self.star_type = "O"
            elif roll == 3:
                self.star_type = "M"
            elif roll == 4 or roll == 5:
                self.star_type = "B"
            elif roll >= 6 and roll <= 9:
                self.star_type = "K"
            else:
                self.star_type = "A"
            if self.star_type != "O" and self.star_type != "M":
                done = True
                
            # an excepttion is that if type O, class II, III, and IV do not exist, and type M, class IV as well. Reroll
            # 
            else:
                if self.star_type == "M" and self.star_class != "IV":
                    done = True
                elif self.star_type == "O" and (self.star_class == "Ia" or self.star_class == "Ib"):
                    done = True
                    
    def determine_dwarf_type(self):
        roll = dice.d6()
        if roll == 1:
            self.star_type = "G"
        elif roll == 2:
            self.star_type = "K"
        else:
            self.star_type = "M"
            
    def generate_orbital_bodies(self):
        star_data = (self.orbital_object_data[self.star_type])[self.star_class]
        self.stellar_mass = star_data[0]
        self.biozone = star_data[1]
        self.inner_limit = star_data[2]
        self.stellar_radius = star_data[3]
        self.planets_on = star_data[4]
        self.num_orbits = star_data[5]
        self.life_roll_mod = star_data[6]

    def generate(self):
        self.determine_star_class()
        if self.star_class == "V":
            self.determine_mainseq_type()
        elif self.star_class in [ "Ia", "Ib", "II", "III", "IV" ]:
            self.determine_giant_type()
        elif self.star_class == "D":
            self.determine_dwarf_type()
        self.generate_orbital_bodies()
            
        
        
        
    
class Planet:
    def __init__(self):
        pass
    
    def generate(self, num_planets = 0):
        pass
    
if __name__ == "__main__":
    universe = Universe()
    universe.generate()