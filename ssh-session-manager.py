import gi
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
            print("You selected", model[treeiter][0])

    def on_row_activated(self, view, path, column):
        model = view.get_model()
        treeiter = model.get_iter(path)
        if treeiter is not None:
            print("You db click on", model[treeiter][0])


builder = Gtk.Builder()
builder.add_from_file("ssh-session-manager.glade")

books = [["Tolstoy, Leo", "War and Peace", "Anna Karenina"],
         ["Shakespeare, William", "Hamlet", "Macbeth", "Othello"],
         ["Tolkien, J.R.R.", "The Lord of the Rings"]]

#: :type: Gtk.TreeStore
server_store = builder.get_object("server_store")
for author_books in books:
    #: :type: Gtk.TreeIter
    node = server_store.append(None, [author_books[0]])
    for book in author_books[1:]:
        server_store.append(node, [book])

builder.connect_signals(Handler())




window = builder.get_object("main_window")
window.show_all()

Gtk.main()