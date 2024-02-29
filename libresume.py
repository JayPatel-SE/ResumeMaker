from file_names import *
from template_data import *

def GetLatexTemplate(file_name):
    ret_str = ''
    with open(file_name, 'r') as file:
        for line in file:
            ret_str += line
    return ret_str
    
def FillLatexTemplate(holders, values, file_name):
    latex_str = GetLatexTemplate(file_name)
    # TODO: make sure size of edu_holder and edu_value is the same
    for i in range(len(holders)):
        latex_str = latex_str.replace(holders[i], values[i])
    return latex_str

def GenerateLatexNoSection(holders, values, file_name):
    return GenerateLatexSection(holders, values, file_name, "n/a")

def GenerateLatexSection(holders, values, file_name, sec_name):
    section = FillLatexTemplate(holders, values, file_name)
    if (sec_name != "n/a"):
        section = AddDataToSection(sec_name, section)
    return section

def GenerateSkillsList(values):
    list_str = ''
    for v in values:
        list_str = list_str + GenerateLatexNoSection(
            skill_category_holders, v, skill_category_file)
    return list_str

def GenerateExperienceDescription(descs):
    descs_str = ''
    for desc in descs:
        descs_str = descs_str + GenerateLatexNoSection(
            experience_description_holders, [desc], experience_description_file)
    return descs_str

def AddDataToSection(sec_name, section):
    sec_values = [sec_name, section]
    return FillLatexTemplate(sec_holders, sec_values, sec_file)
    
def GenerateSkillsSection(values):
    skills = GenerateSkillsList(values)
    return GenerateLatexNoSection(skills_and_awards_holders, [skills], skill_and_awards_section_file)

def GenerateResume(resume_file_name, sections):
    resume_content = ''
    for item in sections:
        resume_content = resume_content + item + "\n"
        
    resume = GenerateLatexNoSection(setup_holders, [resume_content], setup_file)
    file_name = "output/" + resume_file_name + ".tex"
    with open(file_name, 'w') as file:
        # Write content to the file
        file.write(resume)
    print(resume)
    