from collections import namedtuple
from typing import Any
import cc.plugin_manager as manager
from cc.plugin_manager import Payload
from datetime import datetime

from actions.copy_files import copy_inputs, copy_outputs
from actions.hot_start_processing_function import process_basin_files

Attrs = namedtuple(
    "Attrs",
    [
        "hms_project_filepath",
        "basin_models",
        "por_run_name",
        "states_start_date",
        "states_end_date",
        "event_duration_hours",
        "lookback_duration_hours",
        "end_padding_hours",
        "base_control_spec_name",
    ],
)


def collectAttributes(payload: Payload) -> Attrs:
    attr = Attrs(
        hms_project_filepath=".",
        basin_models=payload.attributes["basin_models"],
        por_run_name=payload.attributes["por_run_name"],
        states_start_date=datetime.strptime(
            payload.attributes["start_date"], "%Y-%m-%dT%H:%M:%S.%fZ"
        ),
        states_end_date=datetime.strptime(
            payload.attributes["end_date"], "%Y-%m-%dT%H:%M:%S.%fZ"
        ),
        event_duration_hours=payload.attributes["event_duration_hours"],
        lookback_duration_hours=payload.attributes["lookback_duration_hours"],
        end_padding_hours=payload.attributes["end_padding_hours"],
        base_control_spec_name=payload.attributes["base_control_spec_name"],
    )
    return attr


def main():
    # setup
    pm = manager.PluginManager()
    payload = pm.get_payload()

    # parse payload attributes, bail here if that fails
    attrs = collectAttributes(payload)

    # switch action names
    for action in payload.actions:
        match action.name:
            case "copy-inputs":
                copy_inputs(payload, pm)
            case "copy-outputs":
                copy_outputs(payload, pm)
            case "process-basin-files":
                process_basin_files(
                    hms_project_filepath=attrs.hms_project_filepath,
                    basin_models=attrs.basin_models,
                    por_run_name=attrs.por_run_name,
                    states_start_date=attrs.states_start_date,
                    states_end_date=attrs.states_end_date,
                    event_duration_hours=attrs.event_duration_hours,
                    lookback_duration_hours=attrs.lookback_duration_hours,
                    end_padding_hours=attrs.end_padding_hours,
                    base_control_spec_name=attrs.base_control_spec_name,
                )


if __name__ == "__main__":
    main()
