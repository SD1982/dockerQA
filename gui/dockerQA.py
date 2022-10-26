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
        self.develop_branch_radio=self.builder.get_object("develop_branch_radio")
        self.seventy_seven_branch_radio=self.builder.get_object("seventy_seven_branch_radio")
        self.seventy_eight_branch_radio=self.builder.get_object("seventy_eight_branch_radio")
        self.clone_radio_button=self.builder.get_object("clone_radio_button")
        self.update_radio_button=self.builder.get_object("update_radio_button")
        self.remove_radio_button=self.builder.get_object("remove_radio_button")
        self.execute_repo_action_button=self.builder.get_object("execute_repo_action_button")
        #-----Pull requests section related components
        self.develop_pr_radio=self.builder.get_object("develop_pr_radio")
        self.seventy_seven_pr_radio=self.builder.get_object("seventy_seven_pr_radio")
        self.seventy_eight_pr_radio=self.builder.get_object("seventy_eight_pr_radio")
        self.install_pr_button=self.builder.get_object("install_pr_button")
        #-----Activation
        self.builder.connect_signals(self)
        self.mainWindow.show_all()
        #-----Others vars
        self.available_branches = [self.develop_branch_radio, self.seventy_seven_branch_radio, self.seventy_eight_branch_radio]
        self.repo_actions = [self.clone_radio_button, self.update_radio_button, self.remove_radio_button]


    #-----Repositories section actions
    def get_selected_branch(self, widget):
        for branch in self.available_branches:
            if branch.get_active():
                return branch.get_label().lower()


    def get_selected_repo_action(self, widget):
        for action in self.repo_actions:
            if action.get_active():
                return action.get_label().lower()


    def execute_repo_action(self, widget, branch, action):
        print ({'branch': branch, 'action': action})


    def check_if_repo_folder_exist(self):
        print ("repo repo")


    def on_execute_repo_action_button_clicked(self, widget):
        branch = self.get_selected_branch(widget)
        required_action = self.get_selected_repo_action(widget)
        self.execute_repo_action(widget, branch, required_action)


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