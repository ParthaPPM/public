import pandas as pd
import numpy as np


input_file_name = "12_5_2021_11_15_1_12_5_2021_11_35_30.csv"
output_file_name = input_file_name.split(".")[0] + "_export.csv"
full_data_frame = pd.read_csv(input_file_name)

# input data column names
bus_energy_column_name = "BusEnergyImport"
source_pcu_0_column_name = "PCU1"
source_pcu_1_column_name = "PCU2"
source_gen_0_column_name = "GEN1"
source_gen_1_column_name = "GEN2"
pcu_0_column_name = "PCU1_KWH"
pcu_1_column_name = "PCU2_KWH"
gen_0_column_name = "GEN1_KWH"
gen_1_column_name = "GEN2_KWH"
status_column_name = "Status"
pcu_0_calculated_column_name = "PCU1_KWH_cal"
pcu_1_calculated_column_name = "PCU2_KWH_cal"
gen_0_calculated_column_name = "GEN1_KWH_cal"
gen_1_calculated_column_name = "GEN2_KWH_cal"

# status column values
source_pcu_0 = "PCU1"
source_pcu_1 = "PCU2"
source_gen_0 = "GEN1"
source_gen_1 = "GEN2"
source_many = "!!!!"
source_unknown = "????"

# source status
source_status_on = "ON"
source_status_off = "OFF"
source_status_unknown = ""

# modifying the data frame as our need
full_data_frame = full_data_frame.replace("'","", regex=True)
full_data_frame[bus_energy_column_name] = full_data_frame[bus_energy_column_name].apply(lambda a: float(a) if len(a.strip())!=0 else 0)
full_data_frame[pcu_0_column_name] = full_data_frame[pcu_0_column_name].apply(lambda a: float(a) if len(a.strip())!=0 else 0)
full_data_frame[pcu_1_column_name] = full_data_frame[pcu_1_column_name].apply(lambda a: float(a) if len(a.strip())!=0 else 0)
full_data_frame[gen_0_column_name] = full_data_frame[gen_0_column_name].apply(lambda a: float(a) if len(a.strip())!=0 else 0)
full_data_frame[gen_1_column_name] = full_data_frame[gen_1_column_name].apply(lambda a: float(a) if len(a.strip())!=0 else 0)

# creating the output data frame
column_names = [bus_energy_column_name, source_pcu_0_column_name, source_pcu_1_column_name, source_gen_0_column_name, source_gen_1_column_name, pcu_0_column_name, pcu_1_column_name, gen_0_column_name, gen_1_column_name, status_column_name, pcu_0_calculated_column_name, pcu_1_calculated_column_name, gen_0_calculated_column_name, gen_1_calculated_column_name]
output_data_frame = pd.DataFrame(columns=column_names)

# processing starts
no_of_rows = len(full_data_frame.index)
start_index = 0
stop_index = no_of_rows
previous_status = source_unknown
bus_energy = 0
source_pcu_0_energy = 0
source_pcu_1_energy = 0
source_gen_0_energy = 0
source_gen_1_energy = 0
pcu_0_calculated = 0
pcu_1_calculated = 0
gen_0_calculated = 0
gen_1_calculated = 0
for i in range(start_index, stop_index):
    row = full_data_frame.iloc[i]
    
    # creating the status column
    source = source_unknown
    if row[source_pcu_0_column_name].strip() == source_status_on:
        source = source_pcu_0
    elif row[source_pcu_1_column_name].strip() == source_status_on:
        source = source_pcu_1
    elif row[source_gen_0_column_name].strip() == source_status_on:
        source = source_gen_0
    elif row[source_gen_1_column_name].strip() == source_status_on:
        source = source_gen_1
    
    # creating the calculated columns
    present_status = source
    present_bus_energy = row[bus_energy_column_name]
    present_source_pcu_0_energy = row[pcu_0_column_name]
    present_source_pcu_1_energy = row[pcu_1_column_name]
    present_source_gen_0_energy = row[gen_0_column_name]
    present_source_gen_1_energy = row[gen_1_column_name]
    # if present_status == source_unknown or present_status == source_many:
    #     pcu_0_calculated = 0
    #     pcu_1_calculated = 0
    # else:
    #     if previous_status != present_status:
    #         if present_bus_energy != 0:
    #             bus_energy = present_bus_energy
    #             if present_source_0_energy != 0:
    #                 source_0_energy = present_source_0_energy
    #             if present_source_1_energy != 0:
    #                 source_1_energy = present_source_1_energy
    #             if present_status != source_unknown:
    #                 previous_status = present_status
    #     pcu_0_calculated = present_bus_energy - bus_energy + source_0_energy
    #     pcu_1_calculated = present_bus_energy - bus_energy + source_1_energy
    
    if present_bus_energy != 0:
        bus_energy = present_bus_energy
        if present_status == source_pcu_0 and present_source_pcu_0_energy != 0:
            source_pcu_0_energy = present_source_pcu_0_energy
            pcu_0_calculated = present_bus_energy - bus_energy + source_pcu_0_energy
        if present_status == source_pcu_1 and present_source_pcu_1_energy != 0:
            source_pcu_1_energy = present_source_pcu_1_energy
            pcu_1_calculated = present_bus_energy - bus_energy + source_pcu_1_energy
        if present_status == source_gen_0 and present_source_gen_0_energy != 0:
            source_gen_0_energy = present_source_gen_0_energy
            gen_0_calculated = present_bus_energy - bus_energy + source_gen_0_energy
        if present_status == source_gen_1 and present_source_gen_1_energy != 0:
            source_gen_1_energy = present_source_gen_1_energy
            gen_1_calculated = present_bus_energy - bus_energy + source_gen_1_energy


    # creating the data frame row
    d = {bus_energy_column_name: present_bus_energy,
         source_pcu_0_column_name: row[source_pcu_0_column_name],
         source_pcu_1_column_name: row[source_pcu_1_column_name],
         source_gen_0_column_name: row[source_gen_0_column_name],
         source_gen_1_column_name: row[source_gen_1_column_name],
         pcu_0_column_name: present_source_pcu_0_energy,
         pcu_1_column_name: present_source_pcu_1_energy,
         gen_0_column_name: present_source_gen_0_energy,
         gen_1_column_name: present_source_gen_1_energy,
         status_column_name: source,
         pcu_0_calculated_column_name: pcu_0_calculated,
         pcu_1_calculated_column_name: pcu_1_calculated,
         gen_0_calculated_column_name: gen_0_calculated,
         gen_1_calculated_column_name: gen_1_calculated}
    output_data_frame = output_data_frame.append(d, ignore_index=True)

output_data_frame.to_csv(output_file_name, index=False)
