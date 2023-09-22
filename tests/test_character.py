from unittest import TestCase
from levelup.character import Character
from levelup.dummy_gamemap import Gamemap
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
        gamemap = Gamemap()
        testobj.enterMap(gamemap)

class TestCharacterMove(TestCase):
    def test_move(self):
        arbitrary_name = 'Bob'
        arbitrary_direction = 'N'
        testObj = Character(arbitrary_name)
        startPos = testObj.move(arbitrary_direction)
        assert startPos.getPosition() == (0,0)

class TestCharacterMoveInvalid(TestCase):
    def test_move(self):
        arbitrary_name = 'Bob'
        arbitrary_direction = 'N'
        testObj = Character(arbitrary_name)
        startPos = Position(-1,0)
        testObj.setCurrentPosition(startPos)
        startPos = testObj.move(arbitrary_direction)
        assert startPos.getPosition() == (-1,0)