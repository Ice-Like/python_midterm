cost = int(input(""))
sm = [2.10,3.02,4.39,4.97,5.63]
nsm = [2.10,2.68,3.61,4.01,4.50]
smc = 0
nsmc = 0
if cost < 120:
    smc += cost * sm[0]
    nsmc += cost * nsm[0]
else:
    smc += 120 * sm[0]
    nsmc += 120 * nsm[0]

    if cost < 330:
        smc += (cost-120) * sm[1]
        nsmc += (cost-120) * nsm[1]
    else:
        smc += (330-120) * sm[1]
        nsmc += (330-120) * nsm[1]

        if cost < 500:
            smc += (cost-330) * sm[2]
            nsmc += (cost-330) * nsm[2]
        else:
            smc += (500-330) * sm[2]
            nsmc += (500-330) * nsm[2]

            if cost < 700:
                smc += (cost-500) * sm[3]
                nsmc += (cost-500) * nsm[3]
            else:
                smc += (700-500) * sm[3]
                nsmc += (700-500) * nsm[3]
                smc += (cost-700) * sm[4]
                nsmc += (cost-700) * nsm[4]    
print("Summer months:"+str(smc))
print("Non-Summer months:"+str(nsmc))
                    
