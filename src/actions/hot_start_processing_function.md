# Process Basin Files Action

--What does this plugin do?--

# Implementation Details

--Anything that you need to know?--

# Process Flow

--Walk through steps--

# Configuration

Configuration via payload attributes, inputs and outputs.

### Attributes

* `basin_models`: list of basin model names from the HMS project to use as base models (no .basin extension).
* `por_run_name`: name of the HMS simulation run that produced the POR results.
* `start_date` datetime string for start of range of POR dates to use, inclusive. (ISO format - `YYYY-MM-DDTHH:mm:ss.sssZ` or using `datetime.strptime` - `%Y-%m-%dT%H:%M:%S.%fZ`).
* `end_date`: datetime string for end of range of POR dates to use as start states, inclusive.
* `event_duration_hours`: usually 72
* `lookback_duration_hours`: amount of time before the start date to start the control spec, usually 0
* `end_padding_hours`: how much to add after the event duration in hours
* `base_control_spec_name`: name of a control spec to use as the base for the new ones (no .control)

### Inputs

Inputs leverage payload attributes and new templating rules to reference the appropriate files:

```
"inputs": [
  {
    "name": "ScenarioFiles-{ATTR::scenario}",
    "paths": {
      "por-dss": "{ATTR::ffrd_root}/{ATTR::scenario}/{ATTR::hydrology_dir}-por/{ATTR::por_file_name}",
      "basin": "{ATTR::ffrd_root}/{ATTR::scenario}/{ATTR::hydrology_dir}/{ATTR::basin_models[]}.basin"
    },
    "data_paths": null,
    "store_name": "FFRD"
  },
  {
    "name": "ConformanceFiles",
    "paths": {
      "control": "{ATTR::ffrd_root}/conformance/hydrology/trinity/{ATTR::base_control_spec_name}.control"
    },
    "data_paths": null,
    "store_name": "FFRD"
  }
]
```

### Outputs

Outputs also leverage new templating rules to specify output locations in the attached store:

```
"outputs": [
  {
    "name": "BasinModels",
    "paths": {
      "basinmodels": "{ATTR::ffrd_root}/conformance/hydrology/trinity/data/basinmodels"
    },
    "data_paths": null,
    "store_name": "FFRD"
  },
  {
    "name": "ControlSpecs",
    "paths": {
      "controlspecs": "{ATTR::ffrd_root}/conformance/hydrology/trinity/data/controlspecs"
    },
    "data_paths": null,
    "store_name": "FFRD"
  }
]
```