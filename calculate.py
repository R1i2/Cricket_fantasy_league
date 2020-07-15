def Bowling(wickets,overs,runs):
    wickets=int(wickets)
    overs=int(overs)
    runs=int(runs)
    if overs:
        economy=runs/overs
    else:
        economy=1000
    point=0
    if economy>3.5 and economy<=4.5:
        point+=4
    elif economy>2 and economy<=3.5:
        point+=7
    elif economy<=2:
        point+=10
    if wickets:
        count=0
        while count!=wickets:
            count+=1
            point+=10
        if wickets>=3 and wickets<5:
            point+=5
        elif wickets>=5:
            point+=10
    return point
def Batting(runs,balls,fours,sixes):
    runs=int(runs)
    balls=int(balls)
    fours=int(fours)
    sixes=int(sixes)
    if balls:
        strikeRate=(runs/balls)*100
    else:
        strikeRate=0
    point=0
    if strikeRate>=80 and strikeRate<100:
        point+=2
    elif strikeRate>=100:
        point+=4
    if fours:
        count1=0
        while count1!=fours:
            count1+=1
            point+=1
    if sixes:
        count1=0
        while count1!=sixes:
            count1+=1
            point+=2
    if runs>=50:
        point+=5
    if runs>=100:
        point+=10
    point+=runs//2
    return point
def Fielding(catch,stumping,RO):
    point=0
    if catch:
        count=0
        while count!=catch:
            count+=1
            point+=10
    if stumping:
        count=0
        while count!=stumping:
            count+=1
            point+=10
    if RO:
        count=0
        while count!=RO:
            count+=1
            point+=10
    return point