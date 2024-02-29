from libresume import *

# HEADER SECTION
fname = "Khushee"
lname = "Patel"
p_number = "(431) 998 5560"
email = "patek64@mcmaster.ca"
linkedin = "linkedin.com/in/Khushee-Patel"
header_values = [fname, lname, p_number, email, linkedin]

# EDUCATION SECTION
name = 'McMaster University'
location = 'Hamilton, ON'
education = 'B. Eng Software Engineering'
start_date = '2019'
end_date = '2024'
gpa = "3.9"
edu_values = [name, location, education, start_date, end_date, gpa]

# EXPERIENCE SECTION
# == VP Academics
vp_title = 'Vice President of Academic Affairs'
vp_start_date = 'May 2023'
vp_end_date = 'Present'
vp_org = 'McMaster Humanities Society'
vp_location = 'Hamilton, ON'
## === POSITION DESCRPTION
vp_desc1 = 'Coordinate and lead initiatives to enhance academic support services for students.'
vp_desc2 = 'Actively overseeing all functioning of the Mentorship Coordinators and the Mentorship Initiative.'
vp_desc3 = 'Collaborate with the President to execute tasks critical to the success of the organization.'
vp_desc4 = 'Hired and trained 2 Mentorship Coordinators for the Humanities Mentorship Initiative.'
vp_descs = [vp_desc1, vp_desc2, vp_desc3, vp_desc4]
vp_descs_str = GenerateExperienceDescription(vp_descs)
vp_experience_values = [vp_title, vp_start_date, vp_end_date, vp_org, vp_location, vp_descs_str]
    
    
# LEADERSHIP AND ACTIVITIES
# == Grants Committee
gc_title = 'Grants Commitee'
gc_start_date = 'February 2020'
gc_end_date = 'August 2022'
gc_org = 'United Way Winnipeg'
gc_location = 'Winnipeg, MB'
## == POSITION DESCRIPTION
gc_desc1 = 'Tasked with reviewing and approving funding for grassroot projects which require financial aid, on behalf of United Way Winnipeg’s Youth Committee.'
gc_desc2 = 'Served as a liaison between Youth United and approved projects to ensure they were on track, and received any form of support from our end.'
gc_descs = [gc_desc1, gc_desc2]
gc_descs_str = GenerateExperienceDescription(gc_descs)
gc_experience_values = [gc_title, gc_start_date, gc_end_date, gc_org, gc_location, gc_descs_str]

# SKILLS AND AWARDS
lan_skill_cat = 'Languages'
lan_skill_list = 'English, Gujarati, Hindi, Urdu, and Punjabi'
lan_skill_cat_values = [lan_skill_cat, lan_skill_list]

skill_skill_cat = "Skills"
skill_skill_list = 'Communication and project management skills from leading teams, hiring and training new team members, and being a quick learner'
skill_skill_cat_values = [skill_skill_cat, skill_skill_list]

tech_skill_cat = 'Technical'
tech_skill_list = 'Website Management, LaTeX, Zoom, PowerPoint, Word, Excel, Teams, Microsoft Project'
tech_skill_cat_values = [tech_skill_cat, tech_skill_list]


header_section = GenerateLatexNoSection(header_holders, header_values, header_file)
edu_section = GenerateLatexSection(edu_holders, edu_values, edu_file, "Education")
vp_exp_section = GenerateLatexNoSection(experience_holders, vp_experience_values, experience_file)
gc_exp_section = GenerateLatexNoSection(experience_holders, gc_experience_values, experience_file)
exp_section = AddDataToSection("Experience", vp_exp_section)
leadership_activities_section = AddDataToSection("Leadership and Activities", gc_exp_section)
skills = GenerateSkillsSection([lan_skill_cat_values, skill_skill_cat_values, tech_skill_cat_values])

# print(exp_section)

GenerateResume("Resume", [header_section, edu_section, exp_section, leadership_activities_section, skills])
