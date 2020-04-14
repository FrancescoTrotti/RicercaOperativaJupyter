#!/usr/bin/python

import sys


problem = sys.argv[1]
html_text = ""

# not used at moment
#flags_for_js = ['false', 'false', 'false', 'false', 'false', 'false', 'false', 'false']
not_editable = ['false', 'false']
if ('none' in yaml_tools.get(problem)):
    not_editable[0] = 'true'
    not_editable[1] = 'true'
    
if('select_color_node' in yaml_tools.get(problem)):
    #flags_for_js[0] = 'true'
    html_text = '''<div>
        <button class="button" id="btn_set_one">Select</button>
    </div>
    <div>
        <button class="button" id="btn_set_two">Select</button>
    </div>
    <div>
        <button class="button" id="btn_unselect_set">Unselect</button>
    </div>'''
if('drag_node' in yaml_tools.get(problem)):
    not_editable[1] = 'true'
    #flags_for_js[1] = 'true'
if('remove_edge' in yaml_tools.get(problem)):
    #flags_for_js[2] = 'true'
    html_text = html_text + '''<div>
            <button class="button" id="btn_remove_e">Remove Edge</button>
        </div>'''

if('remove_node' in yaml_tools.get(problem)): 
    #flags_for_js[3] = 'true'
    html_text = html_text + '''<div>
            <button class="button" id="btn_remove">Remove Node</button>
        </div>'''

if('add_node' in yaml_tools.get(problem)):
    #flags_for_js[4] = 'true'
    html_text = html_text + '''<div>
            <button class="button" id="btn_add">Add Node</button>
        </div>'''

if('add_edge' in yaml_tools.get(problem)):
    #flags_for_js[5] = 'true'
    html_text = html_text + '''<div>
            <button class="button" id="btn_add_e">Add Edge</button>
        </div>'''

if('choice' in yaml_tools.get(problem)): 
    #flags_for_js[6] = 'true'
    html_text = html_text + '''<div>
            <button class="button" id="yes">Yes</button>
            </div>
            <div>
            <button class="button" id="no">No</button>
        </div>'''

if('edit_label' in yaml_tools.get(problem)): 
    #flags_for_js[7] = 'true'
    html_text = html_text + '''TODO'''
    
    
if('all' in yaml_tools.get(problem)): 
    #flags_for_js[7] = 'true'
    html_text =''' <div>
        <button class="button" id="btn_set_one">Select</button>
    </div>
    <div>
        <button class="button" id="btn_set_two">Select</button>
    </div>
    <div>
        <button class="button" id="btn_unselect_set">Unselect</button>
    </div> 
    <div>
        <button class="button" id="btn_remove_e">Remove Edge</button>
    </div>
    <div>
        <button class="button" id="btn_remove">Remove Node</button>
    </div>
    <div>
            <button class="button" id="btn_add">Add Node</button>
        </div>
    <div>
        <button class="button" id="btn_add_e">Add Edge</button>
    </div>
    <div>
        <button class="button" id="yes">Yes</button>
    </div>
    <div>
        <button class="button" id="no">No</button>
    </div>
    '''