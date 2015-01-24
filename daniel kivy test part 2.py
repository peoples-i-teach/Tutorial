#Yazmeen's App, a scouting app for FIRST robotics
#Copyright (C) 2014 Camden County Technical Schools FRC Team 203
#Written by Juliet Summers
# This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
<CountingButton>:
    size_hint: (.5, .5)
    rows: 3
    label: ''
    decreaseNum: -1
    increaseNum: 1
    Label:
        size_hint: (.5, .5)
        text: root.label
    Label:
        id: display
#what the hell it doesn't change the text color
        color: (1,0,0)
        text: '0'
    GridLayout:
        id: buttons
        rows: 2
        Button:
            #no - sign for this because it's already on the number
            text: '%i'%root.decreaseNum
            on_release: root.callback(root.decreaseNum, display)
        Button:
            text: '+%i'%root.increaseNum
            on_release: root.callback(root.increaseNum, display)
<ButtonThing>:
    cols: 2
	size_hint: (.5, .5)
    CountingButton:
        decreaseNum: -2
        increaseNum: 2
        label: 'idk'
    CountingButton:
        label: 'thingy'

Enter file contents here
