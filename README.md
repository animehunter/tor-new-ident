One liner for changing tor identity
Note: must have STEM installed

echo -e "import stem.connection\nfrom stem import Signal\ncon = stem.connection.connect_socket_file('/var/run/tro/control')\nif con is None: con = stem.connection.connect_socket_file('/var/run/tor/control')\ncon.signal(Signal.NEWNYM)" | python

