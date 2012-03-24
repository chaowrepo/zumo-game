import sys, random
from board import Board
from unittest import TestCase
from start_project import *

app = QApplication([])

class test_board(TestCase):
        
    def test_roll_dice(self):
        # Act
        tmp = Board.random_position()
        # Assert
        self.assertTrue(tmp <= 3)
        self.assertTrue(tmp >= 1)
    
    def test_move_forward_player1(self):
        position = [0] * 12
        now_position = 0
        tmp = now_position
        point = 3
        player = 1
        board = Board(position, '', '')
        # Act
        now_position = board.move_forward(point, now_position, player)
        # Assert
        for i in range(1,point):
            self.assertEquals(1,position[tmp+i])
        self.assertEquals(3,now_position)
        
    def test_move_forward_player2(self):
        # Arrange
        position = [0] * 12
        now_position = 11
        tmp = now_position
        point = 3
        player = 2
        board = Board(position, '', '')
        # Act
        now_position = board.move_forward(point, now_position, player)
        # Assert
        for i in range(1,point):
            self.assertEquals(2,position[tmp-i])
        self.assertEquals(8,now_position)
        
    def test_check_current_position_player1(self):
        # Arrange
        position = [0] * 12
        now_position = 0
        point = 3
        player = 1
        board = Board(position, '', '')
        # Act
        now_position = board.move_forward(point, now_position, player)
        # Assert
        current = board.check_current_position(player)
        self.assertEquals(3,current)
        # Act
        now_position = board.move_forward(point, now_position, player)
        # Assert
        current = board.check_current_position(player)
        self.assertEquals(6,current)
        
    def test_check_current_position_player2(self):
        # Arrange
        position = [0] * 12
        now_position = 11
        tmp = now_position
        point = 2
        player = 2
        board = Board(position, '', '')
        # Act
        now_position = board.move_forward(point, now_position, player)
        # Assert
        current = board.check_current_position(player)
        self.assertEquals(9,current)
        # Act
        now_position = board.move_forward(point, now_position, player)
        # Assert
        current = board.check_current_position(player)
        self.assertEquals(7,current)
        
    def test_check_win_no_win(self):
        # Arrange
        position = [0]*12
        board = Board(position, '', '')
        # Act
        win = board.check_win(board.position)
        # Assert
        self.assertEquals(False,win)
        
    def test_check_win_p1_win(self):
        # Arrange
        position = [0]*12
        board = Board(position, '', '')
        for i in range (0,len(board.position)):
        	board.position[i] = 1
        # Act
        win = board.check_win(board.position)
        # Assert
        self.assertEquals(1,win)
    
    def test_check_win_p2_win(self):
        # Arrange
       	position = [0]*12
        board = Board(position, '', '')
        for i in range (0,len(board.position)):
        	board.position[i] = 2
        # Act
        win = board.check_win(board.position)
        # Assert
        self.assertEquals(2,win)
    
    def test_show_win_no_win(self):
    	# Arrange
    	position = [0]*12
        board = Board(position, '', '')
        # Act
        show_win = board.show_win(False)
        # Assert
        self.assertEquals(True,show_win)
    
    def test_show_win_p1_win(self):
    	# Arrange
    	position = [0]*12
        board = Board(position, '', '')
        # Act
        show_win = board.show_win(1)
        # Assert
        self.assertEquals(1,show_win)
    
    def test_show_win_p2_win(self):
    	# Arrange
    	position = [0]*12
        board = Board(position, '', '')
        # Act
        show_win = board.show_win(2)
        # Assert
        self.assertEquals(2,show_win)
    
    def test_random_stone_skill(self):
        # Arrange
        # Act
        value = Board.random_stone_skill()
        # Assert
        self.assertTrue(value >= 1 and value <=2) 
     
    def test_check_crash_1(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2
        board = Board(position, '', '')
        # Act
        value = board.check_crash()
        # Assert
        self.assertEqual(True, value) 
        
    def test_check_crash_2(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 0
        board = Board(position, '', '')
        # Act
        value = board.check_crash()
        # Assert
        self.assertEqual(False, value)

    def test_get_real_dice_no_crash_1(self):
        # Arrange
        position = [0] * 12
        player = 1
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice+1, value)
        
    def test_get_real_dice_no_crash_same1(self):
        # Arrange
        position = [0] * 12
        player = 1
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice+1, value)
        
    def test_get_real_dice_no_crash_same2(self):
        # Arrange
        position = [0] * 12
        player = 1
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)
       
    def test_get_real_dice_no_crash_same3(self):
        # Arrange
        position = [0] * 12
        player = 1
        dice = 2
        p1_name = 'Med'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value) 
        
    def test_get_real_dice_no_crash_2(self):
        # Arrange
        position = [0] * 12
        player = 1
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice+1, value)
        
    def test_get_real_dice_no_crash_3(self):
        # Arrange
        position = [0] * 12
        player = 1
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)
       
    def test_get_real_dice_no_crash_4(self):
        # Arrange
        position = [0] * 12
        player = 1
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)
        
    def test_get_real_dice_no_crash_5(self):
        # Arrange
        position = [0] * 12
        player = 1
        dice = 2
        p1_name = 'Med'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)
       
    def test_get_real_dice_no_crash_6(self):
        # Arrange
        position = [0] * 12
        player = 1
        dice = 2
        p1_name = 'Med'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)

    def test_get_real_dice_no_crash_7(self):
        # Arrange
        position = [0] * 12
        player = 2
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)
       
    def test_get_real_dice_no_crash_8(self):
        # Arrange
        position = [0] * 12
        player = 2
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value) 
        
    def test_get_real_dice_no_crash_9(self):
        # Arrange
        position = [0] * 12
        player = 2
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice + 1, value)
       
    def test_get_real_dice_no_crash_10(self):
        # Arrange
        position = [0] * 12
        player = 2
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)
        
    def test_get_real_dice_no_crash_11(self):
        # Arrange
        position = [0] * 12
        player = 2
        dice = 2
        p1_name = 'Med'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice + 1, value)
       
    def test_get_real_dice_no_crash_12(self):
        # Arrange
        position = [0] * 12
        player = 2
        dice = 2
        p1_name = 'Med'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)

    def test_get_real_dice_crash_1(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 1
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == dice or value == dice-1)
        
    def test_get_real_dice_crash_same1(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 1
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == dice+1)
        
    def test_get_real_dice_crash_same2(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 1
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == dice-1)
        
    def test_get_real_dice_crash_same3(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 1
        dice = 2
        p1_name = 'Med'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == 0 or value == dice)
       
    def test_get_real_dice_crash_2(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2         
        player = 1
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == 0 or value == dice+1)
        
    def test_get_real_dice_crash_3(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2 
        player = 1
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)
       
    def test_get_real_dice_crash_4(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2         
        player = 1
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == 0 or value == dice) 
        
    def test_get_real_dice_crash_5(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2         
        player = 1
        dice = 2
        p1_name = 'Med'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)
       
    def test_get_real_dice_crash_6(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2         
        player = 1
        dice = 2
        p1_name = 'Med'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == dice-1)

    def test_get_real_dice_crash_7(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 2
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value)
       
    def test_get_real_dice_crash_8(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 2
        dice = 2
        p1_name = 'Bin'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertEqual(dice, value) 
        
    def test_get_real_dice_crash_9(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 2
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == dice-1)
       
    def test_get_real_dice_crash_10(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 2
        dice = 2
        p1_name = 'Tor'
        p2_name = 'Med'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == dice or value == dice-1)
        
    def test_get_real_dice_crash_11(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 2
        dice = 2
        p1_name = 'Med'
        p2_name = 'Bin'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == 0 or value == dice+1)
       
    def test_get_real_dice_crash_12(self):
        # Arrange
        position = [0] * 12
        position[5] = 1
        position[6] = 2        
        player = 2
        dice = 2
        p1_name = 'Med'
        p2_name = 'Tor'
        board = Board(position, p1_name, p2_name)
        # Act
        value = board.get_real_dice(player, dice)
        # Assert
        self.assertTrue(value == 0 or value == dice)
