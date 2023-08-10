import os,sys

''' we will create the custom exception class
    capture error messsage and error detail
'''

class CustomException(Exception):
    def __init__(self, error_message:Exception, error_detail: sys):
        self. error_message = CustomException.get_detailed_error_message(error_message = error_message,
                                                                         error_detail= error_detail)
    
     
    
    ''' 
     defined the function for error message and error details,
     we need only execution try block and extrcat all the error details while executing 
     if error will ocurrrs
     
     exception_block_line_number = exec_tb.tb_frame.f_lineno:- 
     exception try block : execute try block (frame by frame) (line by line) 
     
     try_block_line_number = exec_tb.tb_lineno:- 
     exception try block: exceute try block by line by line whatever error will get it will 
     store to log
     dir
     
     file_name = exec_tb.tb_frame.f_code.co_filename:- 
     from src -- folder code -- file code -- then one by one execute try and except block
     
     define how to store error message
    
    '''
    
    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys)-> str:
        _,_, exec_tb = error_detail.exc_info()
        
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        
        error_message = f"""
        Error ocurred in execution of :
        [{file_name}] at 
        try block line number:[{try_block_line_number}]
        and exception block line number:[{exception_block_line_number}]
        error message:[{error_message}]
        """
        
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()
        
        
        
        
        