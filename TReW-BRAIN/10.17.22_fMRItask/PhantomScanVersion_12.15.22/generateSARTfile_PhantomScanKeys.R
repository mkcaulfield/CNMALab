library(dplyr)
# This script generates a set of SART stimuli that adhere to the following rules when presented in order:

# Constraints:
# 5 no-go trials (8 is presented; goal is not to respond)
# 12-14 go trials (1-7 and 9; goal is to respond)
# No-go trials cannot occur back-to-back
# The last 10 seconds of each SART block (disengagement trial) should include 2 no-go trials

# The resulting stimuli files are intended for use with the PsychoPy script

# Researcher assistants: customize this section below here! --------------------------------------------

# Fill in with participant number
participant<-"001"

# Stop customizing! Don't change code below!------------------------------------------

# Identify the digits that are eligible for "Go" trials
goNums<-c(1:7,9)
# Identify the "No Go" digit
noGo<-8

for(runNumber in 1:3){
  for(thoughtNumber in 1:9){
# Randomly select among 12, 13, or 14 to determine total number of Go Trials for this run
numGoTrials<-sample(12:14, 1)
# Calculate how many total trials this run will have (the Go trials plus 5 No Go)
totalTrials<-numGoTrials+5

# Randomly select from eligible digits to obtain stimuli for Go Trials
goTrials<-sample(goNums, numGoTrials, replace=TRUE) 

goTrials

# Select the set of all eligible permutations of stimulus orders for this person
orderfile<-case_when(numGoTrials == 12 ~ "orders12.csv",
          numGoTrials == 13 ~ "orders13.csv",
          numGoTrials == 14 ~ "orders14.csv")

orders<-read.csv(orderfile, stringsAsFactors = FALSE)
  
ordering<-orders[sample(1:nrow(orders), 1),1:totalTrials]

stimuli<-rep(NA, totalTrials)
n<-1

for(i in 1:totalTrials){
  if(ordering[i]=="go"){
         stimuli[i]=goTrials[n]
         n<-n+1
  } 
  else {
    stimuli[i]=8
}
}

ordering
stimuli

runinfo<-cbind.data.frame(participant,runNumber, t(rbind(ordering, stimuli)))

names(runinfo)[3:4]<-c("type","stimulus")

runinfo<-runinfo%>%mutate(correct=case_when(type=="go" ~ '2',
                                   type=="nogo" ~ 'None'))

write.csv(runinfo,
          paste0("SART_subject",participant,"_run",runNumber,"_thought",thoughtNumber,".csv"), row.names=FALSE)
  }
}
