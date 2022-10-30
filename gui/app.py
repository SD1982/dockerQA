"""
"""

import gi
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# Main app class
class DockerQA(object):
    """
    """

    # Init & main window creation
    def __init__(self, builder, **kwargs):
        super(DockerQA, self).__init__(**kwargs)

        self.builder = builder
        # ******** General Components ********
        self.builder.add_from_file('app.glade')
        self.main_window = self.builder.get_object("main_window")
        # ******** Stack and switcher ********
        self.main_stack_switcher = self.builder.get_object("main_stack_switcher")
        # ******** Buttons ********
        self.install_pr_button = self.builder.get_object("install_pr_button")
        self.clone_repo_button = self.builder.get_object("clone_repo_button")
        # ******** Selects ********
        self.clone_repo_branch_select = self.builder.get_object("clone_repo_branch_select")
        # Activation
        self.builder.connect_signals(self)
        self.main_window.show_all()

    def set_branches_in_clone_repo_select(self, widget):
        self.clone_repo_branch_select.remove_all()
        branches = ["develop", "1.7.8.x", "8.0.x"]
        for branch in branches:
            self.clone_repo_branch_select.append_text(branch)

    def get_selected_branch(self, widget):
        self.set_branches_in_clone_repo_select(widget)
        print(self.clone_repo_branch_select.get_active_text())

    @staticmethod
    def on_install_pr_button_clicked(widget):
        command = 'make load-pr number=45678'
        print(command)
        subprocess.run(['bash', '-c', command], shell=False, cwd='../')

    def on_clone_repo_button_clicked(self, widget):
        # command = 'make load-pr number=45678'
        self.get_selected_branch(widget)
        print("Clone repo button clicked")
        # subprocess.run(['bash', '-c', command], shell=True, cwd='../')

    # App destroy
    @staticmethod
    def on_main_destroy(widget):
        Gtk.main_quit()


# Main loop
interface = Gtk.Builder()

if __name__ == "__main__":
    DockerQA(interface)
    Gtk.main()
