import logging
import datetime
import os
# import utils
from helpers.resources import root_folder, output_folder_name, output_folder


class Logger():
    __logger = False
    def getLogger(self):
        if (Logger.__logger):
           return Logger.__logger
        else:
            logging.basicConfig(level=logging.INFO)

            # set log level
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)

            #create directory if not present
            directory_path = output_folder
            directory= os.path.dirname(directory_path)+'/consolidated_test_logs'
            if  not os.path.exists(directory):
                os.mkdir(directory)
            else:
                list_file = os.listdir(directory)  # dir is your di
                list_file.sort()
                matching = [s for s in list_file if "test_execution_logs" in s]
                number_files=len(matching)
                matching.sort()
                while number_files >= 5:
                    file_to_delete=matching.pop(0)
                    os.remove(directory+'/'+file_to_delete)
                    number_files=number_files-1
            # define file handler and set formatter
            date_time = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            log_file_name = '/test_execution_logs_'+date_time+'.log'
            file_handler = logging.FileHandler(directory+log_file_name)
            formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
            file_handler.setFormatter(formatter)

            # add file handler to logger
            logger.addHandler(file_handler)
            Logger.__logger = logger
            return Logger.__logger

