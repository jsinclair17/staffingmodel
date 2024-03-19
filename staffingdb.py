import sqlite3           
import math
# Class definitions sqlite

class ProjectAdd:
    def __init__(self, 
                 #name, address, projectname, projecttype, 
                 cost, time_to_market
                 #, criticallity
                , timezone, complexity, expertise, laws
                , availability, innovation
                #, scalability
                ):
        # """ self.name = name
        # self.address = address
        # self.projectname = projectname
        # self.projecttype = projecttype """
        self.cost = cost
        self.time_to_market = time_to_market
        #self.criticallity = criticallity
        self.timezone = timezone
        self.complexity = complexity
        self.expertise = expertise
        self.laws = laws
        self.availability = availability
        self.innovation = innovation
        #self.scalability = scalability

    def save(self):
        conn = sqlite3.connect('Staffing.db')
        c = conn.cursor()
        # Create tables if they don't exist
        c.execute('''CREATE TABLE IF NOT EXISTS projectdetail 
                    (name text, address text, projectname text, projecttype text, cost int, time_to_market text, timezone int, complexity int, expertise int, laws int
                , availability int, innovation int)''')
        c.execute('''INSERT INTO projectdetail (name, address, projectname, projecttype, cost, time_to_market, timezone, complexity, expertise, laws
                , availability, innovation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                  (self.name, self.address, self.projectname, self.projecttype, self.cost, self.time_to_market
                   #, self.criticallity
                   , self.timezone, self.complexity, self.expertise
                   , self.laws, self.availability, self.innovation
                   #, self.scalability
                   ))
        conn.commit()

    def getspread(self):
        funding_on_shore = 0.2
        funding_off_shore = 0.6
        funding_near_shore = 0.45
        timezone_on_shore = 0.4
        timezone_off_shore = 0.15
        timezone_near_shore = 0.225
        expertise_on_shore = 0.4
        expertise_off_shore = 0.15
        expertise_near_shore = 0.15
        laws_on_shore = 0.6
        laws_off_shore = 0.15
        laws_near_shore = 0.15
        response_on_shore = 0.5
        response_off_shore = 0.075
        response_near_shore = 0.225
        innovate_on_shore = 0.5
        innovate_off_shore = 0.15
        innovate_near_shore = 0.15
        on_shore_cost = 210
        near_shore_cost = 140
        off_shore_cost = 110
        on_shore_score = (self.cost * funding_on_shore) + (timezone_on_shore * self.timezone) + (self.expertise*expertise_on_shore) + (self.laws*laws_on_shore) + (self.availability*response_on_shore) + (self.innovation * innovate_on_shore)
        near_shore_score = (funding_near_shore*(6-self.cost)) + (timezone_near_shore*(6 - self.timezone)) + (expertise_near_shore*self.expertise) + (laws_near_shore*(6 - self.laws)) + (response_near_shore*(6 - self.availability)) + (innovate_near_shore*self.innovation)
        off_shore_score = (funding_off_shore*(6-self.cost)) + (timezone_off_shore*(5 - self.timezone)) + (expertise_off_shore*self.expertise) + (laws_off_shore*(6 - self.laws)) + (response_off_shore*(5 - self.availability)) + (innovate_off_shore*self.innovation)
        on_shore_spread = on_shore_score/(on_shore_score + near_shore_score + off_shore_score)
        off_shore_spread = off_shore_score/(on_shore_score + near_shore_score + off_shore_score)
        near_shore_spread = near_shore_score/(on_shore_score + near_shore_score + off_shore_score)
        low_savings_calc = '{:.0%}'.format((1-(((on_shore_cost*on_shore_spread) + (off_shore_cost*off_shore_spread) + (near_shore_cost*near_shore_spread) )/ on_shore_cost))-0.05)
        high_savings_calc = '{:.0%}'.format((1-(((on_shore_cost*on_shore_spread) + (off_shore_cost*off_shore_spread) + (near_shore_cost*near_shore_spread) )/ on_shore_cost))+0.05) 
        return [[('On Shore',round(on_shore_spread,2)), ('Off Shore', round(off_shore_spread,2)) , ('Near Shore', round(near_shore_spread,2))],(low_savings_calc, high_savings_calc)]
       