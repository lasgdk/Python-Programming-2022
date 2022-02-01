import rolo

# test i python kan udføres med "assert"'s som herunder, og køres med kommandoen "pytest"
# mocks and fixtures er to andre emner ifm. pytest, til at simulere ting og til at have testdata
# pytest tester filer der starter filnavnet med test_
# pytest kan give mere info med -v bagefter, verbose

# Skriv testcases først, før indhold af funktioner, så du er sikker på du tester på det rigtige, og ikke bare på det du tror er rigtigt.

def test_insert_person():
    data=[]
    rolo.insert_person(data, "xxx", 'xxx@xx.com', '12341234', '1333-12-31')
    assert data[0]['name'] == 'xxx'

def test_update_person():
    data = rolo.data
    rolo.update_person(data, 'Charlie', tel='1111')
    pers = rolo.find_person(data,'Charlie')
    assert pers['tel'] == '1111'

