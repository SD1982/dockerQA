"""
"""

import gi
import os


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


#-----Main app class
class DockerQA(object):

    #-----Init & main window creation
    def __init__(self,builder,**kwargs):
        super(DockerQA,self).__init__(**kwargs)

        self.builder=builder
        #-----General Components
        self.builder.add_from_file('app.glade')
        self.mainWindow=self.builder.get_object("mainWindow")
        #-----Docker stack related components
        self.start_containers_button=self.builder.get_object("start_containers_button")
        self.stop_containers_button=self.builder.get_object("stop_containers_button")
        #-----Repositories section related components
        self.develop_branch_checkbox=self.builder.get_object("develop_branch_checkbox")
        self.seventySeven_branch_checkbox=self.builder.get_object("seventySeven_branch_checkbox")
        self.seventyEight_branch_checkbox=self.builder.get_object("seventyEight_branch_checkbox")
        self.clone_radio_button=self.builder.get_object("clone_radio_button")
        self.update_radio_button=self.builder.get_object("update_radio_button")
        self.remove_radio_button=self.builder.get_object("remove_radio_button")
        self.execute_repo_action_button=self.builder.get_object("execute_repo_action_button")
        #-----Pull requests section related components
        self.develop_radio_button=self.builder.get_object("develop_radio_button")
        self.seventySeven_radio_button=self.builder.get_object("seventySeven_radio_button")
        self.seventyEight_radio_button=self.builder.get_object("seventyEight_radio_button")
        self.install_pr_button=self.builder.get_object("install_pr_button")
        #-----Activation
        self.builder.connect_signals(self)
        self.mainWindow.show_all()
        #-----Others vars
        self.availableBranches = [self.develop_branch_checkbox, self.seventySeven_branch_checkbox, self.seventyEight_branch_checkbox]
        self.repoActions = [self.clone_radio_button, self.update_radio_button, self.remove_radio_button]


    #-----Repositories section actions
    def get_selected_branches(self, widget):
        selectedBranches = []

        for branch in self.availableBranches:
            if branch.get_active():
                selectedBranches.append(branch.get_label())

        return selectedBranches


    def get_selected_repo_action(self, widget):
        for action in self.repoActions:
            if action.get_active():
                return action.get_label()


    def execute_repo_action(self, widget, branches, action):
        print (branches, action)


    def check_if_repo_folder_exist(self):
        print ("repo repo")


    def on_execute_repo_action_button_clicked(self, widget):
        selectedBranches = self.get_selected_branches(widget)
        requiredAction = self.get_selected_repo_action(widget)
        self.execute_repo_action(widget, selectedBranches, requiredAction)


    #----Pull requests section actions
    def on_install_pr_button_clicked(self, widget):
        print ("install pull request !!")


    #-----App destroy
    def on_mainWindow_destroy(self, widget):
        Gtk.main_quit()


#-----Main loop
interface = Gtk.Builder()

if __name__ == "__main__":
    DockerQA(interface)
    Gtk.main()