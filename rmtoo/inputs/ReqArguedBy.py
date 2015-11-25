'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Tag Reviewed by handling
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.InputModuleTypes import InputModuleTypes

class ReqArguedBy(ReqTagGeneric):
    '''Argued by tag implementation.'''

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Argued by",
                      set([InputModuleTypes.ctstag, InputModuleTypes.reqtag, ]))

    def rewrite(self, rid, req):
        if self.get_config().get_bool('global.projecttype.safetyproject', False):
            '''This tag (Argued by) is mandatory for safety projects.'''
            self.check_mandatory_tag(rid, req, 5)
            rtag = req[self.get_tag()].get_content()

            del req[self.get_tag()]
            return self.get_tag(), rtag
        else:
            return self.handle_optional_tag(req)

