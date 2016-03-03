#!/usr/bin/env python
 
import os
from jinja2 import Environment, FileSystemLoader
import sys

sys.path.append(os.getcwd()+'/resumeSections')

from resume_objective import *
from work_experience import genWorkExperienceList
from education import genEducationList
from computer_skills import genComputerSkills
from other_information import genAwardsAndRecomendations, \
                              genLanguages, \
                              genOtherQualifications

from contacts import *
from positionInfo import getPosition, allPositions

CVSection = '\\newcommand{\CVSection}[1]{\Large\\textbf{#1}\par\MiniSep\\normalsize\\normalfont}'

CVItem = '\\newcommand{\CVItem}[1]{\\textbf{\color{RoyalBlue} #1}}'


def latex_url(link):
    return '\url{'+link+'}'

def latex_href(link, text):
    return '\href{'+link+'}{'+text+'}'

def latex_email(link):
    return '\href{mailto:'+link+'}{'+link+'}'

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'latexTemplates')),
    trim_blocks=False)
TEMPLATE_ENVIRONMENT.globals['latex_href'] = latex_href
TEMPLATE_ENVIRONMENT.globals['latex_url'] = latex_url
TEMPLATE_ENVIRONMENT.globals['latex_email'] = latex_email
 
 
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 
 
def createResumeTemplate(objetiveID='', template='resumeDesigner.template'):

    fname = 'resumeAdrianGarcia.tex'

    templateName = 'resumeDesignerTex.template'
    resumeDict = {}
    resumeDict['CVItem'] = CVItem
    resumeDict['CVSection'] = CVSection
    resumeDict['contacts'] = contacts
    resumeDict['jobs'] = genWorkExperienceList()
    resumeDict['school'] = genEducationList()
    resumeDict['compuSkills'] = genComputerSkills()
    resumeDict['awards'] = genAwardsAndRecomendations()
    resumeDict['languages'] = genLanguages()
    resumeDict['other'] = genOtherQualifications()
    resumeDict['position'] = getPosition()
    
    with open(fname, 'w') as f:
        html = render_template(templateName, resumeDict)
        f.write(html)

def createCoverLetter(objetiveID='', template='coverLetter.template'):

    fname = 'coverLetterAdrianGarcia.tex'

    templateName = 'coverLetter.template'
    resumeDict = {}
    resumeDict['contacts'] = contacts
    resumeDict['position'] = getPosition()
    
    with open(fname, 'w') as f:
        html = render_template(templateName, resumeDict)
        f.write(html)

def main():
    createResumeTemplate()
    createCoverLetter()
 
########################################
 
if __name__ == '__main__':
    main()
