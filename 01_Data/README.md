## Data Structure

Each experiment has a plaintext **.csv** file that stores the time series data for each sensor within the structure. The Time column, in seconds, in each experiment file is offset based on when ignition occurred. In other words, negative values represent background data and positive values represent time post-ignition. The remaining columns are named corresponding to the location (room and elevation) and measurement type.

The **_Event.csv** file in the *Events* sub-directory, contains the relevant actions performed during the experiments (e.g., ignition, burner off, ventilation).

### Bedroom Experiments
Bedroom 1 was selected as the fire room for all bedroom fires. The status of the HVAC was varied between passive (off), on in cooling and on in heating. The bedroom door was also changed between open and closed to see the effect of ventilation on the spread of fire gases. Two experiments, Experiments 12 and 13, included an open front door.


|Exp #  | HVAC Status       | Open Vents 					| HRR [kW]  | Channel List |
|-------|-------------------|-------------------------------|------|-------------------------|
|1 		| Off 				| Bedroom 1 and Basement Doors 	| 110  | Channel_List_Gas_Burner |
|2 		| On Cooling		| Bedroom 1 and Basement Doors 	| 110  | Channel_List_Gas_Burner |
|3		| On Cooling		| Bedroom 1 and Basement Doors 	| 110  | Channel_List_Gas_Burner |
|4		| On Heating		| Bedroom 1 and Basement Doors 	| 110  | Channel_List_Gas_Burner |
|5		| On Cooling		| Bedroom 1 and Basement Doors 	| 110  | Channel_List_Gas_Burner |
|6		| On Heating		| Bedroom 1 and Basement Doors 	| 110  | Channel_List_Gas_Burner |
|7		| Off 				| Bedroom 1 and Basement Doors 	| 110--280  | Channel_List_Gas_Burner |
|8		| Off 				| Basement Door 				| 110  | Channel_List_Gas_Burner |
|9		| On Cooling		| Basement Door 				| 110  | Channel_List_Gas_Burner |
|10 	| Off 				| Basement Door 				| 110  | Channel_List_Gas_Burner |
|11 	| Off 				| Basement Door 				| 110  | Channel_List_Gas_Burner |
|12		| Off 				| Basement and Front Doors 		| 110  | Channel_List_Gas_Burner |
|13 	| On Cooling 		| Basement and Front Doors 		| 110  | Channel_List_Gas_Burner |
|14 	| On Cooling 		| Bedroom 1 and Basement Doors 	| 110  | Channel_List_Gas_Burner |


### Living Room Experiments

Living room experiments were performed to examine how a fire in a larger room on the first floor would spread fire gases throughout the structure. HVAC status was set to either passive or cooling during the living room experiments. With the exception of Experiment 15, all living room experiments were performed with the door to the basement staircase closed. Experiments 20 and 21 included the use of transfer vents installed above the bedroom 1 and bedroom 3 doors. Gas measurements were made in the living room for experiments 15-18 and moved into bedroom 1 for experiments 19-21.

|Exp #  | HVAC Status    | Open Vents 				| HRR [kW] | Channel List |
|-------|----------------|--------------------------|------|-------------------------|
|15 	| Off   		 | Basement Door			| 110  | Channel_List_Gas_Burner_2 |
|16 	| Off 			 | -- 						| 110  | Channel_List_Gas_Burner_2 |
|17 	| On Cooling	 | -- 						| 110  | Channel_List_Gas_Burner_2 |
|18 	| Off 			 | -- 						| 110--280  | Channel_List_Gas_Burner_2 |
|19 	| On Cooling 	 | -- 						| 110--280  | Channel_List_Gas_Burner |
|20 	| Off			 | Bedroom 1 & 3 Transfer	| 110--280  | Channel_List_Gas_Burner |
|21 	| On Cooling	 | Bedroom 1 & 3 Transfer	| 110--280  | Channel_List_Gas_Burner |


### Basement Experiments

Basement fire scenarios were performed to examine how fire in a "below grade" scenario would spread fire gases throughout the structure. Experiments were performed with the HVAC system in passive, cooling and heating. The basement staircase door for these experiments was varied between open and closed to see the effect that it had on fire gas spread to the first floor. Additionally, transfer vents were installed above the bedroom 1 and 3 doors for a subset of the experiments.

|Exp # | HVAC Status | Open Vents 				        | HRR (kW) | Channel List |
|------|-------------|----------------------------------|------|-------------------------|
|22	 | Off 			 | Bedroom 1 and Basement Doors 	| 280  | Channel_List_Gas_Burner |
|	 |				 | Bedroom 1 & 3 Transfer 			| |
|23	 | Off 			 | Basement Door 					| 280  | Channel_List_Gas_Burner |
|	 |				 | Bedroom 1 & 3 Transfer 			| |
|24	 | On Cooling 	 | Basement Door 					| 280  | Channel_List_Gas_Burner |
|	 |				 | Bedroom 1 & 3 Transfer 			| |
|25	 | Off 			 | Bedroom 1 & 3 Transfer 			| 280  | Channel_List_Gas_Burner |
|26	 | On Cooling	 | Bedroom 1 & 3 Transfer 			| 280  | Channel_List_Gas_Burner |
|27	 | On Heating	 | Bedroom 1 & 3 Transfer 			| 280  | Channel_List_Gas_Burner |
|28	 | Off			 | Bedroom 1 & 3 Transfer 			| 360  | Channel_List_Gas_Burner |
|29	 | Off			 | Basement Door 					| 360  | Channel_List_Gas_Burner |
|	 |				 | Bedroom 1 & 3 Transfer 			| |

### Velocity Data

Direction of gas movement for positive and negative gas velocities.

|Location            | Measurement Velocity Sign |
|--------------------|---------------------------|
| Front Door         | (+) velocity is flow out of the front door |
|                    | (-) velocity is flow into the structure |
| Basement Stairwell | (+) velocity is flow up the stairwell |
|                    | (-) velocity is flow down the stairwell |
| Top Stairwell      | (+) velocity is flow up the stairwell |
|                    | (-) velocity is flow down the stairwell |
| Supply Duct        | (+) velocity is flow from system into structure |

### Fan Status

A pressure tap was installed downstream of the HVAC supply fan as a during experiment diagnostic channel. The range of the pressure transducer was &#177; 33 Pa, such that during operation flows from the fan would max out the transducer to easily visualize flow during the experiment. Decreasing pressure during an experiment was an indication that the HVAC filter was potentially becoming clogged, therefore restricting flow. As a result, the magnitude of pressure in this channel should not be considered to be a true representation of the pressure in the supply duct.


