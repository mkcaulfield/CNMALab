#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on Thu Dec 15 10:18:15 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'fMRI_Stimuli_K_Study_Draft'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/marycaulfield/Desktop/Personal/DataWorkforLauren/PsychoPy-KStudy/10.17.22_fMRItask/PhantomScanVersion_10.15.22/fMRI_Stimuli_K_Study_MKC_12.07.22scannerversion_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "waitForTrigger" ---
triggerCheck = keyboard.Keyboard()
displayWaiting = visual.TextStim(win=win, name='displayWaiting',
    text='Awaiting start signal from scanner...',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "DispThought" ---
ThoughtText = visual.TextStim(win=win, name='ThoughtText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Disengage" ---
D_Cue = visual.TextStim(win=win, name='D_Cue',
    text='',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
D_Fixation = visual.ShapeStim(
    win=win, name='D_Fixation', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-1.0, interpolate=True)
D_Response = keyboard.Keyboard()

# --- Initialize components for Routine "Reflection" ---
Reflect = visual.TextStim(win=win, name='Reflect',
    text='Notice thoughts',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "ThoughtProbes" ---
slider = visual.Slider(win=win, name='slider',
    startValue=50, size=(1.0, 0.1), pos=(0, -.25), units=None,
    labels=None, ticks=(range(0,101,5)), granularity=5.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=0, readOnly=False)
# Run 'Begin Experiment' code from sliderCode
# These are the initial values to be used later to control 
# the countdown for total time allowed for each round of 6 thought probes
sliderTimerStarted = False
slidersTimedOut = False
sliderText = visual.TextStim(win=win, name='sliderText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
showPos = visual.TextStim(win=win, name='showPos',
    text='',
    font='Open Sans',
    pos=(0, -.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "ProbesPause" ---
Fixation_earlyfinish = visual.ShapeStim(
    win=win, name='Fixation_earlyfinish', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Fixation" ---
Fixation_P = visual.ShapeStim(
    win=win, name='Fixation_P', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
RunBlocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Runs.csv'),
    seed=None, name='RunBlocks')
thisExp.addLoop(RunBlocks)  # add the loop to the experiment
thisRunBlock = RunBlocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRunBlock.rgb)
if thisRunBlock != None:
    for paramName in thisRunBlock:
        exec('{} = thisRunBlock[paramName]'.format(paramName))

for thisRunBlock in RunBlocks:
    currentLoop = RunBlocks
    # abbreviate parameter names if possible (e.g. rgb = thisRunBlock.rgb)
    if thisRunBlock != None:
        for paramName in thisRunBlock:
            exec('{} = thisRunBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "waitForTrigger" ---
    continueRoutine = True
    # update component parameters for each repeat
    triggerCheck.keys = []
    triggerCheck.rt = []
    _triggerCheck_allKeys = []
    # keep track of which components have finished
    waitForTriggerComponents = [triggerCheck, displayWaiting]
    for thisComponent in waitForTriggerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "waitForTrigger" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *triggerCheck* updates
        waitOnFlip = False
        if triggerCheck.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            triggerCheck.frameNStart = frameN  # exact frame index
            triggerCheck.tStart = t  # local t and not account for scr refresh
            triggerCheck.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triggerCheck, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'triggerCheck.started')
            triggerCheck.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(triggerCheck.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(triggerCheck.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if triggerCheck.status == STARTED and not waitOnFlip:
            theseKeys = triggerCheck.getKeys(keyList=['t','equal'], waitRelease=False)
            _triggerCheck_allKeys.extend(theseKeys)
            if len(_triggerCheck_allKeys):
                triggerCheck.keys = _triggerCheck_allKeys[-1].name  # just the last key pressed
                triggerCheck.rt = _triggerCheck_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *displayWaiting* updates
        if displayWaiting.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            displayWaiting.frameNStart = frameN  # exact frame index
            displayWaiting.tStart = t  # local t and not account for scr refresh
            displayWaiting.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(displayWaiting, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'displayWaiting.started')
            displayWaiting.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitForTriggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "waitForTrigger" ---
    for thisComponent in waitForTriggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if triggerCheck.keys in ['', [], None]:  # No response was made
        triggerCheck.keys = None
    RunBlocks.addData('triggerCheck.keys',triggerCheck.keys)
    if triggerCheck.keys != None:  # we had a response
        RunBlocks.addData('triggerCheck.rt', triggerCheck.rt)
    # the Routine "waitForTrigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    TrialBlocks = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("ThoughtStimuli_subject"+expInfo['participant']+"_run"+str(RunNumber)+".csv"),
        seed=None, name='TrialBlocks')
    thisExp.addLoop(TrialBlocks)  # add the loop to the experiment
    thisTrialBlock = TrialBlocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialBlock.rgb)
    if thisTrialBlock != None:
        for paramName in thisTrialBlock:
            exec('{} = thisTrialBlock[paramName]'.format(paramName))
    
    for thisTrialBlock in TrialBlocks:
        currentLoop = TrialBlocks
        # abbreviate parameter names if possible (e.g. rgb = thisTrialBlock.rgb)
        if thisTrialBlock != None:
            for paramName in thisTrialBlock:
                exec('{} = thisTrialBlock[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "DispThought" ---
        continueRoutine = True
        # update component parameters for each repeat
        ThoughtText.setText(Thought)
        # keep track of which components have finished
        DispThoughtComponents = [ThoughtText]
        for thisComponent in DispThoughtComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "DispThought" ---
        while continueRoutine and routineTimer.getTime() < 34.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ThoughtText* updates
            if ThoughtText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ThoughtText.frameNStart = frameN  # exact frame index
                ThoughtText.tStart = t  # local t and not account for scr refresh
                ThoughtText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ThoughtText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ThoughtText.started')
                ThoughtText.setAutoDraw(True)
            if ThoughtText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ThoughtText.tStartRefresh + 34-frameTolerance:
                    # keep track of stop time/frame for later
                    ThoughtText.tStop = t  # not accounting for scr refresh
                    ThoughtText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ThoughtText.stopped')
                    ThoughtText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in DispThoughtComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DispThought" ---
        for thisComponent in DispThoughtComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-34.000000)
        
        # set up handler to look after randomisation of conditions etc
        DisengageLoop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions("SART_subject"+expInfo['participant']+"_run"+str(RunNumber)+"_thought"+str(ThoughtNumber)+".csv"),
            seed=None, name='DisengageLoop')
        thisExp.addLoop(DisengageLoop)  # add the loop to the experiment
        thisDisengageLoop = DisengageLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDisengageLoop.rgb)
        if thisDisengageLoop != None:
            for paramName in thisDisengageLoop:
                exec('{} = thisDisengageLoop[paramName]'.format(paramName))
        
        for thisDisengageLoop in DisengageLoop:
            currentLoop = DisengageLoop
            # abbreviate parameter names if possible (e.g. rgb = thisDisengageLoop.rgb)
            if thisDisengageLoop != None:
                for paramName in thisDisengageLoop:
                    exec('{} = thisDisengageLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Disengage" ---
            continueRoutine = True
            # update component parameters for each repeat
            D_Cue.setText(stimulus)
            D_Response.keys = []
            D_Response.rt = []
            _D_Response_allKeys = []
            # keep track of which components have finished
            DisengageComponents = [D_Cue, D_Fixation, D_Response]
            for thisComponent in DisengageComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Disengage" ---
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *D_Cue* updates
                if D_Cue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    D_Cue.frameNStart = frameN  # exact frame index
                    D_Cue.tStart = t  # local t and not account for scr refresh
                    D_Cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(D_Cue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D_Cue.started')
                    D_Cue.setAutoDraw(True)
                if D_Cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > D_Cue.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        D_Cue.tStop = t  # not accounting for scr refresh
                        D_Cue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'D_Cue.stopped')
                        D_Cue.setAutoDraw(False)
                
                # *D_Fixation* updates
                if D_Fixation.status == NOT_STARTED and tThisFlip >= .25-frameTolerance:
                    # keep track of start time/frame for later
                    D_Fixation.frameNStart = frameN  # exact frame index
                    D_Fixation.tStart = t  # local t and not account for scr refresh
                    D_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(D_Fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D_Fixation.started')
                    D_Fixation.setAutoDraw(True)
                if D_Fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > D_Fixation.tStartRefresh + 1.75-frameTolerance:
                        # keep track of stop time/frame for later
                        D_Fixation.tStop = t  # not accounting for scr refresh
                        D_Fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'D_Fixation.stopped')
                        D_Fixation.setAutoDraw(False)
                
                # *D_Response* updates
                waitOnFlip = False
                if D_Response.status == NOT_STARTED and tThisFlip >= .25-frameTolerance:
                    # keep track of start time/frame for later
                    D_Response.frameNStart = frameN  # exact frame index
                    D_Response.tStart = t  # local t and not account for scr refresh
                    D_Response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(D_Response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D_Response.started')
                    D_Response.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(D_Response.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(D_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if D_Response.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > D_Response.tStartRefresh + 1.75-frameTolerance:
                        # keep track of stop time/frame for later
                        D_Response.tStop = t  # not accounting for scr refresh
                        D_Response.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'D_Response.stopped')
                        D_Response.status = FINISHED
                if D_Response.status == STARTED and not waitOnFlip:
                    theseKeys = D_Response.getKeys(keyList=[None,'2'], waitRelease=False)
                    _D_Response_allKeys.extend(theseKeys)
                    if len(_D_Response_allKeys):
                        D_Response.keys = _D_Response_allKeys[0].name  # just the first key pressed
                        D_Response.rt = _D_Response_allKeys[0].rt
                        # was this correct?
                        if (D_Response.keys == str(correct)) or (D_Response.keys == correct):
                            D_Response.corr = 1
                        else:
                            D_Response.corr = 0
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in DisengageComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Disengage" ---
            for thisComponent in DisengageComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if D_Response.keys in ['', [], None]:  # No response was made
                D_Response.keys = None
                # was no response the correct answer?!
                if str(correct).lower() == 'none':
                   D_Response.corr = 1;  # correct non-response
                else:
                   D_Response.corr = 0;  # failed to respond (incorrectly)
            # store data for DisengageLoop (TrialHandler)
            DisengageLoop.addData('D_Response.keys',D_Response.keys)
            DisengageLoop.addData('D_Response.corr', D_Response.corr)
            if D_Response.keys != None:  # we had a response
                DisengageLoop.addData('D_Response.rt', D_Response.rt)
            # using non-slip timing so subtract the expected duration of this Routine
            routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'DisengageLoop'
        
        
        # --- Prepare to start Routine "Reflection" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ReflectionComponents = [Reflect]
        for thisComponent in ReflectionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Reflection" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Reflect* updates
            if Reflect.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Reflect.frameNStart = frameN  # exact frame index
                Reflect.tStart = t  # local t and not account for scr refresh
                Reflect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Reflect, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Reflect.started')
                Reflect.setAutoDraw(True)
            if Reflect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Reflect.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Reflect.tStop = t  # not accounting for scr refresh
                    Reflect.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Reflect.stopped')
                    Reflect.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ReflectionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Reflection" ---
        for thisComponent in ReflectionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        
        # set up handler to look after randomisation of conditions etc
        SliderLoop = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ProbeQuestions.csv'),
            seed=None, name='SliderLoop')
        thisExp.addLoop(SliderLoop)  # add the loop to the experiment
        thisSliderLoop = SliderLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSliderLoop.rgb)
        if thisSliderLoop != None:
            for paramName in thisSliderLoop:
                exec('{} = thisSliderLoop[paramName]'.format(paramName))
        
        for thisSliderLoop in SliderLoop:
            currentLoop = SliderLoop
            # abbreviate parameter names if possible (e.g. rgb = thisSliderLoop.rgb)
            if thisSliderLoop != None:
                for paramName in thisSliderLoop:
                    exec('{} = thisSliderLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "ThoughtProbes" ---
            continueRoutine = True
            # update component parameters for each repeat
            slider.reset()
            # Run 'Begin Routine' code from sliderCode
            # This piece of code starts a countdown for the total duration of 
            # each round of 6 thought probes
            if not sliderTimerStarted:
                sliderTimer = core.Clock()
                sliderTimer.addTime(-24)    # set the value in addTime() to the negative value of each loop's total time limit
                sliderTimerStarted = True
                slidersTimedOut = False
            
            # This piece of code reinitializes the slider 
            # object on each run through the routine in 
            # order to allow resetting of the labels
            slider = visual.Slider(win=slider.win, name=slider.name,
                startValue=slider.startValue, size=slider.size, pos=slider.pos, units=slider.units,
                labels=[leftanchor, rightanchor], ticks=slider.ticks, granularity=slider.granularity,
                style=slider.style, styleTweaks=slider.styleTweaks, opacity=slider.opacity,
                labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
                font=slider.font, labelHeight=slider.labelHeight,
                flip=slider.flip, ori=slider.ori, depth=slider.depth, readOnly=slider.readOnly)
            
            slider.marker.size = (0.05, 0.05) # Adjust marker size to fit better on small tick spaces
            
            # Clear the buffer of any prior keypresses
            event.clearEvents(eventType='keyboard')
            
            sliderText.setText(probetext)
            # keep track of which components have finished
            ThoughtProbesComponents = [slider, sliderText, showPos]
            for thisComponent in ThoughtProbesComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ThoughtProbes" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *slider* updates
                if slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    slider.frameNStart = frameN  # exact frame index
                    slider.tStart = t  # local t and not account for scr refresh
                    slider.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'slider.started')
                    slider.setAutoDraw(True)
                # Run 'Each Frame' code from sliderCode
                # This piece of code allows the slider to detect keyboard input
                keys = event.getKeys()
                
                if keys:
                    if '2' in keys:                      # This piece determines the keys that move the marker left
                        slider.markerPos -= slider.granularity
                    elif '3' in keys:                   # This piece determines the keys that move the marker right
                        slider.markerPos += slider.granularity
                    elif '1' in keys: # once space is pressed, that rating is set to markerPos and the trial terminates
                        slider.recordRating(slider.markerPos)
                        continueRoutine = False
                
                # This piece of code checks whether the countdown has expired (the clock has reached zero) and if so ends the routine
                if sliderTimer.getTime() >= 0:
                    continueRoutine = False
                    slidersTimedOut = True
                    SliderLoop.finished = True
                    sliderTimerStarted = False
                
                
                
                # *sliderText* updates
                if sliderText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    sliderText.frameNStart = frameN  # exact frame index
                    sliderText.tStart = t  # local t and not account for scr refresh
                    sliderText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sliderText, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sliderText.started')
                    sliderText.setAutoDraw(True)
                
                # *showPos* updates
                if showPos.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    showPos.frameNStart = frameN  # exact frame index
                    showPos.tStart = t  # local t and not account for scr refresh
                    showPos.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(showPos, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'showPos.started')
                    showPos.setAutoDraw(True)
                if showPos.status == STARTED:  # only update if drawing
                    showPos.setText(slider.getMarkerPos(), log=False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ThoughtProbesComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ThoughtProbes" ---
            for thisComponent in ThoughtProbesComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            SliderLoop.addData('slider.response', slider.getRating())
            SliderLoop.addData('slider.rt', slider.getRT())
            # Run 'End Routine' code from sliderCode
            SliderLoop.addData('slidersTimedOut',slidersTimedOut)
            # the Routine "ThoughtProbes" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'SliderLoop'
        
        
        # --- Prepare to start Routine "ProbesPause" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ProbesPauseComponents = [Fixation_earlyfinish]
        for thisComponent in ProbesPauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ProbesPause" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_earlyfinish* updates
            if Fixation_earlyfinish.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_earlyfinish.frameNStart = frameN  # exact frame index
                Fixation_earlyfinish.tStart = t  # local t and not account for scr refresh
                Fixation_earlyfinish.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_earlyfinish, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation_earlyfinish.started')
                Fixation_earlyfinish.setAutoDraw(True)
            # Run 'Each Frame' code from pause_code
            # This code makes a fixation cross display for 
            # the remaining duration of the 18 second probe time
            # and skips the cross if the probes timed out
            if sliderTimer.getTime() < 0:
                continueRoutine = True
            else: 
                continueRoutine = False
                
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ProbesPauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ProbesPause" ---
        for thisComponent in ProbesPauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "ProbesPause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from SliderReset
        sliderTimerStarted = False
        slidersTimedOut = False
        # keep track of which components have finished
        FixationComponents = [Fixation_P]
        for thisComponent in FixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_P* updates
            if Fixation_P.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_P.frameNStart = frameN  # exact frame index
                Fixation_P.tStart = t  # local t and not account for scr refresh
                Fixation_P.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_P, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation_P.started')
                Fixation_P.setAutoDraw(True)
            if Fixation_P.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation_P.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation_P.tStop = t  # not accounting for scr refresh
                    Fixation_P.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fixation_P.stopped')
                    Fixation_P.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'TrialBlocks'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'RunBlocks'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
