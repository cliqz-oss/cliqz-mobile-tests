from testSuites.test01BasicView import TestBasicView
from testSuites.test02SettingsMenu import TestSettingsMenu
from testSuites.test03FreshTabFeatures import TestFreshTabFeatures
from testSuites.test04UserTabFeatures import TestUserTabFeatures
from testSuites.test05GhosteryControlCenter import TestGhosteryControlCenter
from testSuites.test06SearchFeatures import TestSearchFeatures

class CompleteSuite(
    TestBasicView,
    TestSettingsMenu,
    TestFreshTabFeatures,
    TestUserTabFeatures,
    TestGhosteryControlCenter,
    TestSearchFeatures
):
    def ignore(self):
        pass
