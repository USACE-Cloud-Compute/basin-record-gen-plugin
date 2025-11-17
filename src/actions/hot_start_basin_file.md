# Hot Start Basin File Action

Copies an existing basin file but overwrites certain initial condition parameters with states from another simulation run within the same HMS project. 

Assumes certain processes are being used:

* Deficit-constant loss
* Simple canopy (or none)
* Simple surface (or none)
* Linear reservoir baseflow (2 layers)
* Muskingum-Cunge reach. 

Assumes reservoirs initialized with a starting elevation.

Canopy and surface initial condition should be depth, not percent

Linear reservoir initial baseflow should be discharge, not discharge per area

Muskingum-Cunge reach initial condition should be specified discharge, not inflow = outflow

It also unlinks any observed data from the model and changes the name of the sqlite file to match the new basin model name

__Not yet implemented as a top-level action but used by the `process-basin-files` action__