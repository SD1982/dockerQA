"""
"""
import os

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

        # ******** Main Components **************************************************************
        self.builder.add_from_file('app.glade')
        self.main_window = self.builder.get_object("main_window")

        # ******** Stack and switcher ***********************************************************
        self.main_stack = self.builder.get_object("main_stack")
        self.main_stack_switcher = self.builder.get_object("main_stack_switcher")

        # ******** Buttons **********************************************************************
        self.install_pr_button = self.builder.get_object("install_pr_button")
        self.run_clone_repo_button = self.builder.get_object("run_clone_repo_button")

        # ******** Selects **********************************************************************
        self.clone_repo_branch_select = self.builder.get_object("clone_repo_branch_select")
        self.install_pr_folder_name_select = self.builder.get_object("install_pr_folder_name_select")
        self.install_pr_branch_select = self.builder.get_object("install_pr_branch_select")
        self.reset_repo_folder_name_select = self.builder.get_object("reset_repo_folder_name_select")
        self.reset_repo_branch_select = self.builder.get_object("reset_repo_branch_select")
        self.delete_repo_folder_select = self.builder.get_object("delete_repo_folder_select")

        # ******** Entries **********************************************************************
        self.clone_folder_name_entry = self.builder.get_object("clone_folder_name_entry")
        self.install_pr_number_entry = self.builder.get_object("install_pr_number_entry")

        # ******** Alerts and infos label **************************************************************
        self.missing_branch_label = self.builder.get_object("missing_branch_label")
        self.missing_folder_label = self.builder.get_object("missing_folder_label")
        self.missing_pr_number_label = self.builder.get_object("missing_pr_number_label")

        # ******** Setup app and elements on start *********************************************
        self.builder.connect_signals(self)
        self.main_window.show_all()
        self.disable_all_labels()
        self.set_branches_in_all_selects()
        self.set_repositories_in_folders_selects(self)

    # ******** Setup and globals functions *******************************************************************
    def set_branches_in_all_selects(self):
        self.clone_repo_branch_select.remove_all()
        self.reset_repo_branch_select.remove_all()
        self.install_pr_branch_select.remove_all()
        branches = ["develop", "1.7.8.x", "8.0.x"]
        for branch in branches:
            self.clone_repo_branch_select.append_text(branch)
            self.reset_repo_branch_select.append_text(branch)
            self.install_pr_branch_select.append_text(branch)

    def disable_all_labels(self):
        self.disable_missing_folder_label(self)
        self.disable_missing_branch_label(self)
        self.disable_missing_pr_number_label(self)

    def disable_missing_branch_label(self, widget):
        self.missing_branch_label.set_visible(False)

    def disable_missing_folder_label(self, widget):
        self.missing_folder_label.set_visible(False)

    def disable_missing_pr_number_label(self, widget):
        self.missing_pr_number_label.set_visible(False)

    def enable_missing_branch_label(self, widget):
        self.missing_branch_label.set_visible(True)

    def enable_missing_folder_label(self, widget):
        self.missing_folder_label.set_visible(True)

    def enable_missing_pr_number_label(self, widget):
        self.missing_pr_number_label.set_visible(True)

    @staticmethod
    def get_existing_repositories(widget):
        rootdir = '../html'
        repositories = []
        for root, folder, file in os.walk(rootdir):
            repositories.extend(folder)
        return repositories

    def set_repositories_in_folders_selects(self, widget):
        self.install_pr_folder_name_select.remove_all()
        self.reset_repo_folder_name_select.remove_all()
        self.delete_repo_folder_select.remove_all()
        repositories = self.get_existing_repositories(widget)
        for repo in repositories:
            self.install_pr_folder_name_select.append_text(repo)
            self.reset_repo_folder_name_select.append_text(repo)
            self.delete_repo_folder_select.append_text(repo)

    def on_folder_name_changed(self, widget):
        self.disable_missing_folder_label(widget)

    def on_branch_changed(self, widget):
        self.disable_missing_branch_label(widget)

    # ******** Clone repo stack functions ********************************************************
    def get_selected_branch(self, widget):
        return self.clone_repo_branch_select.get_active_text()

    def get_folder_name_to_create(self, widget):
        return self.clone_folder_name_entry.get_text()

    def on_run_clone_repo_button_clicked(self, widget):
        branch = self.get_selected_branch(widget)
        folder = self.get_folder_name_to_create(widget)

        if branch == '':
            self.enable_missing_branch_label(widget)
        if folder == '':
            self.enable_missing_folder_label(widget)
        else:
            self.disable_all_labels()
            print(f'branch: {branch}')
            print(f'name: {folder}')

    # ******** Install PR stack functions *********************************************************
    def get_pr_number_to_install(self, widget):
        return self.install_pr_number_entry.get_text()

    def get_folder_name_to_install_pr(self, widget):
        return self.install_pr_folder_name_select.get_active_text()

    def on_run_install_pr_button_clicked(self, widget):
        pr_number = self.get_pr_number_to_install(widget)
        folder_to_install = self.get_folder_name_to_install_pr(widget)
        pr_branch = '' # TODO here need a branch select

        if pr_number == '':
            self.enable_missing_pr_number_label(widget)
        if folder_to_install == '':
            self.enable_missing_folder_label(widget)
        if pr_branch == '':
            self.enable_missing_branch_label(widget)
        else:
            self.disable_all_labels()
            # command = f'make install-pr name= branch={} number={}'
            # subprocess.Popen(command, shell=True, cwd='../')
        print(f'number: {pr_number}')

    # ******** Reset repo stack functions *********************************************************
    def get_folder_name_to_reset(self, widget):
        return self.reset_repo_folder_name_select.get_active_text()

    def get_branch_to_reset(self, widget):
        return self.reset_repo_branch_select.get_active_text()

    def on_run_reset_repo_button_clicked(self, widget):
        # TODO here maybe on this function add a "infos resume" before the repo reset ??
        folder_to_reset = self.get_folder_name_to_reset(widget)
        branch_to_reset = self.get_branch_to_reset(widget)

        if folder_to_reset == '':
            self.enable_missing_folder_label(widget)
        if branch_to_reset == '':
            self.enable_missing_branch_label(widget)
        else:
            self.disable_all_labels()
            command = f'make reset-repo branch={branch_to_reset} name={folder_to_reset}'
            subprocess.Popen(command, shell=True, cwd='../')

    # ******** Delete repo stack functions *********************************************************
    def get_repo_folder_name_to_delete(self, widget):
        return self.delete_repo_folder_select.get_active_text()

    def on_run_delete_repo_button_clicked(self, widget):
        # TODO here maybe on this function add a "confirmation popup" before the repo deletion ??
        folder_to_delete = self.get_repo_folder_name_to_delete(widget)

        if folder_to_delete == '':
            self.enable_missing_folder_label(widget)
        else:
            self.disable_all_labels()
            command = f'make delete-repo name={folder_to_delete}'
            subprocess.Popen(command, shell=True, cwd='../')

    # ******** App destroy ************************************************************************
    @staticmethod
    def on_main_destroy(widget):
        Gtk.main_quit()


# ******** Main loop ******************************************************************************
interface = Gtk.Builder()

if __name__ == "__main__":
    DockerQA(interface)
    Gtk.main()
