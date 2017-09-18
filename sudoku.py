"""Program to solve Sudoku puzzles given some starting condition"""

class sudoku():
    
    
    def __init__(self, in_master = None):
        """
        Creates the sudoku object and populates it using the input in_master.
        Contains a list containing each row of the puzzle as its own list,
        and a counter of blank spaces.
        Blank spaces in the lists are represented as 0s.
        """
        self.blanks = 81
        self.solutions = []
        if in_master:
            self.master = list(in_master)
            self._check_blanks()
        else:
            self.master = self._get_puzzle()
            self._check_blanks()
            
            #for row in range(9):
                #self.master.append([0] * 9)
        return
    
    
    def _check_blanks(self):
        for row in self.master:
            for digit in row:
                if digit:
                    self.blanks -= 1
    
    
    def _get_row(self, row):
        """Given a row number, returns a list of that row
        """
        return self.master[row]
    
    
    def _get_column(self, column):
        """Given a column number, returns a list of that column
        """
        column_list = []
        
        for row in range(9):
            column_list.append(self.master[row][column])

        return column_list
    
    
    def _get_zone(self, row, column):
        """Given a zone number, returns a list of that zone
        Zone layout:
            1-2-3
            4-5-6
            7-8-9
        """
        zone = []
        
        for zone_y in range(3):
            for zone_x in range(3):
                zone.append(self.master[zone_y + (row // 3 * 3)][zone_x + (column // 3 * 3)])

        return zone
    
    
    def _check_valid_move(self, digit, row, column):
        """Checks to see if placing the digit (1-9) at the position given by
        the row and column numbers is a valid move
        """
        if digit in self._get_row(row) or digit in self._get_column(column) or digit in self._get_zone(row, column):
            valid = False
        else:
            valid = True

        return valid
    
    
    def _find_next_blank(self):
        """Scans row by row until a blank space is found,
        returns its row and column
        """
        for row in range(9):
            for column in range(9):
                if self.master[row][column] == 0:
                    
                    return row, column
    
    
    def _place_digit(self, digit, row, column):
        """Places a digit in the specified position and updates the count of
        blanks"""
        self.master[row][column] = digit
        self.blanks -= 1
        
        return
    
    
    def _remove_digit(self, row, column):
        """Removes a digit from the specified position and updates the count of
        blanks"""
        self.master[row][column] = 0
        self.blanks += 1
        
        return
    
    
    def _check_solved(self):
        if self.blanks:
            return False
        else:
            return True
    
    
    def _save_solution(self):
        solution = []
        for row in self.master:
            solution.append(row[:])
        return solution


    def _get_puzzle(self):
        """Prompts user for input"""
        return list(list(map(int, input('>').split())) for __ in range(9))
        
        
    def display(self):
        counter = 1
        print('=' * 27)
        for solution in self.solutions:
            print('Solution {}'.format(counter))
            counter += 1
            for row in solution:
                print(row)
            print('=' * 27)
        return    
    
    
    def solve(self):
        """Solves the puzzle"""
        if self._check_solved():          
            self.solutions.append(self._save_solution())
            return
        else:
            (row, column) = self._find_next_blank()
            for digit in range(1, 10):
                if self._check_valid_move(digit, row, column):
                    self._place_digit(digit, row, column)
                    self.solve()
                    self._remove_digit(row, column)

if __name__ == '__main__':
    puzzle = sudoku()
    puzzle.solve()
    puzzle.display()
