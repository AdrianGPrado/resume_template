# from hyper_text_and_kinks.py import *

# -------------------------------------------------------------------------------
# OTHER INFORMATION
# -------------------------------------------------------------------------------
def genOtherInformation():
    return [genAwardsAndRecomendations(), 
            genLanguages(),
            genOtherQualifications()]

def genAwardsAndRecomendations():
    return {'name': 'Awards \& Recomendations',
            'items':
                [
                    {
                     'txtA': '2014',
                     'txtB': 'Recommendation Letter, from David Holman, for my job at XFlow-CFD.',
                     'link': 'https://goo.gl/xm6PnX'
                    },
                    # {
                    #  'txtA': '2012',
                    #  'txtB': 'M.S. Thesis: CUDA implementation of integration rules within an hp-Finite Element code, qualification 9.6 over 10.'
                    # },
                    {
                     'txtA': '2012',
                     'txtB': 'Recommendation Letter from David Pardo, for my work developing a FEM integration method in CUDA.',
                     'link': 'http://goo.gl/DDasq'
                    },
                    {
                     'txtA': '2011',
                     'txtB': 'Recommendation Letter from my project manager at Tb-Solutions.',
                     'link': 'http://goo.gl/c0Kh1'
                    },
                    {
                      'txtA': '2010',
                      'txtB': 'Recommendation Letter. from professor Alberto Abad, (ESEO Project).',
                      'link': 'http://goo.gl/GdAr5'
                    }
                ]
            }

def genLanguages():
    return {'name': 'Languages',
            'items':
                [
                    {
                     'txtA': 'Spanish',
                     'txtB': 'Mothertongue.'
                    },
                    {
                     'txtA': 'English',
                     'txtB': 'Full professional communication. (C1).'
                    },
                    {
                     'txtA': 'French',
                     'txtB': 'Competent communication, non full professional. (B1).'
                    }
                ]
            }


def genOtherQualifications():
    return {'name': 'Other qualifications',
            'items':
                [
                    {
                     'txtA': '2015',
                     'txtB': 'MITx Introduction to Computational Thinking and Data Science.',
                     'link': 'https://courses.edx.org/certificates/ee1df99f492d461e80c7de060635d6e2'
                    },
                    {
                     'txtA': '2015',
                     'txtB': 'Toast Master international. Organization focused on the public speech and leadership personal skills development.',
                     'link': 'https://www.toastmasters.org/'
                    },
                    {
                     'txtA': '2010',
                     'txtB': 'Applied course on Advanced Computation.'
                    },
                    {
                     'txtA': '2010',
                     'txtB': 'Course on Renewable Energies.'
                    },
                    {
                     'txtA': '08-11',
                     'txtB': 'Member of LEEM group. Laboratory to Experimentation in Space and Microgravity.',
                     'link': 'http://www.leem.es/'
                    },
                    {
                     'txtA': '01-05',
                     'txtB': 'Member of the student representatives.'
                    }
                ]
            }


def main():
    otherInfo = genOtherInformation()

    for info in otherInfo:
        print ' -- '
        print info['name']
        for item in info['items']:
            print item['txtA'], item['txtB']
            if 'link' in item.keys():
                print item['link']
if __name__ == '__main__':
    main()