#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`sudoku_solver` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides sudoku solver's primitive operations

:Provides:

* `print_grid`
* `MAJ_hipothetic`
* `is_solved`
* `find_cell_min`
* `not_solved`
* `search_sol`
"""


import sudoku_grid,cells

sol_way = list()
sud_notfinished = "490001007000045030382600050003070401800902005907030600030006529020850000500700013"
sud_finished = "495381267671245938382697154263578491814962375957134682738416529129853746546729813"
sud_2sol = '495381267671245938382697154263578400814962375957134682738426500129853746546791823'

def print_grid(grid):
    """
    print the sudoku's grid

    :param grid: a sudoku's grid
    :type grid: grid
    :return: None
    :rtype: NoneType
    :Action: print the grid
    :UC: none
    
    :Examples:
    >>> grid = sudoku_grid.make_grid(sudoku_grid.val_test)
    >>> print_grid(grid)
    +-------+-------+-------+
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    +-------+-------+-------+
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    +-------+-------+-------+
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    +-------+-------+-------+
    """
    print('+'+'-------+'*3)
    for l1 in range(3):
        for l2 in range(3):
            print('|',end='')
            for c1 in range(3):
                for c2 in range(3):
                    if cells.get_cellvalue(sudoku_grid.get_cell(grid,l1*3+l2,c1*3+c2)) == '0':
                        print(' .',end='')
                    else:
                        print(' '+cells.get_cellvalue(sudoku_grid.get_cell(grid,l1*3+l2,c1*3+c2)),end='')
                print(' |',end='')
            print()
        print('+'+'-------+'*3)

def is_solved(grid):
    """
    verify if the grid is solved

    :param grid: the sudoku's grid
    :type grid: grid
    :return: True if the sudoku is solved and False if not
    :rtype: bool
    :UC: none

    :Example:
    >>> grid1 = sudoku_grid.make_grid()
    >>> grid2 = sudoku_grid.make_grid(sud_finished)
    >>> is_solved(grid1)
    False
    >>> is_solved(grid2)
    True
    """
    for i in range(9):
        ens_cell_in_line = set()
        for cell in sudoku_grid.get_line(grid,i):
            ens_cell_in_line.add(cells.get_cellvalue(cell))
            if cells.get_cellvalue(cell) == '0':
                return False
        if len(ens_cell_in_line) != len(sudoku_grid.get_line(grid,i)):
            return False
    return True

def MAJ_hipothetic(cell_list,hipo):
    """
    up-date the cells' hipothetics values of cell_list with the value of the other cells of cell_value

    :param cell_list: a list of cells
    :type cell_list: list
    :return: None
    :rtype: NoneType
    :Action: up-date the hipohtetics value of each cell of cell_list
    :UC: none

    :Examples:
    >>> cell_list = [cells.create('0') for i in range(9)]
    >>> for cell in cell_list: print(set(int(i) for i in cells.get_cellhipo(cell)))
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    >>> cells.set_cellvalue(cell_list[0],1)
    >>> MAJ_hipothetic(cell_list,'1')
    >>> for cell in cell_list: print(set(int(i) for i in cells.get_cellhipo(cell)))
    set()
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    """
    for cell in cell_list:
        cells.unset_cellhipothetic(cell,hipo)

def find_cell_min(grid):
    """
    search the cell of the grid with the highter contraints

    :param grid: a sudoku's grid
    :type grid: grid
    :return: the cell with the most contraints
    :rtype: cell
    :UC: none
    >>> 
    """
    cell_min = (cells.create('0'),0,0)
    for ind_line in range(9):
        for ind_col in range(9):
            cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
            if 0<len(cells.get_cellhipo(cell))<=len(cells.get_cellhipo(cell_min[0])):
                cell_min = (cell,ind_col,ind_line)
    return cell_min

def not_solved(grid):
    """
    say if it's impossible to find solution of the sudoku's grid
    
    :param grid: a sudoku's grid
    :type grid: grid
    :return: True if it's impossible to find solution and False if not
    :rtype: bool
    :UC: none
    """
    for i in range(9):
        for cell in sudoku_grid.get_line(grid,i):
            if cells.get_cellvalue(cell) == '0' and not cells.get_cellhipo(cell):
                return True
    return False

def complete_1hipo(grid,talkative=False):
    global sol_way
    boolean = True
    while boolean:
        boolean = False
        for ind_line in range(9):
            for ind_col in range(9):
                cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
                if len(cells.get_cellhipo(cell)) == 1:
                    boolean = True
                    value = cells.get_cellhipo(cell).pop()
                    sol_way += [(value,ind_col,ind_line)]
                    cells.set_cellvalue(cell,value)
                    if talkative:
                        print_grid(grid)
                    func_lists = [sudoku_grid.get_line(grid,ind_line),sudoku_grid.get_colomn(grid,ind_col),sudoku_grid.get_square(grid,(ind_col//3) + (ind_line//3)*3)]
                    for cell_list in func_lists:
                        MAJ_hipothetic(cell_list,value)

def search_sol(grid,talkative=False):
    """
    this algorithm search all solutions of a sudoku

    :param string: a string with all values of a sudoku
    :type string: str
    :return:
    :rtype:
    :UC: none
    """
    global sol_way
    complete_1hipo(grid,talkative=talkative)
    if is_solved(grid):
        if not talkative:
            print_grid(grid)
    elif not_solved(grid):
        pass
    else:
        grid_list = list()
        cell_min = find_cell_min(grid)
        list_hipo = cells.get_cellhipo(cell_min[0])
        for hipo in list_hipo:
            sol_way += [(str(hipo),cell_min[1],cell_min[2])]
            cells.set_cellvalue(cell_min[0],hipo)
            grid_list += [sudoku_grid.grid2string(grid)]
        for string in grid_list:
            grid = sudoku_grid.make_grid(string)
            if talkative:
                print_grid(grid)
            search_sol(grid,talkative=talkative)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
