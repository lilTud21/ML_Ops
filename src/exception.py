import sys

def error_message_detail(error,error_deatil:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineo,str(error)
     return error_message
    )
    
class CustomException(Exception):
    def _innit_(self,error_message,error_detail:sys):
        super._innit_(error_message)
        self.error_message=error_message_detail(error_message,error_deatil=error_detail)

    def _str_(self):
        return self.error_message