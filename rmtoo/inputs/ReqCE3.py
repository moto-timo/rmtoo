'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Constraint Evaluation and Execution Environment python code
   
 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes

class ReqCE3(ReqTagGeneric):

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "CE3",
                               set([InputModuleTypes.ctstag, ]))

    def rewrite(self, _, req):
        '''This attribute is optional.'''
        return self.handle_optional_tag(req)

