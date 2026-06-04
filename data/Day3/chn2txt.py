import struct
import os
import numpy as np 


'''
How to use this script:
Paste the .Chn file from MAESTRO you want to convert to .txt in the same folder as chn2txt.py.
Run the script and type the name of the file you wish to convert in the command window like shown in the example.
If successfull you have now obtained your channel numbers and counts per channel number in a text file in the same folder.
If you encounter any problems, don't hesitate to contact the TA.

Script is based on:
https://github.com/tegmyr/ortec_read
^Can be used to solve problems encountered when converting to txt file.
'''

print("Please input the name of the file to convert, like the following example")
print('02062026DataMUO.Chn')
filename = input()

filename = os.path.join(os.getcwd(), filename)

def chn2txt(filename):       
        # Opening file and reading information
        try:
            infile             = open(filename, "rb")
            version            = struct.unpack('h', infile.read(2))[0]
            mca_detector_id    = struct.unpack('h', infile.read(2))[0]
            segment_number     = struct.unpack('h', infile.read(2))[0]
            start_time_ss      = infile.read(2)
            real_time          = struct.unpack('I', infile.read(4))[0]
            live_time          = struct.unpack('I', infile.read(4))[0]
            start_date         = infile.read(8) #Ascii type date in #DDMMMYY* where * == 1 means 21th century
            start_time_hhmm    = infile.read(4)
            chan_offset        = struct.unpack('h', infile.read(2))[0]
            no_channels        = struct.unpack('h', infile.read(2))[0]    
            hist_array         = np.zeros(no_channels) #Init hist_array 

            #Read the binary data
            for index in range(len(hist_array)):
                hist_array[index]= struct.unpack('I', infile.read(4))[0]
            assert struct.unpack('h', infile.read(2))[0] == -102
            infile.read(2)
            en_zero_inter = struct.unpack('f', infile.read(4))[0]  
            en_slope = struct.unpack('f', infile.read(4))[0]
            en_quad = struct.unpack('f', infile.read(4))[0]

        except ValueError:
            print('Unable to load file ' + filename)


        # Writing data to txt file
        headers = ['Channel No.', 'Counts']
        with open(f"{filename.rsplit('.',1)[0]}.txt", "w") as f:
            
            # Write headers to first line of file
            f.write('\t'.join(headers) + '\n')

            i=1
            for item in hist_array:
                line = f'{i}\t{item}\n'
                f.write(line)
                i+=1

        infile.close()
        print('chn2txt Successful!')


chn2txt(filename)
input("Press enter to exit;")
