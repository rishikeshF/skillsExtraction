import streamlit as st
import pickle
import string

skills_dict = pickle.load(open('skills_dict_v2.pickle', 'rb'))

roles_tuple = list(list(skills_dict.keys()))
roles_tuple = sorted(tuple([string.capwords(x) for x in roles_tuple if str(x) != 'nan']))
roles_tuple = list(set(roles_tuple))
roles_tuple = sorted(roles_tuple)
skills_set = set()
for subset in list(skills_dict.values()):
	skills_set = skills_set.union(subset)
skills_list = sorted([ x for x in skills_set ])
skills_list = list(set(skills_list))
skills_list = sorted(skills_list)

def main():
	"""main function for skill recommendation engine"""
	
	st.title("Welcome to skill recommendation engine")
	with st.form("my_form", clear_on_submit=True):

		target_role = st.selectbox(
			'Please select the role you are targetting',
			roles_tuple)


		user_skills = st.multiselect(
			'Please select all the skills you have from the drop down below :',
			skills_list)

		st.write('Your target role is ', target_role)
		st.write('\nYou currently have following skills :')
		st.write(', '.join(user_skills))

		submitted = st.form_submit_button("Submit")

	if submitted: 
		required_skills = skills_dict[target_role]
		suggested_skills = list(set(required_skills) - set(user_skills))
		st.write('Skills that you need to acquire are :')
		st.write(', '.join(suggested_skills))

if __name__ == '__main__' : 
	main()