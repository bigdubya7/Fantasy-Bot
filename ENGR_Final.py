# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:03:46 2020

@author: 19795
"""


#Purpose and set of instructions:
print("Welcome! I am the Fantasy Football Assistant.")
print("Throughout our time together, I will help you build the best football team in the league!")
print("To do so, I will be asking a series of questions related to your team and league.")
print("Next, all you have to do is answer these questions and I will do my best to help!")
print("Note: When choosing players, make sure to input their full name.")
print("Let's get started!")
print(("\U0001f3c8" + "\t") * 24)

# Obtain data from Excel file
# Use Pandas package to read in data from excel file
import pandas as pd
# Make a Data Frame for each sheet in the excel file
with pd.ExcelFile("Fantasy-Football-Rankings-PPR.xlsx") as xls:
    df1 = pd.read_excel(xls, 'QB')
    df2 = pd.read_excel(xls, 'RB')
    df3 = pd.read_excel(xls, 'WR')
    df4 = pd.read_excel(xls, 'TE')
    df5 = pd.read_excel(xls, 'K')
    df6 = pd.read_excel(xls, 'DEF')
    df7 = pd.read_excel(xls, 'IDP')
    df8 = pd.read_excel(xls, 'ALL')
    
# Add headers for each data Frame to a new list
# Convert each data frame to a list of lists and add appropriate headers

# Quaterback data
QB_headers = df1.columns.values.tolist()
QB_data = df1.values.tolist()
QB_data.insert(0, QB_headers)
# Running back data
RB_headers = df2.columns.values.tolist()
RB_data = df2.values.tolist()
RB_data.insert(0, RB_headers)
# Wide Receiver data
WR_headers = df3.columns.values.tolist()
WR_data = df3.values.tolist()
WR_data.insert(0, WR_headers)
# Tight End data
TE_headers = df4.columns.values.tolist()
TE_data = df4.values.tolist()
TE_data.insert(0, TE_headers)
# Kicker data
K_headers = df5.columns.values.tolist()
K_data = df5.values.tolist()
K_data.insert(0, K_headers)
# Team Defense data
DEF_headers = df6.columns.values.tolist()
DEF_data = df6.values.tolist()
DEF_data.insert(0, DEF_headers)
# Individual Defensive Player data
IDP_headers = df7.columns.values.tolist()
IDP_data = df7.values.tolist()
IDP_data.insert(0, IDP_headers)
# All players data
ALL_headers = df8.columns.values.tolist()
ALL_data = df8.values.tolist()
ALL_data.insert(0, ALL_headers)

# Search for player in the ALL list
# Get position of player
def position(name):
    for i in range(len(ALL_data)):
        for j in range(len(ALL_data[i])):
            if ALL_data[i][j] == name:
                return ALL_data[i][-1]

# Make a dictionary for specified positon of player with the data of specified position
position_data = {"QB" : QB_data, "RB" : RB_data, "WR" : WR_data, "TE" : TE_data, "K" : K_data, "DEF" : DEF_data, "IDP" : IDP_data}
# Search for player in the specified postion data
# Match the desired data with the player
def stat(name, data):
    
    player_position_data = position_data[position(name)]
    for i in range(len(player_position_data[0])):
        if player_position_data[0][i] == data:
            column_num = i
    for k in range(len(player_position_data)):
        for l in range(len(player_position_data[k])):
            if player_position_data[k][l] == name:
                list_num = k
    out = name + '\n' + data + ": " + str(player_position_data[list_num][column_num])
    return out

def bestplayers(available):
    ''' This function takes in a paramater of the available players in a list.
    With this information it is able to pull the first three lists up and find the fourth item in those lists
    to determine the next best players based on the POS stat.'''
    com=', '
    bestplayer1=available[1][4]
    bestplayer2=available[2][4]
    bestplayer3=available[3][4]
    print('The next three best picks are', bestplayer1 + com + bestplayer2 + com +'and', bestplayer3)
def deletefromlist(available, pick):
    for i in range(len(available)):
        if available[i][4] == pick:
            available.pop(i)
            break
def userpick(available): 
    '''This function allows the user to input the name of a player of then that name is taken out of
    the avaible players list for future use. The picked player is also added onto another list
    that stores all players who have been picked.'''
    pick=input('Enter the next pick: ')
    team.append(pick)
    try:
        deletefromlist(available,pick)
    except:
        print('Enter an available player')
        deletefromlist(available,pick)

    # for i in range(len(available)):
    #     if available[i][4] == pick:
    #         available.pop(i)
    #         break

available = ALL_data
team = []
#Menu function that gives as options if you want to see top players,
#see specific player stats, leave the application, or go to the next round.
def menu(available):
    '''Menu that provides options to view player stats, top players, go to next round of draft, or leave application.'''
    count = 0
    user = 0
    while user != 5:
        print("\n")
        print("What would you like to do?")
        print("If you would like to search up a specific player's stats, please enter 1.")
        print("If you would like to see a list of the next best players to choose from, please enter 2.")
        print("If you would like to jump into the next round of the draft, please enter 3.")
        print("If you would like to see the players who have already been drafted, please enter 4.")
        print("If you would like to quit the application, please enter 5.")
        user = input("Enter your choice here: ")
        print("\n")
        while True:
            try:
                user = int(user)
                break
            except:
                user = input("Please enter an integer: ")
        if user == 1:
            name = input("Please enter the full name of the player you want to search: ")
            data = input("Please enter what type of stat you'd like to find: ")
            print(stat(name,data))
        elif user == 2:
            bestplayers(available)
        elif user == 3:
            count += 1
            rounds(count)
        elif user == 4:
            if len(team) == 0:
                print("No players drafted yet!")
            else:
                print("\U0001f3c8","Drafted Players:","\U0001f3c8")
                for i in team:
                    print(i)
    print("Ok. Goodbye and good luck!")
#Rounds function that states what round it is and allows the player to inout their
#chosen player and other players that other people have chosen.
def rounds(count):
    '''Keeps track of rounds of draft.'''
    print("\U0001f3c8","Draft: Round", count,"\U0001f3c8")
    userpick(available)
menu(available)
    