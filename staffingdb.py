import sqlite3           
# Class definitions sqlite

class ProjectAdd:
    def __init__(self, name, address, projectname, projecttype, cost, time_to_market, criticallity, timezone, complexity, expertise, laws
                , availability, innovation, scalability):
        self.name = name
        self.address = address
        self.projectname = projectname
        self.projecttype = projecttype
        self.cost = cost
        self.time_to_market = time_to_market
        self.criticallity = criticallity
        self.timezone = timezone
        self.complexity = complexity
        self.expertise = expertise
        self.laws = laws
        self.availability = availability
        self.innovation = innovation
        self.scalability = scalability

    def save(self):
        conn = sqlite3.connect('Staffing.db')
        c = conn.cursor()
        # Create tables if they don't exist
        c.execute('''CREATE TABLE IF NOT EXISTS projectdetail 
                    (name text, address text, projectname text, projecttype text, cost int, time_to_market text, criticallity int, timezone int, complexity int, expertise int, laws int
                , availability int, innovation int, scalability int)''')
        c.execute('''INSERT INTO projectdetail (name, address, projectname, projecttype, cost, time_to_market, criticallity, timezone, complexity, expertise, laws
                , availability, innovation, scalability) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                  (self.name, self.address, self.projectname, self.projecttype, self.cost, self.time_to_market, self.criticallity, self.timezone, self.complexity, self.expertise
                   , self.laws, self.availability, self.innovation, self.scalability))
        conn.commit()
