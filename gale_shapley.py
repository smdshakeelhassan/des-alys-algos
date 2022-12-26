import random

def PreferNewer(w_pref_list, new_man, old_man):
	if w_pref_list.index(new_man) < w_pref_list.index(old_man):
		return True
	return False 


def GaleShapley(preference_men, preference_women):
	m_prefs = list(preference_men.values())
	w_prefs = list(preference_women.values())
	N = len(m_prefs)
	if N != len(w_prefs):
		raise ValueError("Number of men and women must be equal")

	husb_list = {x:-1 for x in preference_women.keys()}	#dict containing respective husbands of N women, if a val is -1, that woman is free 
	free_men = list(preference_men.keys())			#list of free men
	num_steps = 1
	men_choices = {x:0 for x in preference_men.keys()}	#index of best available proposal for each man	
		
	while free_men:				
		m_idx = random.choice(range(len(free_men)))	#randomly a free man
		man = free_men[m_idx]
		pref_list = preference_men[man]			#preference order of the selected man
		proposal_to = pref_list[men_choices[man]]	#find his best possible proposal		

		print(f"\nStep {num_steps}")
		print(f"Current free men: {free_men}")
		temp_dict = {item:husb_list[item] for item in husb_list if husb_list[item] != -1 }
		print(f"Current engagements: {temp_dict}")
		print(f"Man {man} proposes to his best available choice Woman {proposal_to}")
		
		#if best proposal woman is free, form alliance
		if husb_list[proposal_to] == -1:
			husb_list[proposal_to] = man
			free_men.pop(m_idx)
			men_choices[man] += 1
			num_steps += 1
			print(f"Since Woman {proposal_to} is free, (Woman {proposal_to}, Man {man}) pair is formed.")
		else:
			print(f"Woman {proposal_to} is engaged to Man {husb_list[proposal_to]}")
			if PreferNewer(preference_women[proposal_to], man, husb_list[proposal_to]):
				print(f"Since Woman {proposal_to} prefers new partner, (Woman {proposal_to}, Man {man}) get engaged and Man {husb_list[proposal_to]} becomes free")
				free_men.pop(m_idx)
				free_men.append(husb_list[proposal_to])
				husb_list[proposal_to] = man
				men_choices[man] += 1
				num_steps += 1
			else:
				print(f"Since Woman {proposal_to} prefers existing partner, (Woman {proposal_to}, Man {husb_list[proposal_to]}) remain engaged and Man {man} remains free")
				men_choices[man] += 1
				num_steps += 1
				continue

	return husb_list

if __name__ == "__main__":
	preference_men = {
				# 1: [3,1,2],
				# 2: [1,3,2],
				# 3: [3,1,2],
				'A': ['W','X','Y','Z'],
				'B': ['X','W','Z','Y'],
				'C': ['Y','Z','W','X'],
				'D': ['Z','Y','X','W']
			}
	preference_women = {
				# 1: [1,2,3],
				# 2: [1,2,3],
				# 3: [2,3,1],
				'W': ['D','C','B','A'],
				'X': ['C','D','A','B'],
				'Y': ['B','A','D','C'],
				'Z': ['A','B','C','D']
			}
	print(f"Male Preference lists: \n{preference_men}")
	print(f"Female Preference lists: \n{preference_women}")
	print("\n\n\n")
	result = GaleShapley(preference_men, preference_women)
	
	print(result)
