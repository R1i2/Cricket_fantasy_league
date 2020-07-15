import sqlite3
MyMatch=sqlite3.connect("database.db")
curmatch=MyMatch.cursor()
# sql="""CREATE TABLE match(
# player TEXT PRIMARY KEY REFERENCES stats(player) ,
# Scored INTEGER,
# Faced INTEGER,
# Fours INTEGER,
# Sixes INTEGER,
# Bowled INTEGER,
# Maiden INTEGER,
# Given INTEGER,
# Wkts INTEGER,
# Catches INTEGER,
# Stumping INTEGER,
# RO INTEGER
# )"""
# curmatch.execute(sql)
# sql="""CREATE TABLE stats(
#     player TEXT PRIMARY KEY,
#     matches INTEGER,
#     runs INTEGER,
#     century INTEGER,
#     half_century INTEGER,
#     value INTEGER,
#     ctg TEXT
# )"""
# curmatch.execute(sql)
print("Enter the values for match table \n")
while True:
    player=input(" the name of player: ")
    scored=int(input("Runs scored: "))
    faced=int(input("Bowl faced: "))
    fours=int(input("Fours scored: "))
    sixes=int(input("Sixes scored: "))
    bowled=int(input("Overs bowled"))
    maiden=int(input("Maiden overs bowled: "))
    given=int(input("Runs given: "))
    wkts=int(input("Wickets taken: "))
    catches=int(input("Catches taken: "))
    stumping=int(input("Stumpings: "))
    ro=int(input("Run outs: "))
    value=int(input("Value: "))
    matches=int(input("Matches: "))
    runs=int(input("Runs: "))
    century=int(input("100s: "))
    half_century=int(input("50s: "))
    role=input("Enter role: ")
    try:
        curmatch.execute("""INSERT INTO match(
            player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RO
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);""",(player,scored,faced,fours,sixes,bowled,maiden,given,wkts,catches,stumping,ro))
        MyMatch.commit()
        curmatch.execute("""INSERT INTO stats(
            player,matches,runs,century,half_century,value,ctg
        ) VALUES (?,?,?,?,?,?,?);
        """,(player,matches,runs,century,half_century,value,role))
        MyMatch.commit()
        res=input("Do you want to add more Items?Y/N: ")
        if res=="N":
            break
        print("Record successfully added\n")
    except:
        print('Error while inserting\n')
        MyMatch.rollback()
MyMatch.close()
