'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Topic tests
     
 (c) 2010,2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.TopicSet import TopicSet
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.tests.lib.TestVCS import TestVCS
from rmtoo.tests.lib.TestInputModules import TestInputModules
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.vcs.ObjectCache import ObjectCache

class TestParse:

    def test_positive_01(self):
        "TopicSet - constructor with only one element"
        try:
            tioconfig = TxtIOConfig()
            cfg = Cfg()
            cfg.set_value('ahah.directory',
                          'tests/unit-test/topic-tests/testdata/topicset01')
            cfg.set_value('ahah.name', 't01')
            cfg.set_value('topics.bkdkd.output', {})

            cfg.set_value('topic_root_node', 'RootNode')
            tvcs = TestVCS(cfg)
            tobjcache = ObjectCache()
            tinmod = TestInputModules()
            topicset = TopicSet(cfg, tvcs, "bkdkd", tobjcache, tinmod)
            assert(False)
        except AssertionError, ae:
            pass

    def test_positive_02(self):
        "TopicSet - valid"
        tioconfig = TxtIOConfig()
        cfg = Cfg()
        cfg.set_value('hahaha.directory',
                      'tests/unit-test/topic-tests/testdata/topicset01')
        cfg.set_value('hahaha.name', 't01')
        cfg.set_value('topics.test-name01.output', {})
        tioconfig = TxtIOConfig()
        cfg.set_value('topic_root_node', 'RootNode')
        tvcs = TestVCS(cfg)
        tobjcache = ObjectCache()
        tinmod = TestInputModules()
        topicset = TopicSet(
            cfg, tvcs, "test-name01", tobjcache, tinmod)

    def test_positive_03(self):
        "TopicSet - valid with empty requirement set"

        tioconfig = TxtIOConfig()
        cfg = Cfg()
        cfg.set_value('huhuhu.directory',
                      'tests/unit-test/topic-tests/testdata/topicset01')
        cfg.set_value('huhuhu.name', 't01')
        cfg.set_value('topics.test-name02.output', {})
        cfg.set_value('topic_root_node', 'RootNode')
        tvcs = TestVCS(cfg)
        tobjcache = ObjectCache()
        tinmod = TestInputModules()
        topicset = TopicSet(cfg, tvcs, "test-name02", tobjcache, tinmod)
