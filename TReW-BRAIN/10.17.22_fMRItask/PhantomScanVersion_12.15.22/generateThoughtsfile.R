library(dplyr)

# Researcher assistants: customize this section below here! --------------------------------------------

# Fill in with correct participant number (in quotes, with leading zeroes, e.g., "001")
participant<-"001"

# Make sure your participant's thoughts file is labeled like this:
# "Thoughts_subject001.csv" and is located in the same folder as this script

# Stop customizing! Don't change code below!------------------------------------------

# Will read in appropriately titled thoughts file eg Thoughts_subject001.csv
# Two columns: Intensity (high or low) and Thought (prompt word or phrase)
subjectThoughts<-read.csv(paste0("Thoughts_subject",participant,".csv"), stringsAsFactors = FALSE)

highInt<-subjectThoughts%>%filter(Intensity=="high")
lowInt<-subjectThoughts%>%filter(Intensity=="low")

# According to the preregistration, "Blocks are counterbalanced within participant" with the following arrangement for everyone:
# Run 1: High, high, low, high, high, low, high, high, low
# Run 2: High, low, high, high, low, high, high, low, high 
# Run 3: Low, high, high, low, high, high, low, high, high


# Run 1 Thought Stimuli Ordering --------------------------------------------------

# Run 1: High, high, low, high, high, low, high, high, low

subjectThoughts1<-data.frame("ThoughtNumber"=1:9,
                             "Thought"=NA,
                             "Intensity"=c("high","high","low","high","high","low","high","high","low"),
                             stringsAsFactors = FALSE)

# Randomly re-order thoughts within intensity levels
subjectThoughts1$Thought[c(1,2,4,5,7,8)]<-sample(highInt$Thought)
subjectThoughts1$Thought[c(3,6,9)]<-sample(lowInt$Thought)


# Run 2 Thought Stimuli Ordering ----------------------------------------

# Run 2: High, low, high, high, low, high, high, low, high 

subjectThoughts2<-data.frame("ThoughtNumber"=1:9,
                             "Thought"=NA,
                             "Intensity"=c("high","low","high","high","low","high","high","low","high"),
                             stringsAsFactors = FALSE)

# Randomly re-order thoughts within intensity levels
subjectThoughts2$Thought[c(1,3,4,6,7,9)]<-sample(highInt$Thought)
subjectThoughts2$Thought[c(2,5,8)]<-sample(lowInt$Thought)


# Run 3 Thought Stimuli Ordering ------------------------------------------

# Run 3: Low, high, high, low, high, high, low, high, high

subjectThoughts3<-data.frame("ThoughtNumber"=1:9,
                             "Thought"=NA,
                             "Intensity"=c("low","high","high","low","high","high","low","high","high"),
                             stringsAsFactors = FALSE)

# Randomly re-order thoughts within intensity levels
subjectThoughts3$Thought[c(2,3,5,6,8,9)]<-sample(highInt$Thought)
subjectThoughts3$Thought[c(1,4,7)]<-sample(lowInt$Thought)


# Output files ------------------------------------------------------------

# Outputs three labeled files per participant with appropriately ordered thought stimuli for each run
write.csv(subjectThoughts1, paste0("ThoughtStimuli_subject",participant,"_run1.csv"), row.names=FALSE)
write.csv(subjectThoughts2, paste0("ThoughtStimuli_subject",participant,"_run2.csv"), row.names=FALSE)
write.csv(subjectThoughts3, paste0("ThoughtStimuli_subject",participant,"_run3.csv"), row.names=FALSE)
