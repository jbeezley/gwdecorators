from girder_worker import GirderWorkerPluginABC


class GWTaskDemoPlugin(GirderWorkerPluginABC):
    def task_imports(self):
        return ['gwtasks_demo.tasks']
