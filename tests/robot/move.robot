*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py
/main/tests/robot/images/IMG_6617.HEIC

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
origin N                            0             0             1                     NORTH           0           1           2
origin S                            0             0             5                     EAST            1           0           6
origin E                            0             0             1                     WEST            0           0           2
Origin W                            0             0             5                     SOUTH           0           0           6
End N                               9             9             1                     NORTH           9           9           2
End E                               9             9             5                     EAST            9           9           6
End W                               9             9             5                     WEST            8           9           6
End S                               9             9             5                     SOUTH           9           8           6
RH corner N                         0             9             5                     NORTH           0           9           6
RH corner E                         0             9             5                     EAST            1           9           6
RH Corner W                         0             9             5                     WEST            0           9           6
RH Corner S                         0             9             5                     SOUTH           0           8           6
TL Corner N                         9             0             5                     NORTH           9           1           6
TL Corner E                         9             0             5                     EAST            9           0           6
TL Corner W                         9             0             5                     WEST            8           0           6
TL Corner S                         9             0             1                     SOUTH           9           0           2
Center of board  N                  4             5             5                     NORTH           4           6           6
Center of board  E                  4             5             5                     EAST            5           5           6
Center of board  W                  4             5             5                     WEST            3           5           6
Center of board  S                  4             5             5                     SOUTH           4           4           6


*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}