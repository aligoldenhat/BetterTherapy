def SecToFrame(data, frame):
    listed = list(data)
    frame_result = []
    emotion_result = []

    for i in range(len(listed)):
        live_sec = listed[i].split('_')
        x = int(live_sec[0])
        y = int(live_sec[1])
        if x == 0:
            frame_result.append(x*frame)
            frame_result.append(y*frame)
        else:
            frame_result.append(y*frame)

        emotion_result.append(data[listed[i]])
    
    return frame_result, emotion_result
        
def MergingData(SA_data, AET_data, FED_data, frame, how_much_change_AET, how_much_change_SA):
    SA_data = SecToFrame(SA_data, frame)
    AET_data = SecToFrame(AET_data, frame)

    how_much_change_SA = how_much_change_SA * frame
    how_much_change_AET = how_much_change_AET * frame

    for i in range(len(SA_data[1])):
        for j in range(SA_data[0][i], SA_data[0][i+1]):
            if SA_data[1][i] == 1:
                x = []
                x = [p for p in FED_data[j+1]]
                x[3] += how_much_change_SA
                if x[4] > how_much_change_SA:
                    x[4] -= how_much_change_SA
                FED_data[j+1] = tuple(x)
            else:
                x = []
                x = [p for p in FED_data[j+1]]
                x[4] += how_much_change_SA
                #x[3] += how_much_change_SA 
                FED_data[j+1] = tuple(x)
    
    for i in range(len(FED_data)):
        x = []
        x = [p for p in FED_data[i+1]]
        x.append(0)
        x.append(0)
        FED_data[i+1] = tuple(x)

    for i in range(len(AET_data[1])):
        for j in range(AET_data[0][i], AET_data[0][i+1]):
            if AET_data[1][i] == 6:      #Surprise
                x = []
                x = [p for p in FED_data[j+1]]
                x[0] += how_much_change_AET
                FED_data[j+1] = tuple(x)

            elif AET_data[1][i] == 4:    #Neutral
                x = []
                x = [p for p in FED_data[j+1]]
                x[1] += how_much_change_AET
                FED_data[j+1] = tuple(x)

            elif AET_data[1][i] == 0:    #Anger
                x = []
                x = [p for p in FED_data[j+1]]
                x[2] += how_much_change_AET
                FED_data[j+1] = tuple(x)

            elif AET_data[1][i] == 3:    #Happy
                x = []
                x = [p for p in FED_data[j+1]]
                x[3] += how_much_change_AET
                if x[4] > how_much_change_AET:
                    x[4] -= how_much_change_AET
                FED_data[j+1] = tuple(x)

            elif AET_data[1][i] == 5:    #Sad
                x = []
                x = [p for p in FED_data[j+1]]
                x[4] += how_much_change_AET *1.5
                if x[3] > how_much_change_AET:
                    x[3] -= how_much_change_AET
                FED_data[j+1] = tuple(x)

            elif AET_data[1][i] == 1:    #Disgust
                x = []
                x = [p for p in FED_data[j+1]]
                x[5] += how_much_change_AET*1.5
                FED_data[j+1] = tuple(x)

            elif AET_data[1][i] == 2:    #Fear
                x = []
                x = [p for p in FED_data[j+1]]
                x[6] += how_much_change_AET
                FED_data[j+1] = tuple(x)
    return FED_data
