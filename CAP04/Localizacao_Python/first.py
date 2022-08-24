from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'

print(Geocoder('AIzaSyC6866AgRXcrDA7av7ol8QzkGqbgVMl73s').geocode(endereco).coordinates)
