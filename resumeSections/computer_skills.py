# ------------------------------------------------------------------------------
#  COMPUTER SKILLS
# ------------------------------------------------------------------------------

def genComputerSkills():
    advanced = {'grade': 'Advanced', 'skills': ['C', 'C++', 'Python', 
                                                'Fortran 90/95', 'Linux', 
                                                'R', 'Weka', 'Optimization', 
                                                'Git', 'LaTeX', 'Octave', 
                                                'Matlab']}
    compilers = {'grade': 'Compilers', 'skills': ['GNU', 'INTEL',
                                                  'PGI', 'CRAY']}
    intermediate = {'grade': 'Intermediate', 'skills': ['BASH', 'MPI', 'CUDA', 
                                                        'openMPI', 
                                                        'Design Patterns', 
                                                        'Qt', 'MYSQL',
                                                        'Mathematica']}
    basic = {'grade': 'Basic', 'skills': ['java', 'javaScript']}

    skills = [advanced, compilers, intermediate, basic]
    return skills

# %------------------------------------------------

# \EndCVSection

def main():
    skills = genComputerSkills()

    for skill in skills:
        print " -- "
        print skill['grade'], " ".join(skill['skills'])

if __name__ == '__main__':
    main()
