import os
import subprocess

import gi
import xml.etree.ElementTree as Et
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonClicked(self, button):
        print("Hello World!")

    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            server_view = builder.get_object("server_tree_view")
            if server_view.row_expanded(selection.get_selected_rows()[1][0]):
                server_view.collapse_row(selection.get_selected_rows()[1][0])
            else:
                server_view.expand_row(selection.get_selected_rows()[1][0], False)
            print("You selected", model[treeiter][0])

    def on_row_activated(self, view, path, column):
        model = view.get_model()
        treeiter = model.get_iter(path)
        if treeiter is not None:
            print("You db click on", model[treeiter][0])
            subprocess.Popen(['/usr/bin/putty',
                              '-title', get_path_unix_style(model, treeiter),
                              '-l', model[treeiter][2],
                              model[treeiter][1]])


def add_to_store(store, parent, node):
    store_node = store.append(parent, [node.get('Name'), node.get('Hostname'), node.get('Username')])
    if len(node.getchildren()) != 0:
        for subnodes in node:
            add_to_store(store, store_node, subnodes)

def get_path_unix_style(model, node):
    parent = model.iter_parent(node)
    if parent is None:
        return model[node][0]
    else:
        return '{}/{}'.format(get_path_unix_style(model, parent),model[node][0])

builder = Gtk.Builder()
builder.add_from_file("ssh-session-manager.glade")

#: :type: Gtk.TreeStore
server_store = builder.get_object("server_store")
if os.path.isfile('../../../progs/mremoteng/confCons.xml'):
    tree = Et.parse('../../../progs/mremoteng/confCons.xml')

    #: :type: Et.ElementTree
    root = tree.getroot()
    add_to_store(server_store, None, root)

builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.show_all()
Gtk.main()
