from cc.plugin_manager import PluginManager, Payload, DataSourceOpInput
from pathlib import Path


def _getFileName(path: str) -> str:
    return Path(path).name


def copy_inputs(payload: Payload, pm: PluginManager):
    for input in payload.inputs:
        for path_key in input.paths:
            pm.copy_file_to_local(
                DataSourceOpInput(input.name, path_key, None),
                _getFileName(input.paths[path_key]),
            )


def copy_outputs(payload: Payload, pm: PluginManager):
    for output in payload.outputs:
        for path_key in output.paths:
            pm.copy_folder_to_remote(
                DataSourceOpInput(output.name, path_key, None),
                f"data/{path_key}",
            )
