import math 

def calculate_temperature_rise(temp_data):
    """
    Calculate the temperetaure rise, i.e. the difference between the maximum and the minimum 
    
    """
    
    for d in temp_data:
        d['temp_rise'] = d['temperature'].max(axis=0) - d['temperature'][d['temperature']>0.0].min(axis=0)

    return temp_data
def calculate_rms_error(exp_data, sim_data, tc_names='all', split_delim='-'):
    """
    Calculate the RMS error of the simulated temperature values for a range of efficiencies against 
    an experimental dataset.
    
    Parameters
    ----------
    exp_data: list of dicts
    
    sim_data: list of dicts
    
    tc_names : string or list of strings
        A list of the selected thermocouples for the analysis to be performed in the format of 'TC#',
        where # stands for the thermocouple number. Or alternatively 'all' experimental thermocouples 
        will be included.
    split_delim: string
        Delimiter of the thermocouples data names used to separate the 'TC#'' part only, 
        e.g. if 'D-TC1', delimiter is '-' [default].

    """
    
    exp_selected_data = []
    sim_selected_data = []
    if tc_names == 'all':
        # redefine tc_names to an empty list to be updated later
        tc_names = []
        for exp_tc in exp_data[0]['temp_rise'].index.values:
            exp_selected_data.append(exp_data[0]['temp_rise'][exp_tc])
            # update the tc_names list with each tc name in the experimental data as 'TC#''
            tc_names.append(exp_tc.rpartition(split_delim)[2])
    else:
        for tc in tc_names:
            for exp_tc in exp_data[0]['temp_rise'].index.values:
                exp_tc_split = exp_tc.rpartition(split_delim)[2]
                if tc == exp_tc_split:
                    exp_selected_data.append(exp_data[0]['temp_rise'][exp_tc])
#     print(exp_selected_data)
    for sim_idx, sim_d in enumerate(sim_data):
        sim_selected_data.append([])
        for tc in tc_names:
            for sim_tc in sim_d['temp_rise'].index.values:
                sim_tc_split = sim_tc.rpartition(split_delim)[2]
                if tc == sim_tc_split:
                    sim_selected_data[sim_idx].append(sim_d['temp_rise'][sim_tc])

    # create empty list
    RMS_list = []

    #calculation of RMS for all efficiencies
    for  i in range(len(sim_selected_data)):
        dif_sqr_sum = 0
        for tc_i, tc in enumerate(tc_names):
            dif_sqr_sum += ((sim_selected_data[i][tc_i] - exp_selected_data[tc_i]) / exp_selected_data[tc_i]) ** 2
        
        RMS_list.append(
            math.sqrt(dif_sqr_sum / len(tc_names))
        )
        
    return RMS_list