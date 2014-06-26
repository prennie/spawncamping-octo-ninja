from mean_sightings import get_sightings

filename = 'sightings_tab_sm.csv'

def test_water_is_correct():
	watrec,watmean = get_sightings(filename,'Water')
	assert watrec==2, 'Number of records for water is wrong'
	assert watmean==17, 'Mean counts for water is wrong'

def test_clay_is_correct():
        clayrec,claymean = get_sightings(filename,'Clay')
        assert clayrec==2, 'Number of records for clay is wrong'
        assert claymean==25.5, 'Mean counts for clay is wrong'

def test_notpresent_is_correct():
	norec,nomean = get_sightings(filename,'Not Present')
	assert norec==0, 'Biosignature not present has no records'
	assert nomean==0, 'Mean is not present for missing biosignatures'

