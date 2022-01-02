                # for i , BS in enumerate(BS_array):
                #     if(Find_BS):
                #         break
                #     distance = ((BS.rect.x - car.rect.x)**2 + (BS.rect.y - car.rect.y)**2 ) **0.5 / KM_RATIO
                #     path_loss =  32.45 + (20 * math.log10(BS.frequency)) + (20 * math.log10(distance))
                #     Receive_DB = 120 - path_loss
                #     if(MAX_DB - Receive_DB < MyAlgorithm_error_THRESHOLD):
                #         distance2 = ((BS.rect.x - tx)**2 + (BS.rect.y - ty)**2 ) **0.5 / KM_RATIO
                #         path_loss2 =  32.45 + (20 * math.log10(BS.frequency)) + (20 * math.log10(distance2))
                #         Receive_DB2 = 120 - path_loss2
                #         if(MAX_DB - Receive_DB2 < MyAlgorithm_error_THRESHOLD):
                #             Find_BS = True
                #             if(car.connect[index] != -1 and car.connect[index] != i):
                #                 total_switch[index] += 1
                #             car.connect[index] = i
                #             car.DB[index] = Receive_DB
                #             car.color[index] = BS.color
                #             if(index == Algorithm_mode):
                #                 car.image.fill(car.color[index])