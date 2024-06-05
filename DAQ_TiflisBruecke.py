from DAQ_Module import DAQ_Module as daq

if __name__ == "__main__":
    device_in = "cDAQ4Mod1"
    channels = [0, 1, 2]    # Channels 1 and 2 are roving sensors while Sensor 3 is used for reference
    sensitivities = [100.93, 100.73, 94.875]  # mv/ms^-2
    duration = 500        # Measurement length allows for the SDs to have an error of 10 %
    sample_rate = 2048      # Hz
    mat_filename = "Data/TiflisBruecke/Data_040624_pos0612.mat"    
    #1#3#
    ##r##
    #2#4#
    acc_data = daq.daq_oma(device_in=device_in,
                           channels=channels,
                           duration=duration,
                           fs=sample_rate,
                           acc_sensitivities=sensitivities)
    daq.save_to_mat(acc_data, mat_filename)
    daq.plot_data(acc_data, sample_rate)