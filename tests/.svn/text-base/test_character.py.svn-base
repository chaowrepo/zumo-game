import sys ,os
from board import Board
from unittest import TestCase


class test_character(TestCase):
    def setUp(self):
        self.position = [0] * 12
    
    def test_swapPlayer1(self):
    
        #Arrange
        board = Board(self.position, '', '')
        board.set_player(1)
        #Act
        board.swapPlayer()
        #Assert
        self.assertEqual(board.get_player(),2)
        
    def test_swapPlayer2(self):
    
        #Arrange
        board = Board(self.position, '', '')
        board.set_player(2)
        #Act
        board.swapPlayer()
        #Assert
        self.assertEqual(board.get_player(),1)    


    def test_select_character1_Bin(self):
        #Arrange
        board = Board(self.position, '', '')
        board.set_player(1)
        text = 'Bin'
        #Act
        board.select_character(text)
        #Assert
        name_p1 = board.get_p1_name()
        self.assertEqual(name_p1 ,'Bin')
    
    def test_select_character1_Med(self):
        #Arrange
        board = Board(self.position, '', '')
        board.set_player(1)
        text = 'Med'
        #Act
        board.select_character(text)
        #Assert
        name_p1 = board.get_p1_name()
        self.assertEqual(name_p1 ,'Med')    
        
    def test_select_character1_Tor(self):
        #Arrange
        board = Board(self.position, '', '')
        board.set_player(1)
        text = 'Tor'
        #Act
        board.select_character(text)
        #Assert
        name_p1 = board.get_p1_name()
        self.assertEqual(name_p1 ,'Tor')    

    def test_select_character2_Bin(self):
        #Arrange
        board = Board(self.position, '', '')
        board.set_player(2)
        text = 'Bin'
        #Act
        board.select_character(text)
        #Assert
        name_p2 = board.get_p2_name()
        self.assertEqual(name_p2 ,'Bin')
    
    def test_select_character2_Med(self):
        #Arrange
        board = Board(self.position, '', '')
        board.set_player(2)
        text = 'Med'
        #Act
        board.select_character(text)
        #Assert
        name_p2 = board.get_p2_name()
        self.assertEqual(name_p2 ,'Med')     
        
    def test_select_character2_Tor(self):
        #Arrange
        board = Board(self.position, '', '')
        board.set_player(2)
        text = 'Tor'
        #Act
        board.select_character(text)
        #Assert
        name_p2 = board.get_p2_name()
        self.assertEqual(name_p2 ,'Tor')  
        
    def test_show_is_selected_P1(self):
        pass
        
    
    def test_show_is_selected_P2(self):
        pass
    
    def test_get_BG_character_path(self):
        #Act
        path = Board.get_BG_character_path()
        #Arrange
        self.assertTrue(os.path.exists(path))    
    
    def test_get_frame_P1_path(self):
        #Act
        path = Board.get_frame_P1_path()
        #Arrange
        self.assertTrue(os.path.exists(path))     
        
    def test_get_frame_P2_path(self):
        #Act
        path = Board.get_frame_P2_path()
        #Arrange
        self.assertTrue(os.path.exists(path))     
    
    def test_get_label_skill_path(self):
        #Act
        path = Board.get_label_skill_path()
        #Arrange
        self.assertTrue(os.path.exists(path))        