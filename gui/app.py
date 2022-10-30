"""
"""

import gi
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class DockerQA(object):
    """
    """

    def __init__(self, builder, **kwargs):
        super(DockerQA, self).__init__(**kwargs)

        self.builder = builder
        # ******** Main Components ********
        self.builder.add_from_file('app.glade')
        self.main_window = self.builder.get_object("main_window")

        # ******** Stack and switcher ********
        self.main_stack_switcher = self.builder.get_object("main_stack_switcher")

        # ******** Buttons ********
        self.install_pr_button = self.builder.get_object("install_pr_button")
        self.run_clone_repo_button = self.builder.get_object("run_clone_repo_button")

        # ******** Selects ********
        self.clone_repo_branch_select = self.builder.get_object("clone_repo_branch_select")

        # ******** Entries ********
        self.clone_folder_name_entry = self.builder.get_object("clone_folder_name_entry")

        # ******** Setup app and components on start ********
        self.builder.connect_signals(self)
        self.main_window.show_all()
        self.set_branches_in_clone_repo_select(self)

    # ******** Setup functions ********
    def set_branches_in_clone_repo_select(self, widget):
        self.clone_repo_branch_select.remove_all()
        branches = ["develop", "1.7.8.x", "8.0.x"]
        for branch in branches:
            self.clone_repo_branch_select.append_text(branch)

    # ******** Clone repo stack functions ********
    def get_selected_branch(self, widget):
        return self.clone_repo_branch_select.get_active_text()

    def get_folder_name_to_create(self, widget):
        return self.clone_folder_name_entry.get_text()

    def on_run_clone_repo_button_clicked(self, widget):
        branch = self.get_selected_branch(widget)
        name = self.get_folder_name_to_create(widget)
        if branch == '' or name == '':
            print(f"Branch or folder name is empty !!")
        else:
            command = f'make clone branch={branch} name={name}'
            # command = 'cd html/ && ls -la'
            subprocess.run(['bash', '-c', command], shell=False, cwd='../')

    # ******** App destroy ********
    @staticmethod
    def on_main_destroy(widget):
        Gtk.main_quit()


# ******** Main loop ********
interface = Gtk.Builder()

if __name__ == "__main__":
    DockerQA(interface)
    Gtk.main()
