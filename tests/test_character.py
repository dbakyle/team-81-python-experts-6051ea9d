from unittest import TestCase
from levelup.character import Character
from levelup.dummy_gamemap import GameMap
from levelup.position import Position

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestCharacterInitNoName(TestCase):
    def test_init(self):
        DEFAULT_NAME = 'Bob'
        testobj = Character()
        self.assertEqual(DEFAULT_NAME, testobj.name)

class TestCharacterGetName(TestCase):
    def test_init(self):
        DEFAULT_NAME = 'Bob'
        testobj = Character()
        self.assertEqual(DEFAULT_NAME, testobj.getName())

class TestCharacterEnterMap(TestCase):
    def test_enter_map(self):
        testobj = Character()
        gamemap = GameMap()
        testobj.enterMap(gamemap)

class TestCharacterMove(TestCase):
    def test_move(self):
        testObj = Character('Bob')
        startPos = testObj.move('NORTH')
        assert startPos.getPosition() == (1,1)
