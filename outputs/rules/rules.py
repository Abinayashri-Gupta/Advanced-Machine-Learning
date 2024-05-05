def findDecision(obj): #obj[0]: species, obj[1]: body_wt, obj[2]: brain_wt, obj[3]: non_dreaming, obj[4]: dreaming, obj[5]: total_sleep, obj[6]: life_span, obj[7]: gestation, obj[8]: predation, obj[9]: exposure
	# {"feature": "species", "instances": 62, "metric_value": 1.4296, "depth": 1}
	if obj[0] == 'Africanelephant':
		return 3
	elif obj[0] == 'Raccoon':
		return 2
	elif obj[0] == 'Man':
		return 1
	elif obj[0] == 'Molerat':
		return 1
	elif obj[0] == 'Mountainbeaver':
		return 3
	elif obj[0] == 'Mouse':
		return 3
	elif obj[0] == 'Muskshrew':
		return 3
	elif obj[0] == 'NAmericanopossum':
		return 1
	elif obj[0] == 'Nine-bandedarmadillo':
		return 1
	elif obj[0] == 'Okapi':
		return 5
	elif obj[0] == 'Owlmonkey':
		return 2
	elif obj[0] == 'Patasmonkey':
		return 4
	elif obj[0] == 'Phanlanger':
		return 2
	elif obj[0] == 'Pig':
		return 4
	elif obj[0] == 'Rabbit':
		return 5
	elif obj[0] == 'Rat':
		return 3
	elif obj[0] == 'Africangiantpouchedrat':
		return 3
	elif obj[0] == 'Redfox':
		return 1
	elif obj[0] == 'Rhesusmonkey':
		return 2
	elif obj[0] == 'Rockhyrax(Heterob)':
		return 2
	elif obj[0] == 'Rockhyrax(Procaviahab)':
		return 3
	elif obj[0] == 'Roedeer':
		return 5
	elif obj[0] == 'Sheep':
		return 5
	elif obj[0] == 'Slowloris':
		return 2
	elif obj[0] == 'Starnosedmole':
		return 2
	elif obj[0] == 'Tenrec':
		return 2
	elif obj[0] == 'Treehyrax':
		return 3
	elif obj[0] == 'Treeshrew':
		return 2
	elif obj[0] == 'Vervet':
		return 4
	elif obj[0] == 'Wateropossum':
		return 1
	elif obj[0] == 'Littlebrownbat':
		return 1
	elif obj[0] == 'Lessershort-tailedshrew':
		return 4
	elif obj[0] == 'Kangaroo':
		return 4
	elif obj[0] == 'Jaguar':
		return 1
	elif obj[0] == 'ArcticFox':
		return 1
	elif obj[0] == 'Arcticgroundsquirrel':
		return 3
	elif obj[0] == 'Asianelephant':
		return 4
	elif obj[0] == 'Baboon':
		return 4
	elif obj[0] == 'Bigbrownbat':
		return 1
	elif obj[0] == 'Braziliantapir':
		return 4
	elif obj[0] == 'Cat':
		return 1
	elif obj[0] == 'Chimpanzee':
		return 1
	elif obj[0] == 'Chinchilla':
		return 4
	elif obj[0] == 'Cow':
		return 5
	elif obj[0] == 'Deserthedgehog':
		return 2
	elif obj[0] == 'Donkey':
		return 5
	elif obj[0] == 'EasternAmericanmole':
		return 1
	elif obj[0] == 'Echidna':
		return 2
	elif obj[0] == 'Europeanhedgehog':
		return 2
	elif obj[0] == 'Galago':
		return 2
	elif obj[0] == 'Genet':
		return 1
	elif obj[0] == 'Giantarmadillo':
		return 1
	elif obj[0] == 'Giraffe':
		return 5
	elif obj[0] == 'Goat':
		return 5
	elif obj[0] == 'Goldenhamster':
		return 2
	elif obj[0] == 'Gorilla':
		return 1
	elif obj[0] == 'Grayseal':
		return 1
	elif obj[0] == 'Graywolf':
		return 1
	elif obj[0] == 'Groundsquirrel':
		return 3
	elif obj[0] == 'Guineapig':
		return 4
	elif obj[0] == 'Horse':
		return 5
	elif obj[0] == 'Yellow-belliedmarmot':
		return 1
	else: return 1.0
