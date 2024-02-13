# Place code below to do the munging part of this assignment.
def conver(temperature):
    return ((temperature/100) * 1.8)

def clean():
    f = open("./data/GLB.Ts+dSST.txt", "r")
    w = open("./data/clean_data.csv", "w")
    heading = False
    for line in f:
        if line[0:4] == "Year":
            if not heading:
                heading = True
                h = ""
                data = line.split()
                for i in range(len(data) - 1):
                    if i == 0:
                        h += data[i]
                    else:
                        h += "," + data[i]
                h += "\n"
                w.write(h)
        elif line[0:4].isdigit():
            t = ""
            data = line.split()
            for i in range(len(data) - 1):
                if i == 0:
                    t += data[i]
                else:
                    if data[i][0:1] != "*":
                        num = conver(float(data[i]))
                        num_ = format(num,'.1f')
                        t += "," + num_
                    else:
                        t += ",N/A"
            t += "\n"
            w.write(t)
    w.close()

clean()
