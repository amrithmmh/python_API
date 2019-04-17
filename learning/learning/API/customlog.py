"""Description: my custom logging class with log to file and log to console"""

import logging

class Custom_log:
    """class that takes custom logger parameters to initialize a logger module
    arguments to be passed :
    1 > logger_name           -- name of the logger module
    2 > logger_level          -- logger logging level
    3 > console_log           -- if True make a console logger else only file logger
    4 > console_stream_level  -- setlevel for console level logging
    5 > console_format        -- format for logging
    6 > file_log              -- set True to create a file logger
    7 > file_path             -- file path/name for logging
    8 > file_format           -- file format for logging
    9 > file_stream_level     -- set level for logging
    """
    def __init__(self,**kwargs):
        self.logger = logging.getLogger(str(kwargs["logger_name"]))
        self.logger.setLevel(kwargs["logger_level"])
        if kwargs["console_log"]==True:
            self.ch = logging.StreamHandler()
            self.ch.setLevel(kwargs["console_stream_level"])
            self.consoleformatter = logging.Formatter(kwargs["console_format"])
            self.ch.setFormatter(self.consoleformatter)
            self.logger.addHandler(self.ch)
        if kwargs["file_log"]==True:
            self.fh = logging.FileHandler(kwargs["file_path"])
            self.fileFormatter = logging.Formatter(kwargs["file_format"])
            self.fh.setFormatter(self.fileFormatter)
            self.fh.setLevel(kwargs["file_stream_level"])
            self.logger.addHandler(self.fh)
    
    def print_all(self,**kwargs):
        """prints all values of class members"""
        print("self.logger = {}".format(self.logger))
        print("self.logger.setLevel = {}".format(kwargs["logger_level"]))
        if kwargs["console_log"]==True:
            print("console setlevel {}".format(kwargs["console_stream_level"]))
            print("console formatter {}".format(kwargs["console_format"]))
        if kwargs["file_log"]==True:
            print("file path {}".format(kwargs["file_path"]))
            print("file_format {}".format(kwargs["file_format"]))
            print("file stream level {}".format(kwargs["file_stream_level"]))

def main():
    """main function for this module"""
    custom_logger=Custom_log(logger_name="custom_name",logger_level=logging.DEBUG,console_log=True,console_stream_level=logging.DEBUG,console_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',file_log=False)
    custom_logger.logger.info("log this")
    custom_logger.logger.debug("this is debbuging message")
    custom_logger.logger.error("oops something bad happened")
    custom_logger.logger.critical("this will break")
    custom_logger2=Custom_log(logger_name="custom_logger2",logger_level=logging.DEBUG,console_log=True,console_stream_level=logging.DEBUG,console_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',file_log=True,file_path="logs.log",file_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',file_stream_level=logging.INFO)
    custom_logger2.logger.info("first log")
    #custom_logger.print_all(logger_name="custom_name",logger_level=logging.DEBUG,console_log=True,console_stream_level=logging.INFO,console_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',file_log=False)

if __name__=="__main__":
    main()



        




        



