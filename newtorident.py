import stem.connection 
from stem import Signal

con = stem.connection.connect_socket_file('/var/run/tro/control')
if con is None: con = stem.connection.connect_socket_file('/var/run/tor/control')
con.signal(Signal.NEWNYM)

