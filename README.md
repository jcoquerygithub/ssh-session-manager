# ssh-session-manager
GTK Application showing a tree view of connection. Starts putty on double click.

This application make use of Glade.
In the code, there are some doc comments to infere type statically helping IDE to do autocomplete:

```python
from gi.repository import Gtk
builder = Gtk.Builder()

#: :type: Gtk.TreeStore
server_store = builder.get_object("server_store")
```

