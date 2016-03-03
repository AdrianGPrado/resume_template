import contacts as c

def genEducationList():
    studies = [genMS(), genBS(), genErasmus()]
    return studies

def genMS():
    edu = {}
    edu["studiID"] = "MS"
    edu["mayor"] = "M.S. Applied Mathematics"
    edu["title"] = "Mathematical Modeling, Statistics and Mathematical Computation."
    edu["location"] = "Zaragoza's Universty "+chr(92)+"& UPV/EHU"
    edu["dates"] = "2011 - 2012"
    edu["achievements"] = ["M.S. Thesis: CUDA implementation of integration rules within an hp-Finite Element code, qualification 9.6 over 10.",
                           "Main study areas: Mathematical Modeling, Statistics and Mathematical Computation. Data mining, Neuronal Networks, Model Optimization, and Simulation."]

    ref1 = {"refName": c.contacts['DP']['name'],
            "refEmail": c.contacts['DP']['email']}
    ref2 = {"refName": c.contacts['RC']['name'],
            "refEmail": c.contacts['RC']['email']}

    edu["references"] = [ref1, ref2]

    return edu

def genBS():
    edu = {}
    edu["studiID"] = "BS"
    edu["mayor"] = "B.S. Theoretical Physics"
    edu["title"] = "Theoretical Physics Specialization 5yr Program"
    edu["location"] = "Zaragoza's Universty"
    edu["dates"] = "2001 - 2010"
    edu["achievements"] = ["Besides learning how to analyze different physical phenomena, and the corresponding governing laws, differential and integral calculus, mathematical models, non linear dynamical equations.",
        " I learn to develop physical simulations using C/C++. And among all those projects, the simulation of ESEO satellite orbit injection is my greatest achievement."]
    ref = {}

    edu["references"] = []

    return edu

def genErasmus():
    edu = {}
    edu["studiID"] = "Erasmus"
    edu["mayor"] = "Telecom"
    edu["title"] = "Exchange Program"
    edu["location"] = "Saint-Etienne, France"
    edu["dates"] = "2007 - 2008"
    edu["achievements"] = ["Throughout this program I had telecom engineer formation: guide of waves, antennas, optical fibers."]
    ref = {}

    edu["references"] = []

    return edu

def main():
    studies = genEducationList()

    for edu in studies:
        print " -- "
        print edu['mayor'], ".", edu['title'], ".", edu['location'], ".", edu['dates']
        print edu['achievements']
        if len(edu['references']) > 0:
            for ref in edu['references']:
                print "Refence: ", ref['refName'], ref['refEmail']
            print " "

if __name__ == '__main__':
    main()


