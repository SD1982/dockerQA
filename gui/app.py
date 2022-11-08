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
        self.main_stack_switcher = self.builder.get_object("main_stack_switcher")

        # ******** Buttons **********************************************************************
        self.install_pr_button = self.builder.get_object("install_pr_button")
        self.run_clone_repo_button = self.builder.get_object("run_clone_repo_button")

        # ******** Selects **********************************************************************
        self.clone_repo_branch_select = self.builder.get_object("clone_repo_branch_select")
        self.install_pr_folder_name_select = self.builder.get_object("install_pr_folder_name_select")
        self.reset_repo_folder_name_select = self.builder.get_object("reset_repo_folder_name_select")
        self.reset_repo_branch_select = self.builder.get_object("reset_repo_branch_select")
        self.delete_repo_folder_select = self.builder.get_object("delete_repo_folder_select")

        # ******** Entries **********************************************************************
        self.clone_folder_name_entry = self.builder.get_object("clone_folder_name_entry")
        self.install_pr_number_entry = self.builder.get_object("install_pr_number_entry")

        # ******** Alerts and infos label **************************************************************
        self.clone_repo_missing_branch_label = self.builder.get_object("clone_repo_missing_branch_label")
        self.clone_repo_missing_folder_label = self.builder.get_object("clone_repo_missing_folder_label")
        self.install_pr_missing_folder_label = self.builder.get_object("install_pr_missing_folder_label")
        self.install_pr_missing_number_label = self.builder.get_object("install_pr_missing_number_label")
        self.delete_repo_missing_folder_label = self.builder.get_object("delete_repo_missing_folder_label")
        self.reset_repo_missing_folder_label = self.builder.get_object("reset_repo_missing_folder_label")
        self.reset_repo_missing_branch_label = self.builder.get_object("reset_repo_missing_branch_label")

        # ******** Setup app and elements on start *********************************************
        self.builder.connect_signals(self)
        self.main_window.show_all()
        self.disable_alerts_and_infos_on_start(self)
        self.set_branches_in_all_selects(self)
        self.set_repositories_in_folders_selects(self)

    # ******** Setup functions *******************************************************************
    def set_branches_in_all_selects(self, widget):
        self.clone_repo_branch_select.remove_all()
        self.reset_repo_branch_select.remove_all()
        branches = ["develop", "1.7.8.x", "8.0.x"]
        for branch in branches:
            self.clone_repo_branch_select.append_text(branch)
            self.reset_repo_branch_select.append_text(branch)

    def disable_alerts_and_infos_on_start(self, widget):
        self.disable_clone_stack_alerts_and_infos(self)
        self.disable_pr_stack_alerts_and_infos(self)
        self.disable_reset_repo_stack_alerts_and_infos(self)
        self.disable_delete_repo_stack_alerts_and_infos(self)

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

    # ******** Clone repo stack functions ********************************************************
    def disable_clone_stack_alerts_and_infos(self, widget):
        self.clone_repo_missing_branch_label.set_visible(False)
        self.clone_repo_missing_folder_label.set_visible(False)

    def get_selected_branch(self, widget):
        return self.clone_repo_branch_select.get_active_text()

    def get_folder_name_to_create(self, widget):
        return self.clone_folder_name_entry.get_text()

    def on_clone_folder_name_changed(self, widget):
        self.clone_repo_missing_folder_label.set_visible(False)

    def on_clone_branch_changed(self, widget):
        self.clone_repo_missing_branch_label.set_visible(False)

    def on_run_clone_repo_button_clicked(self, widget):
        branch = self.get_selected_branch(widget)
        name = self.get_folder_name_to_create(widget)

        if branch == '':
            self.clone_repo_missing_branch_label.set_visible(True)
        elif name == '':
            self.clone_repo_missing_folder_label.set_visible(True)
        else:
            print(f'branch: {branch}')
            print(f'name: {name}')

    # ******** Install PR stack functions *********************************************************
    def disable_pr_stack_alerts_and_infos(self, widget):
        self.install_pr_missing_folder_label.set_visible(False)
        self.install_pr_missing_number_label.set_visible(False)

    def get_pr_number_to_install(self, widget):
        return self.install_pr_number_entry.get_text()

    def get_folder_name_to_install_pr(self, widget):
        return self.install_pr_folder_name_select.get_active_text()

    def on_run_install_pr_button_clicked(self, widget):
        pr_number = self.get_pr_number_to_install(widget)
        folder_to_install = self.get_folder_name_to_install_pr(widget)
        pr_branch = '' # TODO here need a branch select

        if pr_number == '':
            self.install_pr_missing_number_label.set_visible(True)
        elif folder_to_install == '':
            self.install_pr_missing_folder_label.set_visible(True)
        else:
            self.disable_reset_repo_stack_alerts_and_infos(widget)
            # command = f'make install-pr name= branch={} number={}'
            # subprocess.Popen(command, shell=True, cwd='../')
        print(f'number: {pr_number}')

    # ******** Reset repo stack functions *********************************************************
    def get_folder_name_to_reset(self, widget):
        return self.reset_repo_folder_name_select.get_active_text()

    def get_branch_to_reset(self, widget):
        return self.reset_repo_branch_select.get_active_text()

    def disable_reset_repo_stack_alerts_and_infos(self, widget):
        self.reset_repo_missing_folder_label.set_visible(False)
        self.reset_repo_missing_branch_label.set_visible(False)

    def on_run_reset_repo_button_clicked(self, widget):
        # TODO here maybe on this function add a "infos resume" before the repo reset ??
        folder_to_reset = self.get_folder_name_to_reset(widget)
        branch_to_reset = self.get_branch_to_reset(widget)

        if folder_to_reset == '':
            self.reset_repo_missing_folder_label.set_visible(True)
        elif branch_to_reset == '':
            self.reset_repo_missing_branch_label.set_visible(True)
        else:
            self.disable_reset_repo_stack_alerts_and_infos(widget)
            command = f'make reset-repo branch={branch_to_reset} name={folder_to_reset}'
            subprocess.Popen(command, shell=True, cwd='../')

    # ******** Delete repo stack functions *********************************************************
    def get_repo_folder_name_to_delete(self, widget):
        return self.delete_repo_folder_select.get_active_text()

    def disable_delete_repo_stack_alerts_and_infos(self, widget):
        self.delete_repo_missing_folder_label.set_visible(False)

    def on_run_delete_repo_button_clicked(self, widget):
        # TODO here maybe on this function add a "confirmation popup" before the repo deletion ??
        folder_to_delete = self.get_repo_folder_name_to_delete(widget)

        if folder_to_delete == '':
            self.delete_repo_missing_folder_label.set_visible(True)
        else:
            self.disable_delete_repo_stack_alerts_and_infos(widget)
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
