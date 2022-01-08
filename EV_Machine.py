print("Welcome to the Electronic Voting machine !!\n")
print("---------------------------------------------\n")


nominee1 = input("Enter the name of firt nominee : ")
nominee2 = input("Enter the name of second nominee : ")


nominee1_votes = 0
nominee2_votes = 0


voter_id = [1,2,3,4,5,6,7,8,9,10]
no_of_voter = len(voter_id)


while True :
    if voter_id == []:
        print("Voting session is over  !!")


        if(nominee1_votes > nominee2_votes):
            percentage = (nominee1_votes//no_of_voter)*100
            print(f"{nominee1} is Winner with {percentage}% votes !!")
            break


        elif(nominee1_votes < nominee2_votes):
            percentage = (nominee2_votes/no_of_voter)*100
            print(f"{nominee2} is Winner with {percentage}% votes !!")
            break
            

        else:
            print(" Election is draw !!")
            break
        

    voter = int(input("Enter your voter id : "))
    
    if voter in voter_id:
        print("You can vote ")
        voter_id.remove(voter)


        print("--------------------------------------------------------------------------------\n")

        vote = int(input(f"To give vote to {nominee1} Press 1 and to gove vote to {nominee2} Press 2 :  "))
        print("\n")

        print("---------------------------------------------------------------------------------")


        if vote == 1:
             nominee1_votes += 1
             print(f"Thanks to give vote to {nominee1} !!")


        elif vote == 2:
             nominee2_votes += 1
             print(f"Thanks for giving vote to {nominee2} !!")    


        else:
            print("Select the correct voter !!   ")
            

    
