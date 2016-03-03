import contacts as c

def genWorkExperienceList():
    jobs = [genJobTotal(), genJobXFlow(), genJobTbSolutions(), genJobESA()]
    return jobs

def genJobTotal():
    pos = {}
    pos["jobID"] = "Total"
    pos["positionName"] = "Professional Trainee at Advance Computing Team"
    pos["company"] = "TOTAL E"+chr(92)+"&P"
    pos["location"] = "Houston, USA"
    pos["dates"] = "2014 - 2015"
    pos["achievements"] = ["Design and implement a new deep underground imaging software application. Based on the Discontinous Galerkin (DG) method, and taking as reference the book Nodal DG Methods. I developed the application with scalability as main target.", "The application main property is that when implemented in parallel the computational time, decreases almost linearly with the number of cores, both in CPU and GPU. I developed the application always taking into account the full development life cycle, from unitary test per module, to version deployment."]
    ref = {"refName": c.contacts['HC']['name'],
           "refEmail": c.contacts['HC']['email']}

    pos["references"] = [ref]

    return pos

def genJobXFlow():
    pos = {}
    pos["jobID"] = "Total"
    pos["positionName"] = "Mathematical Software Developer"
    pos["company"] = "Xflow-CFD"
    pos["location"] = "Madrid, Spain"
    pos["dates"] = "2013 - 2014"
    pos["achievements"] = ["Design and implement an new data representation, along with a new data architecture to communicate the simulation engine and the GUI.", "Maintain and improve the HPC code, so XFlow-CFD fits its requirements of scalability and flexibility."]
    ref = {"refName": c.contacts['DH']['name'],
           "refEmail": c.contacts['DH']['email']}

    pos["references"] = [ref]

    return pos

def genJobTbSolutions():
    pos = {}
    pos["jobID"] = "TbSolutions"
    pos["positionName"] = "Java Developer"
    pos["company"] = "Tb-Solutions"
    pos["location"] = "Zaragoza, Spain"
    pos["dates"] = "Jun-Nov 2011"
    pos["achievements"] = ["Develop statistical analysis tool while improving the server side of Tb-Solutions online banking application."]
    ref = {}

    pos["references"] = []

    return pos

def genJobESA():
    pos = {}
    pos["jobID"] = "ESA"
    pos["positionName"] = "Fellowship ESEO Project"
    pos["company"] = "ESA Student Project"
    pos["location"] = "Zaragoza, Spain"
    pos["dates"] = "2009 - 2010"
    pos["achievements"] = ["I implemented a simulation software to compute the satellite orbit injection and the subsequent orbit to all the mission. ESEO is a ESA (European Space Agency) project.", " I worked in this program inside the Space Mechanical Group, at Zaragoza's University."]
    ref = {"refName": c.contacts['JY']['name'],
           "refEmail": c.contacts['JY']['email']}
    pos["references"] = [ref]
    return pos


def main():
    jobs = genWorkExperienceList()

    for job in jobs:
        print " -- "
        print job['positionName'], ".", job['company'], ".", job['location'], ".", job['dates']
        print job['achievements']
        if len(job['references']) > 0:
            for ref in job['references']:
                print "Refence: ", ref['refName'], ref['refEmail']
            print " "

if __name__ == '__main__':
    main()


