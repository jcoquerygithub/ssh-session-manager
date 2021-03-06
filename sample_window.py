import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

books = [["Tolstoy, Leo", "War and Peace", "Anna Karenina"],
         ["Shakespeare, William", "Hamlet", "Macbeth", "Othello"],
         ["Tolkien, J.R.R.", "The Lord of the Rings"]]


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app, *args, **kwargs):
        Gtk.Window.__init__(self, title="Library", application=app)
        super().__init__(self, title="Library", application=app)
        self.set_default_size(250, 100)
        self.set_border_width(10)

        # the data are stored in the model
        # create a treestore with one column
        store = Gtk.TreeStore(str)
        for i in range(len(books)):
            # the iter piter is returned when appending the author
            piter = store.append(None, [books[i][0]])
            # append the books as children of the author
            j = 1
            while j < len(books[i]):
                store.append(piter, [books[i][j]])
                j += 1

        # the treeview shows the model
        # create a treeview on the model store
        view = Gtk.TreeView()
        view.set_model(store)

        # the cellrenderer for the column - text
        renderer_books = Gtk.CellRendererText()
        # the column is created
        column_books = Gtk.TreeViewColumn(
            "Books by Author", renderer_books, text=0)
        # and it is appended to the treeview
        view.append_column(column_books)

        # the books are sortable by author
        column_books.set_sort_column_id(0)

        select = view.get_selection()
        select.connect("changed", self.on_tree_selection_changed)

        # e
        view.connect("row-activated", self.on_row_activated)

        # add the treeview to the window
        self.add(view)

    def on_row_activated(self, view, path, column):
        model = view.get_model()
        treeiter = model.get_iter(path)
        if treeiter is not None:
            print("You db click on", model[treeiter][0])

    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            print("You selected", model[treeiter][0])

class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)