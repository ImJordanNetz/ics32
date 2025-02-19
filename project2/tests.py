#  import unittest
# import random
# import threading
# from time import sleep

# from gradescope_utils.autograder_utils.decorators import weight, visibility, hide_errors

# try:
#     # from solution import *
#     import connect4
#     import connect4_ui
#     import connect4_ui_ai
#     import connect4_network_server_test
#     import connect4_network_client
#     import client_short

#     import connect4_ui_soln
#     import connect4_ui_ai_soln
#     import connect4_network_server_test
#     import connect4_network_client_soln


# except Exception as e:
#     raise Exception(f'Couldnt import a file for the 2-player console connect4, remember to work off of the template. The error is {e}')


# DROP = 1
# POP = 2

# random.seed(190)

# class TestBasics(unittest.TestCase):
#     def setUp(self):
#         pass
    
#     # Test console 
#     # @hide_errors("A q test case has failed!")

#     @weight(5)
#     def test_case00(self):
#         '''testing submission of console files'''
#         try:
#             import connect4_console
#             import connect4_console_ai
#         except:
#             self.assertTrue(False)


#     @weight(5)
#     def test_case01(self):
#         '''printing of empty board'''
#         columns = 8
#         rows = 8
#         c4_state = connect4.new_game(columns, rows)
#         # out = connect4_ui.print_board(c4_state)
#         out = connect4_ui.print_board(c4_state)
#         ans = connect4_ui_soln.print_board(c4_state)
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())
    
#     # @hide_errors("A hidden test case has failed!")
#     @weight(5)
#     def test_case02(self):
#         '''printing of empty board'''
#         columns = 20
#         rows = 10
#         c4_state = connect4.new_game(columns, rows)
#         # out = connect4_ui.print_board(c4_state)
#         out = connect4_ui.print_board(c4_state)
#         # out = " " 
#         ans = connect4_ui_soln.print_board(c4_state)
#         # print("printing of empty board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())

#     @weight(5)
#     def test_case03(self):
#         '''Testing 4x4 game with 4 drops to different columns'''
#         columns = 4
#         rows = 4
#         c4_out = connect4.new_game(columns, rows)
#         c4_ans = connect4.new_game(columns, rows)
        
#         for i in range(1,columns+1):
#             c4_out = connect4_ui.make_move(c4_out, (DROP, i))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, i))

#         out = connect4_ui.print_board(c4_out)
#         ans = connect4_ui_soln.print_board(c4_out)
#         print("printing of board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())

#     @weight(5)
#     def test_case04(self):
#         '''Testing 4x4 game with 4 drops and 4 pops to different columns '''
#         columns = 4
#         rows = 4
#         c4_out = connect4.new_game(columns, rows)
#         c4_ans = connect4.new_game(columns, rows)
        
#         for i in range(1,columns+1):
#             c4_out = connect4_ui.make_move(c4_out, (DROP, i))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, i))

#         for i in range(1,columns+1):
#             c4_out = connect4_ui.make_move(c4_out, (POP, i))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (POP, i))

#         out = connect4_ui.print_board(c4_out)
#         ans = connect4_ui_soln.print_board(c4_out)
#         print("printing of board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())

#     @weight(5)
#     def test_case05(self):
#         '''Testing 4x4 game with multiple drops to each column'''
#         columns = 4
#         rows = 4
#         c4_out = connect4.new_game(columns, rows)
#         c4_ans = connect4.new_game(columns, rows)
        
#         for i in range(1,columns):
#             c4_out = connect4_ui.make_move(c4_out, (DROP, i))
#             c4_out = connect4_ui.make_move(c4_out, (DROP, i))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, i))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, i))

#         out = connect4_ui.print_board(c4_out)
#         ans = connect4_ui_soln.print_board(c4_out)
#         print("printing of board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())

#     @weight(5)
#     def test_case06(self):
#         '''Testing 4x4 game with multiple drops to each column and a pop'''
#         columns = 4
#         rows = 4
#         c4_out = connect4.new_game(columns, rows)
#         c4_ans = connect4.new_game(columns, rows)
        
#         for i in range(1,columns):
#             c4_out = connect4_ui.make_move(c4_out, (DROP, i))
#             c4_out = connect4_ui.make_move(c4_out, (DROP, i))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, i))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, i))

#         c4_out = connect4_ui.make_move(c4_out, (POP, i))
#         c4_ans = connect4_ui_soln.make_move(c4_ans, (POP, i))

#         out = connect4_ui.print_board(c4_out)
#         ans = connect4_ui_soln.print_board(c4_out)
#         print("printing of board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())

#     @weight(5)
#     def test_case07(self):
#         '''Testing 4x4 game with multiple drops and pops to columns 1 and 2'''
#         columns = 4
#         rows = 4
#         c4_out = connect4.new_game(columns, rows)
#         c4_ans = connect4.new_game(columns, rows)
        
#         for i in range(1,columns):
#             c4_out = connect4_ui.make_move(c4_out, (DROP, 1))
#             c4_out = connect4_ui.make_move(c4_out, (DROP, 2))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, 1))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, 2))

#         c4_out = connect4_ui.make_move(c4_out, (POP, 1))
#         c4_ans = connect4_ui_soln.make_move(c4_ans, (POP, 1))
#         c4_out = connect4_ui.make_move(c4_out, (POP, 2))
#         c4_ans = connect4_ui_soln.make_move(c4_ans, (POP, 2))

#         out = connect4_ui_soln.print_board(c4_out)
#         ans = connect4_ui_soln.print_board(c4_out)
#         print("printing of board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())

#     @weight(5)
#     def test_case08(self):
#         '''Testing 4x4 game with multiple drops to columns 1 and 2'''
#         columns = 4
#         rows = 4
#         c4_out = connect4.new_game(columns, rows)
#         c4_ans = connect4.new_game(columns, rows)
        
#         for i in range(1,columns):
#             c4_out = connect4_ui.make_move(c4_out, (DROP, 1))
#             c4_out = connect4_ui.make_move(c4_out, (DROP, 2))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, 1))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, 2))

#         c4_out = connect4_ui.make_move(c4_out, (DROP, 1))
#         c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, 1))
#         out = connect4_ui.print_board(c4_out)
#         ans = connect4_ui_soln.print_board(c4_out)
#         print("printing of board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())     

#     @weight(5)
#     def test_case09(self):
#         '''Testing 20x20 game with multiple drops'''
#         columns = 20
#         rows = 20
#         c4_out = connect4.new_game(columns, rows)
#         c4_ans = connect4.new_game(columns, rows)
        
#         for i in range(5,8):
#             c4_out = connect4_ui.make_move(c4_out, (DROP, i))
#             c4_out = connect4_ui.make_move(c4_out, (DROP, i))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, i))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, i))

#         c4_out = connect4_ui.make_move(c4_out, (DROP, 20))
#         c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, 20))
#         c4_out = connect4_ui.make_move(c4_out, (DROP, 8))
#         c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, 8))
#         c4_out = connect4_ui.make_move(c4_out, (DROP, 20))
#         c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, 20))
#         c4_out = connect4_ui.make_move(c4_out, (DROP, 8))
#         c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, 8))
#         out = connect4_ui.print_board(c4_out)
#         ans = connect4_ui_soln.print_board(c4_out)
#         print("printing of board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())     

#     @weight(5)
#     def test_case10(self):
#         '''Testing 20x20 game with multiple drops and pops'''
#         columns = 20
#         rows = 20
#         c4_out = connect4.new_game(columns, rows)
#         c4_ans = connect4.new_game(columns, rows)
        
#         for i in range(7):
#             num = random.randint(1,columns)
#             c4_out = connect4_ui.make_move(c4_out, (DROP, num))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (DROP, num))

#         for i in range(7):
#             num = random.randint(1,columns)
#             c4_out = connect4_ui.make_move(c4_out, (POP, num))
#             c4_ans = connect4_ui_soln.make_move(c4_ans, (POP, num))

#         out = connect4_ui.print_board(c4_out)
#         ans = connect4_ui_soln.print_board(c4_out)
#         print("printing of board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())  

#     # Test Console AI

#     @weight(10)
#     def test_case11(self):
#         '''Testing Console AI with 20x20 game by having AI play against AI'''
#         columns = 20
#         rows = 20
#         state = connect4.new_game(columns, rows)
#         state_ans = connect4.new_game(columns, rows)
#         m_list = []
#         player = True
#         move = None

#         while connect4.winner(state_ans) == connect4.EMPTY:
#             # out = connect4_ui_soln.print_board(state_ans)
#             # ans = connect4_ui_soln.print_board(state_ans)
#             if player:
#                 state_og = state_ans
#                 # state = connect4_ui_ai_soln.make_move(state, connect4_ui_ai_soln.choose_move(state))
#                 while state_og == state_ans:
#                     move = connect4_ui_ai.ai_move(state_ans)
#                     state_ans = connect4_ui_soln.make_move(state_ans, move )
#                 m_list.append(move)
#             else:
#                 state_og = state_ans
#                 while state_og == state_ans:
#                     move =  connect4_ui_ai.ai_move(state_ans)
#                     state_ans = connect4_ui_soln.make_move(state_ans, move)
#                 m_list.append(move)
#             player = not player

#         ans = (connect4_ui_soln.print_board(state_ans))
#         # print("out:\n" + out)

#         # print(f"m_list: {m_list}")
#         for ai_move in m_list:
#             state = connect4_ui.make_move(state, ai_move)

#         out = connect4_ui_soln.print_board(state)

#         print("printing of board test 11")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())  

    
#     @weight(10)
#     def test_case12(self):
#         '''Testing Console AI with 20x20 game by having AI play against AI'''      
#         random.seed(23)
#         columns = 20
#         rows = 20
#         state = connect4.new_game(columns, rows)
#         state_ans = connect4.new_game(columns, rows)
#         m_list = []
#         player = True
#         move = None

#         while connect4.winner(state) == connect4.EMPTY:
#             out = connect4_ui_soln.print_board(state)
#             # ans = connect4_ui_soln.print_board(state_ans)
#             if player:
#                 state_og = state
#                 # state = connect4_ui_ai_soln.make_move(state, connect4_ui_ai_soln.choose_move(state))
#                 while state_og == state:
#                     move = connect4_ui_ai.ai_move(state)
#                     state = connect4_ui.make_move(state, move )
#                 m_list.append(move)
#             else:
#                 state_og = state
#                 while state_og == state:
#                     move =  connect4_ui_ai.ai_move(state)
#                     state = connect4_ui.make_move(state, move)
#                 m_list.append(move)
#             player = not player

#         out = (connect4_ui_soln.print_board(state))
#         # print("out:\n" + out)

#         # print(f"m_list: {m_list}")
#         for ai_move in m_list:
#             state_ans = connect4_ui_soln.make_move(state_ans, ai_move)

#         ans = connect4_ui_soln.print_board(state_ans)

#         print("printing of board")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())  

#     @weight(10)
#     def test_case13(self):
#         '''Testing Console AI with 4x4 game by having AI play against AI'''
#         random.seed(23)
#         columns = 4
#         rows = 4
#         state = connect4.new_game(columns, rows)
#         state_ans = connect4.new_game(columns, rows)
#         m_list = []
#         player = True
#         move = None

#         while connect4.winner(state) == connect4.EMPTY:
#             out = connect4_ui_soln.print_board(state)
#             # ans = connect4_ui_soln.print_board(state_ans)
#             if player:
#                 state_og = state
#                 # state = connect4_ui_ai_soln.make_move(state, connect4_ui_ai_soln.choose_move(state))
#                 while state_og == state:
#                     move = connect4_ui_ai.ai_move(state)
#                     state = connect4_ui.make_move(state, move )
#                 m_list.append(move)
#             else:
#                 state_og = state
#                 while state_og == state:
#                     move =  connect4_ui_ai.ai_move(state)
#                     state = connect4_ui.make_move(state, move)
#                 m_list.append(move)
#             player = not player

#         out = (connect4_ui_soln.print_board(state))
#         print("out:\n" + out)

#         print(f"m_list: {m_list}")
#         for ai_move in m_list:
#             state_ans = connect4_ui_soln.make_move(state_ans, ai_move)

#         ans = connect4_ui_soln.print_board(state_ans)

#         print("printing of board test 11")
#         print("out:\n" + out)
#         print("ans:\n" + ans)
#         self.assertTrue(ans.strip() in out.strip())  

#     @weight(10)
#     def test_case14(self):
#         random.seed(8000)
#         columns = 4
#         rows = 4
#         player = True
#         networked_ai = True
#         start = ""

#         server_thread = threading.Thread(target=connect4_network_server_test.start_server, args=("localhost", 8000))
#         # client_thread = threading.Thread(target=client_short.connect, args=("localhost", 8000))
#         server_thread.start()
#         sleep(1)

#         connection = client_short.connect("localhost", 8000)
    
#         # connection = client_thread.start()

#         output_msg = "GAME " + str(rows) + " " + str(columns)
#         client_short.send_message(connection, output_msg)

#         state = connect4.new_game(columns, rows)
#         while start != "START":
#             start = client_short.receive_response(connection).strip()

#         print("Received START")

#         while connect4.winner(state) == connect4.EMPTY:
#             # print(connect4_ui_soln.print_board(state))
#             if player:
#                 state_og = state
#                 while state_og == state:
#                     move =  connect4_ui_ai.ai_move(state)
#                     # move = connect4_ui_soln.choose_move(state)
#                     state = connect4_ui.make_move(state, move)
#                 print("Found move")
#                 if networked_ai:
#                     client_short.send_message(connection,f"USER {move[0]} {move[1]}") 
#                     received = client_short.receive_response(connection).strip()  
#                     print(received)           
#             else:
#                 state_og = state
#                 while state_og == state:
#                     if networked_ai == False:
#                         state = connect4_ui.make_move(state, connect4_ui_ai.ai_move(state))
#                     else:
#                         # get move and column from server
#                         # print(state)
                        
#                         client_short.send_message(connection,"MOVE")
#                         print("Waiting for AI MOVE")
#                         move = int(client_short.receive_response(connection).strip())
#                         print("AI MOVE:", move)
#                         client_short.send_message(connection,"COLUMN")
#                         column = int(client_short.receive_response(connection).strip())
#                         print("AI COLUMN:", column)
#                         state = connect4_ui.make_move(state, (move, column))                    
#             player = not player

#         print(connect4_ui.print_board(state))
#         if networked_ai:
#             client_short.close(connection)

#         self.assertTrue(True) 


#     @weight(10)
#     def test_case15(self):
#         random.seed(23)
#         columns = 20
#         rows = 20
#         player = True
#         networked_ai = True
#         start = ""

#         server_thread = threading.Thread(target=connect4_network_server_test.start_server, args=("localhost", 8000))
#         # client_thread = threading.Thread(target=client_short.connect, args=("localhost", 8000))
#         server_thread.start()
#         sleep(1)

#         connection = client_short.connect("localhost", 8000)
    
#         # connection = client_thread.start()

#         output_msg = "GAME " + str(rows) + " " + str(columns)
#         client_short.send_message(connection, output_msg)

#         state = connect4.new_game(columns, rows)

#         while start != "START":
#             start = client_short.receive_response(connection).strip()

#         print("Received START")

#         while connect4.winner(state) == connect4.EMPTY:
#             # print(connect4_ui_soln.print_board(state))
#             if player:
#                 state_og = state
#                 while state_og == state:
#                     move =  connect4_ui_ai.ai_move(state)
#                     # move = connect4_ui_soln.choose_move(state)
#                     state = connect4_ui.make_move(state, move)
#                 print("Found move")
#                 if networked_ai:
#                     client_short.send_message(connection,f"USER {move[0]} {move[1]}") 
#                     received = client_short.receive_response(connection).strip()  
#                     print(received)             
#             else:
#                 state_og = state
#                 while state_og == state:
#                     if networked_ai == False:
#                         state = connect4_ui.make_move(state, connect4_ui_ai.ai_move(state))
#                     else:
#                         # get move and column from server
#                         # print(state)
                        
#                         client_short.send_message(connection,"MOVE")
#                         print("Waiting for AI MOVE")
#                         move = int(client_short.receive_response(connection).strip())
#                         print("AI MOVE:", move)
#                         client_short.send_message(connection,"COLUMN")
#                         column = int(client_short.receive_response(connection).strip())
#                         print("AI COLUMN:", column)
#                         state = connect4_ui.make_move(state, (move, column))                    
#             player = not player

#         print(connect4_ui.print_board(state))
#         if networked_ai:
#             client_short.close(connection)

#         self.assertTrue(True) 