'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Owner attribute
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes

class ReqChecking(ReqTagGeneric):

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Checking",
                    set([InputModuleTypes.ctstag, InputModuleTypes.reqtag]))

    def rewrite(self, rid, req):
        if self.get_config().get_bool('global.projecttype.safetyproject', False):
           # This tag (Checking) is optional
           self.check_mandatory_tag(rid, req, 10)

           # Also the check must be in the list of checks
           t = req[self.get_tag()].get_content()
           checks = self.get_config().get_value('requirements.checks')
           if t not in checks:
               raise RMTException(11, "%s: invalid checking '%s'. Must be one "
                                  "of the following cheks '%s'" %
                                  (rid, t, checks))
           # Copy and delete the original
           del req[self.get_tag()]
           return self.get_tag(), t
        else:
           return self.handle_optional_tag(req)
