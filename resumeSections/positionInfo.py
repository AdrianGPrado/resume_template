

# ------------------------------------------------------------------------------
positions = {}

# ------------------------------------------------------------------------------
positions['default'] = {
                'objective': '',

                'comName':  '',
                'jobName':  '',

                'comURL':   '',
                'jobURL':   '',

                'jobID':    '',
                'location': '',
                'salary':   '',
                'status':   []
               }

# ------------------------------------------------------------------------------
positions['defaultCPP'] = {
                'objective': '',

                'comName':  '',
                'jobName':  'C++ Developer',

                'comURL':   '',
                'jobURL':   '',

                'jobID':    '',
                'location': '',
                'salary':   '',
                'status':   []
               }

# ------------------------------------------------------------------------------
positions['defaultHPC'] = {
                'objective': '',

                'comName':  '',
                'jobName':  'HPC Developer',

                'comURL':   '',
                'jobURL':   '',

                'jobID':    '',
                'location': '',
                'salary':   '',
                'status':   []
               }

JOINDEVTEAM = ""

def getPosition():
    positionKey = 'default'
    pos = positions[positionKey]
    pos['objective'] = JOINDEVTEAM
    return pos

def allPositions():
    return positions

def main():
    for k in positions:
        print "---------------------------"
        print "Key: ", k
        v = getPosition(k)
        print v['comName'], ": ", v['jobName']
        print 'location: ', v['location']
        print 'salary: ', v['salary']
        print 'status: '
        for s in v['status']:
            print '\t', s
        print " "


if __name__ == '__main__':
    main()
