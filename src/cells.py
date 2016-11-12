#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cells` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides cells' primitive operations for the sudoku solver.

:Provides:

* `create`
* `get_cellvalue`
* `get_cellhipo`
* `set_cellvalue`
* `unset_cellhipothetic`
"""

import sudoku_grid

#############################
# Exceptions for gthe grid
#############################

class NotCorrectValueError(Exception):
    """
    Exception for not correct values of the grid
    """
    def __init__(self, msg):
        self.message = msg

        
##############################################
# Functions for grid's setup and management
##############################################


   ###############
   # Constructor #
   ###############

def create():
    """
    :return: a new cell of a sudoku's grid.
    :rtype: cell
    :UC: none

    :Examples:
    >>> create() == ({'hipothetic': {'1', '2', '3', '4', '5', '6', '7', '8', '9'}, 'value': '0'} or {'value': '0', 'hipothetic': {'1', '2', '3', '4', '5', '6', '7', '8', '9'}})
    True
    """
    return {'value':'0','hipothetic':set(str(i) for i in range(1,10))}
        

   #############
   # Selectors #
   #############

def get_cellvalue(cell):
    """
    :param cell: a cell of the sudoku's grid
    :type cell: cell
    :return: the value of the cell
    :rtype: str
    :UC: none

    :Examples:
    >>> cell = create()
    >>> get_cellvalue(cell)
    '0'
    """
    return cell['value']

def get_cellhipo(cell):
    """
    :param cell: a cell of the sudoku's grid
    :type cell: cell
    :return: all of hipothetic values of the cell
    :rtype: set
    :UC: none
    
    :Examples:
    >>> cell = create()
    >>> get_cellhipo(cell) == {str(i) for i in range(1,10)}
    True
    """
    return cell['hipothetic']


   ############
   # modifier #
   ############
   
def set_cellvalue(cell,value):
    """
    :param cell: a cell of the sudoku's grid
    :type cell: cell
    :param value: the value of the cell
    :type value: str
    :return: None
    :rtype: NoneType
    :Action: modify the value of the cell
    :UC: value must be between 0 and 9

    :Examples:
    >>> cell = create()
    >>> get_cellvalue(cell)
    '0'
    >>> len(get_cellhipo(cell))
    9
    >>> set_cellvalue(cell,'5')
    >>> get_cellvalue(cell)
    '5'
    >>> len(get_cellhipo(cell))
    0
    >>> set_cellvalue(cell,-1)
    Traceback (most recent call last):
    ...
    NotCorrectValueError: value must be an integer between 0 and 9
    >>> set_cellvalue(cell,10)
    Traceback (most recent call last):
    ...
    NotCorrectValueError: value must be an integer between 0 and 9
    """
    if int(value) in range(10):
        cell['value'] = value
        if value != '0':
            cell['hipothetic'] = set() #on enlève toutes les valeurs hipothetiques si la valeur que l'on donne est différente de 0
        else:
            cell['hipothetic'] = set(str(i) for i in range(1,10)) #et on ajoute toutes les valeurs hipothetiques possibles si la valeur que l'on donne à la cellule est nul
    else:
        raise NotCorrectValueError("value must be an integer between 0 and 9")

def unset_cellhipothetic(cell,hipo):
    """
    :param cell: a cell of the sudoku's grid
    :type cell: cell
    :param hipo: an hipothetic value
    :type hipo: int
    :return: None
    :rtype: NoneType
    :Action: unset hipo of the hipothetics value of the cell
    :UC: none

    :Examples:
    >>> cell = create()
    >>> unset_cellhipothetic(cell,'2')
    >>> '2' in get_cellhipo(cell)
    False
    """
    if hipo in get_cellhipo(cell):
        cell['hipothetic'].remove(hipo)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
