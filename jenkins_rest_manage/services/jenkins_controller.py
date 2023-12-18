import jenkins
from settings import Settings

class Jenkins:
    def __init__(self):
        super().__init__()
        self.server = jenkins.Jenkins(Settings.jenkins_url, Settings.jenkins_user, Settings.jenkins_password, Settings.jenkins_timeout)

    def get_job_information(self, name, depth=0, fetch_all_builds=False ):
        self.server.get_job_info(name, depth, fetch_all_builds)

    def get_job_info_regex(self, pattern, depth=0, folder_depth=0, folder_depth_per_request=10):
        self.server.get_job_info_regex(pattern, depth, folder_depth, folder_depth_per_request)

    def get_job_name(self, name):
        self.server.get_job_name(name)

    def debug_job_info(self, job_name):
        self.server.debug_job_info(job_name)

    def jenkins_open(self, req, add_crumb=True, resolve_auth=True):
        self.server.jenkins_open(req, add_crumb, resolve_auth)

    def jenkins_request(self, req, add_crumb=True, resolve_auth=True):
        self.server.jenkins_request(req, add_crumb, resolve_auth)

    def get_queue_item(self, number, depth=0):
        self.server.get_queue_item(number, depth)

    def get_build_info(self, name, number, depth=0):
        self.server.get_build_info(name, number, depth)

    def get_build_env_vars(self, name, number, depth=0):
        self.server.get_build_env_vars(name, number, depth)

    def get_build_test_report(self, name, number, depth=0):
        self.server.get_build_test_report(name, number, depth)

    def get_build_artifact(self, name, number, artifact):
        self.server.get_build_artifact(name, number, artifact)

    def get_build_stages(self, name, number):
        self.server.get_build_stages(name, number)

    def get_queue_info(self):
        self.server.get_queue_info()

    def cancel_queue(self, id):
        self.server.cancel_queue(id)

    def get_info(self,item='', query=None):
        self.server.get_info(item, query)

    def get_whoami(self, depth=0):
        self.server.get_whoami(depth)

    def get_version(self):
        self.server.get_version()

    def get_plugins_info(self, depth=2):
        self.server.get_plugins_info(depth)

    def get_plugin_info(self, name, depth=2):
        self.server.get_plugin_info(name, depth)

    def get_plugins(self, depth=2):
        self.server.get_plugins(depth)

    def get_jobs(self, folder_depth=0, folder_depth_per_request=10, view_name=None):
        self.server.get_jobs(folder_depth, folder_depth_per_request, view_name)

    def copy_job(self, from_name, to_name):
        self.server.copy_job(from_name, to_name)

    def rename_job(self, from_name, to_name):
        self.server.rename_job(from_name, to_name)

    def delete_job(self, name):
        self.server.delete_job(name)

    def enable_job(self, name):
        self.server.enable_job(name)

    def disable_job(self, name):
        self.server.disable_job(name)

    def set_next_build_number(self, name, number):
        self.server.set_next_build_number(name, number)

    def job_exists(self, name):
        self.server.job_exists(name)

    def jobs_count(self):
        self.server.jobs_count()

    def create_folder(self ,folder_name, ignore_failures=False):
        self.server.create_folder(folder_name, ignore_failures)

    def upsert_job(self, name, config_xml):
        self.server.upsert_job(name, config_xml)

    def create_job(self, name, config_xml):
        self.server.create_job(name, config_xml)

    def get_job_config(self, name):
        self.server.get_job_config(name)

    def reconfig_job(self, name, config_xml):
        self.server.reconfig_job(name, config_xml)

    def build_job_url(self, name, parameters=None, token=None):
        self.server.build_job_url( name, parameters, token)

    def build_job(self, name, parameters=None, token=None):
        self.server.build_job(name, parameters, token)

    def run_script(self, script, node=None):
        self.server.run_script(script, node)

    def stop_build(self, name, number):
        self.server.stop_build(name, number)

    def delete_build(self, name, number):
        self.server.delete_build(name, number)

    def wipeout_job_workspace(self, name):
        self.server.wipeout_job_workspace(name)

    def get_running_builds(self):
        self.server.get_running_builds()

    def get_nodes(self, depth=0):
        self.server.get_nodes(depth)

    def get_node_info(self, name, depth=0):
        self.server.get_node_info(name, depth)

    def node_exists(self, name):
        self.server.node_exists(name)

    def get_build_console_output(self, name, number):
        self.server.get_build_console_output(name, number)
